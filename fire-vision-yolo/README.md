# YOLO Fire Detection — Computer Vision Prototype

A webcam-based Python prototype using **custom YOLO weights** for fire detection, combined with OpenCV drawing and CSRT tracker calls.

## Features

- Live video input through OpenCV (`cv2.VideoCapture(0)`).
- Per-frame inference with a custom **Ultralytics YOLO** fire-detection model.
- Detection bounding boxes and confidence display.
- CSRT tracker initialization and immediate update for each detection.
- On-frame overlays: box center, reference crosshair, horizontal and vertical offsets, and an illustrative depth estimate.

## Setup

Install Python 3.10+ and the dependencies:

```bash
pip install -r requirements.txt
```

Put your own trained weights at `weights/best.pt` (the weights file is **not** included here), connect a webcam, then run:

```bash
python fire_detection_tracking.py
```

Press `x` to exit the preview. The script assumes a local desktop session with a camera. The original local Windows path has been replaced with a project-relative path, for portability.

## Important limitations

- The source file is a prototype, not a validated fire-safety system.
- The example contains a reference object size of **10 cm** and predefined screen/camera geometry. Its printed depth value is an *illustrative estimate*, not a calibrated physical distance. It should not be used for UAV navigation or safety decisions.
- The CSRT tracker is reinitialized for detections on each frame; this is not robust persistent multi-frame object tracking or multi-object ID tracking.
- A working camera, custom model weights, and an OpenCV build supporting `TrackerCSRT_create` are required.
- The repository does not include model training data, performance validation, or pretrained weight files.

## Code

[fire_detection_tracking.py](fire_detection_tracking.py)

Part of [the portfolio's software projects](../index.html#fire-vision).