import cv2
from pathlib import Path
import numpy as np
from ultralytics import YOLO

# Load the YOLO model with your custom weights
weights_path = Path(__file__).resolve().parent / "weights" / "best.pt"
if not weights_path.is_file():
    raise FileNotFoundError(
        f"Custom YOLO weights not found at {weights_path}. "
        "Copy your trained best.pt into the weights/ folder."
    )
model = YOLO(str(weights_path))

# Initialize OpenCV tracker
tracker = cv2.TrackerCSRT_create()
tracking = False
bbox = None

# Video capture
ip_camera_url = 0
cap = cv2.VideoCapture(ip_camera_url)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# Get frame dimensions
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_center = (frame_width // 2, frame_height // 2)

# Central box size
central_box_size = 100
central_box_half_size = central_box_size // 2
central_box_top_left = (frame_center[0] - central_box_half_size, frame_center[1] - central_box_half_size)
central_box_bottom_right = (frame_center[0] + central_box_half_size, frame_center[1] + central_box_half_size)

# Field of view and screen size
FOV_HORIZ_DEG = 62.2
FOV_VERT_DEG = 48.8
SCREEN_WIDTH_CM = 37.6
SCREEN_HEIGHT_CM = 30.2

focal_length_x = SCREEN_WIDTH_CM / (2 * np.tan(np.radians(FOV_HORIZ_DEG / 2)))
focal_length_y = SCREEN_HEIGHT_CM / (2 * np.tan(np.radians(FOV_VERT_DEG / 2)))

def calculate_distance_x(x):
    pixel_distance_x = x - frame_center[0]
    distance_x_cm = (pixel_distance_x / frame_width) * SCREEN_WIDTH_CM
    return distance_x_cm

def calculate_distance_y(y):
    pixel_distance_y = frame_center[1] - y
    distance_y_cm = (pixel_distance_y / frame_height) * SCREEN_HEIGHT_CM
    return distance_y_cm

def calculate_depth(bbox_width, bbox_height):
    bbox_size_pixels = (bbox_width + bbox_height) / 2.0
    face_size_cm = 10
    depth_x_cm = face_size_cm * focal_length_x / bbox_size_pixels
    depth_y_cm = face_size_cm * focal_length_y / bbox_size_pixels
    depth_cm = (depth_x_cm + depth_y_cm) / 2.0
    return depth_cm

def draw_advanced_frame(frame, bbox, face_center, distance_x_cm, distance_y_cm, depth_cm, detection_confidence):
    p1 = (int(bbox[0]), int(bbox[1]))
    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
    cv2.rectangle(frame, p1, p2, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.line(frame, frame_center, face_center, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.line(frame, frame_center, face_center, (0, 255, 0), 1, cv2.LINE_AA, shift=4)

    cv2.line(frame, (bbox[0], face_center[1]), (bbox[0] + bbox[2], face_center[1]), (0, 255, 0), 1, cv2.LINE_AA)
    cv2.line(frame, (face_center[0], bbox[1] + bbox[3]), (face_center[0], bbox[1]), (0, 255, 0), 1, cv2.LINE_AA)

    cv2.circle(frame, face_center, 3, (255, 255, 0), -1, cv2.LINE_AA)
    cv2.arrowedLine(frame, (face_center[0], face_center[1]), (face_center[0], face_center[1] + int(depth_cm)), (255, 0, 255), 1, cv2.LINE_AA)

    """
    overlay = frame.copy()
    alpha = 0.6
    cv2.rectangle(overlay, (0, 0), (300, 150), (0, 0, 0), -1)
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
    """
    cv2.putText(frame, f'Distance X: {distance_x_cm:.2f} cm', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, f'Distance Y: {distance_y_cm:.2f} cm', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, f'Depth: {depth_cm:.2f} cm', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, f'Confidence: {detection_confidence:.2f}', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

while True:
    ret, frame = cap.read()
    if ret:
        #gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        frame =cv2.flip(frame, 1)
        results = model(frame)  # Perform inference

        # Check if any detections were made
        if results:
            for result in results[0].boxes:  # Iterate over detected objects
                x_min, y_min, x_max, y_max = result.xyxy[0]  # Access bounding box coordinates

                bbox = (int(x_min), int(y_min), int(x_max - x_min), int(y_max - y_min))


                tracker.init(frame, bbox)
                tracking = True

                ok, bbox = tracker.update(frame)
                if ok:
                    face_center = (int(bbox[0] + bbox[2] / 2), int(bbox[1] + bbox[3] / 2))

                    distance_x_cm = calculate_distance_x(face_center[0])
                    distance_y_cm = calculate_distance_y(face_center[1])
                    depth_cm = calculate_depth(bbox[2], bbox[3])

                    detection_confidence = result.conf[0]  # Get confidence score
                    draw_advanced_frame(frame, bbox, face_center, distance_x_cm, distance_y_cm, depth_cm, detection_confidence)

        # Display central box and other lines
        cv2.line(frame, (0, frame_center[1]), (frame_width, frame_center[1]), (0, 255, 255), 1)
        cv2.line(frame, (frame_center[0], 0), (frame_center[0], frame_height), (0, 255, 255), 1)
        cv2.rectangle(frame, central_box_top_left, central_box_bottom_right, (0, 255, 255), 2, cv2.LINE_AA)

        # Show original frame and grayscale frame
        cv2.imshow("Video", frame)
        
        #cv2.imshow("Grayscale", gray_frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()

