import math
import numpy as np
from PIL import Image



class Array:
    def __init__(self, data):
        self.data = data
        self.shape = self.get_shape(data)
        self.dimension=self.get_dimension(data)
        self.size=self.get_size(data)
        
    
    def get_shape(self,data):
        if isinstance(data, list):             
            rows = len(data)

            if isinstance(data[0], list):       
                cols = len(data[0])

                if isinstance(data[0][0], list):  
                    dimension = len(data[0][0])
                    return (rows, cols, dimension)

                return (rows, cols, 0)          
            return (rows, 0, 0)                 
        return (0, 0, 0)  
    
    def get_dimension(self,data):
        if isinstance(data, list):
            if isinstance(data[0], list):
                if isinstance(data[0][0], list):
                    return 3  
                return 2       
            return 1           
        return 0 
                
    

        
    def get_size(self, data):
        if self.dimension == 1:
            return len(data)
        elif self.dimension == 2:
            return len(data) * len(data[0])
        elif self.dimension == 3:
            return len(data) * len(data[0]) * len(data[0][0])
        else:
            return 0
        
    def flat(self, data):
        flat_list = []

        dim = self.get_dimension(data)

        if dim == 1:
            for i in range(len(data)):
                flat_list.append(data[i])

        elif dim == 2:
            for i in range(len(data)):
                for j in range(len(data[0])):
                    flat_list.append(data[i][j])

        elif dim >= 3:
            for i in range(len(data)):
                for j in range(len(data[0])):
                    for k in range(len(data[0][0])):
                        flat_list.append(data[i][j][k])

        return flat_list

    def reshape(self, data, row, col, depth):
        ##if self.get_size(data) != row * col * depth:
            ##return "Error: sizes do not match"
        if row != 0 and depth == 0 and col == 0:
            n_data=data
        
        if row != 0 and depth != 0 and col != 0:
            array = self.flat(data)
            n_data = []
            index = 0

            for i in range(row):
                row_l = []
                for j in range(col):
                    col_l = []
                    for k in range(depth): 
                        col_l.append(array[index])   
                        index += 1
                    row_l.append(col_l)              
                n_data.append(row_l) 

        if row != 0 and depth == 0 and col != 0:
            array = self.flat(data)
            n_data = []
            index = 0

            for i in range(row):
                row_l = []
                for j in range(col):
                    row_l.append(array[index])
                    index += 1
                n_data.append(row_l)

        return n_data
    
    def transpose(self,data):
        if self.get_dimension(data) != 2:
            return "Transpose only work for 2D array"
        
        array=[]
        for i in range(len(data[0])):
            row=[]
            for j in  range(len(data)):
                row.append(data[j][i])
            array.append(row)
        return array


    def zero(self, row, col):
        zero = []
        for i in range(row):          
            row_l = []
            for j in range(col):    
                row_l.append(0)     
            zero.append(row_l)       
        return zero

    def one(self, row, col):
        one = []
        for i in range(row):          
            row_l = []
            for j in range(col):    
                row_l.append(1)     
            one.append(row_l)       
        return one
    
    def eye(self,row,col):
        if row!=col:
            return"error"
        eye=self.zero(row,col)
        
        if row == col:
            for i  in range(row):
                eye[i][i]=1
        return eye
    
    def arrange(self,start,stop,step):
        
        arrange_m=[]
        for i in range (start,stop,step):
                arrange_m.append(i)
        return arrange_m
    
      

    def linspace(self, start, stop, number):
        value = (stop - start) / (number - 1)
        linspace_array = []
        for i in range(number):
            linspace_array.append(start + i * value)
        return linspace_array               
        

    def add(self, array_1, array_2):
        if self.get_dimension(array_1)!=self.get_dimension(array_2):
            return"error"
        if self.get_dimension(array_1)==self.get_dimension(array_2):
            a=[]
            a1=self.flat(array_1)
            a2=self.flat(array_2)
            for i in range(len(a1)):
                a.append(a1[i]+a2[i])
        dim = self.get_dimension(array_1)
        if dim == 1:
            array=self.reshape(a,len(array_1),0,0)
            
            
        elif dim == 2:
            array=self.reshape(a,len(array_1),len(array_1[0]),0)
            

        elif dim >= 3:
            
            array=self.reshape(a,len(array_1),len(array_1[0]),len(array_1[0][0]))
        return array

   


    def sub(self, array_1, array_2):
        if self.get_dimension(array_1)!=self.get_dimension(array_2):
            return"error"
        if self.get_dimension(array_1)==self.get_dimension(array_2):
            a=[]
            a1=self.flat(array_1)
            a2=self.flat(array_2)
            for i in range(len(a1)):
                a.append(a1[i]-a2[i])
        dim = self.get_dimension(array_1)
        if dim == 1:
            array=self.reshape(a,len(array_1),0,0)
            
            
        elif dim == 2:
            array=self.reshape(a,len(array_1),len(array_1[0]),0)
            

        elif dim >= 3:
            
            array=self.reshape(a,len(array_1),len(array_1[0]),len(array_1[0][0]))
        return array
    
    def element_wise_multiplication(self, array_1, array_2):
        if self.get_dimension(array_1)!=self.get_dimension(array_2):
            return"error"
        if self.get_dimension(array_1)==self.get_dimension(array_2):
            a=[]
            a1=self.flat(array_1)
            a2=self.flat(array_2)
            for i in range(len(a1)):
                a.append(a1[i]*a2[i])
        dim = self.get_dimension(array_1)
        if dim == 1:
            array=self.reshape(a,len(array_1),0,0)
            
            
        elif dim == 2:
            array=self.reshape(a,len(array_1),len(array_1[0]),0)
            

        elif dim >= 3:
            
            array=self.reshape(a,len(array_1),len(array_1[0]),len(array_1[0][0]))
        return array
    
    def element_wise_dive(self, array_1, array_2):
        if self.get_dimension(array_1)!=self.get_dimension(array_2):
            return"error"
        if self.get_dimension(array_1)==self.get_dimension(array_2):
            a=[]
            a1=self.flat(array_1)
            a2=self.flat(array_2)
            for i in range(len(a1)):
                a.append(a1[i]/a2[i])
        dim = self.get_dimension(array_1)
        if dim == 1:
            array=self.reshape(a,len(array_1),0,0)
            
            
        elif dim == 2:
            array=self.reshape(a,len(array_1),len(array_1[0]),0)
            

        elif dim >= 3:
            
            array=self.reshape(a,len(array_1),len(array_1[0]),len(array_1[0][0]))
        return array
    def element_wise_double (self, array_1):
   
        a=[]
        a1=self.flat(array_1)
            
        for i in range(len(a1)):
                a.append(a1[i]*a1[i])
        dim = self.get_dimension(array_1)
        if dim == 1:
            array=self.reshape(a,len(array_1),0,0)
            
            
        elif dim == 2:
            array=self.reshape(a,len(array_1),len(array_1[0]),0)
            

        elif dim >= 3:
            
            array=self.reshape(a,len(array_1),len(array_1[0]),len(array_1[0][0]))
        return array
    
    def exp(self, array_1):
        a=[]
        a1=self.flat(array_1)
            
        for i in range(len(a1)):
                a.append(math.exp(a1[i]))
        dim = self.get_dimension(array_1)
        if dim == 1:
            array=self.reshape(a,len(array_1),0,0)
            
            
        elif dim == 2:
            array=self.reshape(a,len(array_1),len(array_1[0]),0)
            

        elif dim >= 3:
            
            array=self.reshape(a,len(array_1),len(array_1[0]),len(array_1[0][0]))
        return array
    
    
    def log(self, array_1):
        a=[]
        a1=self.flat(array_1)
            
        for i in range(len(a1)):
                a.append(math.log(a1[i]))
        dim = self.get_dimension(array_1)
        if dim == 1:
            array=self.reshape(a,len(array_1),0,0)
            
            
        elif dim == 2:
            array=self.reshape(a,len(array_1),len(array_1[0]),0)
            

        elif dim >= 3:
            
            array=self.reshape(a,len(array_1),len(array_1[0]),len(array_1[0][0]))
        return array
    
    def sqrt(self, array_1):
        a=[]
        a1=self.flat(array_1)
            
        for i in range(len(a1)):
                a.append(math.sqrt(a1[i]))
        dim = self.get_dimension(array_1)
        if dim == 1:
            array=self.reshape(a,len(array_1),0,0)
            
            
        elif dim == 2:
            array=self.reshape(a,len(array_1),len(array_1[0]),0)
            

        elif dim >= 3:
            
            array=self.reshape(a,len(array_1),len(array_1[0]),len(array_1[0][0]))
        return array
    def abs(self, array_1):
        a=[]
        a1=self.flat(array_1)
            
        for i in range(len(a1)):
                a.append(math.fabs(a1[i]))
        dim = self.get_dimension(array_1)
        if dim == 1:
            array=self.reshape(a,len(array_1),0,0)
            
            
        elif dim == 2:
            array=self.reshape(a,len(array_1),len(array_1[0]),0)
            

        elif dim >= 3:
            
            array=self.reshape(a,len(array_1),len(array_1[0]),len(array_1[0][0]))
        return array
    
    def sum(self, array_1):
        total = 0
        a1=self.flat(array_1)
        for i in range(len(a1)):
            total+=a1[i]
        return total

    def mean(self, array_1):

        mean=self.sum(array_1)/len(self.flat(array_1))
       
        return mean 

    def max(self, array_1):
       
        a1=self.flat(array_1)
        ma=max(a1)
        return ma

    def min(self, array_1):
       
        a1=self.flat(array_1)
        ma=min(a1)
        return ma
    

    def argmax(self, data):
        a1 = self.flat(data)
        ma = max(a1)
        dim = self.get_dimension(data)
        if dim == 1:
            for i in range(len(data)):
                if data[i] == ma:
                    return (f"row:{i}")
        elif dim == 2:
            for i in range(len(data)):
                for j in range(len(data[0])):
                    if data[i][j] == ma:
                            return (f"row:{i}", f"col:{j}")
        elif dim == 3:           
            for i in range(len(data)):
                for j in range(len(data[0])):
                    for k in range(len(data[0][0])):
                        if data[i][j][k] == ma:
                            return (f"row:{i}", f"col:{j}", f"depth:{k}")
    def argmin(self, data):
        a1 = self.flat(data)
        ma = min(a1)
        dim = self.get_dimension(data)
        if dim == 1:
            for i in range(len(data)):
                if data[i] == ma:
                    return (f"row:{i}")
        elif dim == 2:
            for i in range(len(data)):
                for j in range(len(data[0])):
                    if data[i][j] == ma:
                            return (f"row:{i}", f"col:{j}")
        elif dim == 3:           
            for i in range(len(data)):
                for j in range(len(data[0])):
                    for k in range(len(data[0][0])):
                        if data[i][j][k] == ma:
                            return (f"row:{i}", f"col:{j}", f"depth:{k}")
                        
    def matmul(self, a1, a2):
        dem_1 = self.get_dimension(a1)
        dem_2 = self.get_dimension(a2)
        
    
        if dem_1 <= 2 and dem_2 <= 2:
            if len(a1[0]) != len(a2):
                return "Error: incompatible dimensions"
            array = []
            for k in range(len(a1)):
                row = []
                for i in range(len(a2[0])):
                    value = 0
                    for j in range(len(a1[0])):
                        value += a1[k][j] * a2[j][i]
                    row.append(value)
                array.append(row)
            return array
        
    
        elif dem_1 >= 3 and dem_2 >= 3:
            if len(a1[0][0]) != len(a2[0]):
                return "Error: incompatible dimensions for 3D"
            result_3d = []
            for x in range(len(a1)): 
                depth_array = []
                for k in range(len(a1[0])):  
                    row = []
                    for i in range(len(a2[0][0])):  
                        value = 0
                        for j in range(len(a1[0][0])): 
                            value += a1[x][k][j] * a2[x][j][i]
                        row.append(value)
                    depth_array.append(row)
                result_3d.append(depth_array)
            return result_3d
        
    def dot(self, a1, a2):
        dim_1=self.get_dimension(a1)
        dim_2=self.get_dimension(a2)
        
        if dim_1<dim_2:
            out_put=[]
            for i in range(len(a2[0])):  
                row=[]
                for j in range(len(a2)):  
                    row.append(a2[j][i])  
                value=0
                for x in range(len(a1)):
                    value += a1[x]*row[x] 
                out_put.append(value)
            return out_put
        
        if dim_1>dim_2:
            out_put=[]
            for i in range(len(a1[0])): 
                row=[]
                for j in range(len(a1)):  
                    row.append(a1[j][i])   
                value=0
                for x in range(len(a2)):
                    value += a2[x]*row[x] 
                out_put.append(value)
            return out_put
          
    def norm(self,data):
        array=self.flat(data)
        value=0
        for i in range(len(array)):
            value+=array[i]*array[i]
        value=math.sqrt(value)
        return value

    def det(self, data):
        dim = self.get_dimension(data)

        
        if len(data) == 2 and len(data[0]) == 2:
            detr = data[0][0] * data[1][1] - data[0][1] * data[1][0]   
            return detr

    
        if len(data) > 2 and dim == 2:
            pos = 0
            neg = 0
            array = []

            for i in range(len(data)):
                row = []
                for j in range(len(data)):
                    row.append(data[i][j])
                for k in range(len(data) - 1):
                    row.append(data[i][k])
                array.append(row)

            for x in range(len(array)):
                new_vector = []
                z = x
                for y in range(len(array)):
                    new_vector.append(array[y][z])
                    z += 1
                value = 1
                for c in range(len(new_vector)):
                    value *= new_vector[c]
                pos += value

            for x in range(len(array)):
                new_vector = []
                z = x
                for y in range(len(array) - 1, -1, -1):
                    new_vector.append(array[y][z])
                    z += 1
                value = 1
                for c in range(len(new_vector)):
                    value *= new_vector[c]
                neg -= value

            detr = pos + neg
            return detr

    
        if dim > 2:
            det_3d = []

            for d in range(dim):
                pos = 0            
                neg = 0
                array = []        

                for i in range(len(data)):
                    row = []
                    for j in range(len(data)):
                        row.append(data[i][j])
                    for k in range(len(data) - 1):
                        row.append(data[i][k])
                    array.append(row)

                for x in range(len(array)):
                    new_vector = []
                    z = x
                    for y in range(len(array)):
                        new_vector.append(array[y][z])
                        z += 1
                    value = 1
                    for c in range(len(new_vector)):
                        value *= new_vector[c]
                    pos += value

                for x in range(len(array)):
                    new_vector = []
                    z = x
                    for y in range(len(array) - 1, -1, -1):
                        new_vector.append(array[y][z])
                        z += 1
                    value = 1
                    for c in range(len(new_vector)):
                        value *= new_vector[c]
                    neg -= value

                detr = pos + neg
                det_3d.append(detr)

            return det_3d


    
    def det_1(self,matrix):
    
        n = len(matrix)

     
        if n == 1:
            return matrix[0][0]
       
        if n == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

        determinant = 0
       
        for j in range(n):
            sign = (-1) ** j
            element = matrix[0][j]

          
            minor = []
            for row in matrix[1:]:      
                new_row = row[:j] + row[j+1:] 
                minor.append(new_row)

           
            determinant += sign * element * self.det_1(minor)

        return determinant

    def scaler(self, data, scal):
        d = self.flat(data)
        row = []
        for i in range(len(d)):
            row.append(d[i] / scal) 
        fun = self.reshape(row, len(data), len(data[0]), 0)
        return fun

    def inv(self, data):
        array = self.det_1(data)
        inv_m = []
        dim = self.get_dimension(data)
        if dim == 1:
            return data

        if len(data) == len(data[0]) and dim >= 2:

            if len(data[0]) == 2:
                for i in range(len(data)):
                    row = []
                    for j in range(len(data[0])):
                        if i == 0 and j == 0:
                            row.append(data[1][1])
                        if i == 0 and j == 1:
                            row.append(-1 * data[0][1])
                        if i == 1 and j == 0:
                            row.append(-1 * data[1][0])
                        if i == 1 and j == 1:
                            row.append(data[0][0])
                    inv_m.append(row)
                v = self.scaler(inv_m, array)

            if len(data[0]) > 2:
                for i in range(len(data)):
                    r = []
                    for j in range(len(data[0])):
                        sign = (-1) ** (i + j)
                        minor = []
                        for row_idx in range(len(data)):
                            if row_idx != i:
                                new_row = []
                                for col_idx in range(len(data[0])):
                                    if col_idx != j:
                                        new_row.append(data[row_idx][col_idx])
                                minor.append(new_row)
                        determinant = self.det_1(minor) * sign
                        r.append(determinant)
                    inv_m.append(r)

                
                inv_m_T = []
                for i in range(len(inv_m[0])):
                    row = []
                    for j in range(len(inv_m)):
                        row.append(inv_m[j][i])
                    inv_m_T.append(row)

                v = self.scaler(inv_m_T, array)

        return v
    
       
    def load_image(self, image_path):
        img = Image.open(image_path).convert("RGB")
        w, h = img.size
        img_data = [[[img.getpixel((x, y))[c] for c in range(3)] for x in range(w)] for y in range(h)]
        return Array(img_data), w, h

    
    def scale_image(self, arr, sx=1, sy=1):
        h, w = arr.shape[0], arr.shape[1]

        
        S = [[sx, 0],
             [0, sy]]

        new_h, new_w = int(h*sy), int(w*sx)
        scaled_img_rgb = [[[0,0,0] for _ in range(new_w)] for _ in range(new_h)]

        for y in range(h):
            for x in range(w):
                xy = [[x],[y]]
                scaled_xy = self.matmul(S, xy)
                new_x, new_y = int(scaled_xy[0][0]), int(scaled_xy[1][0])
                if new_x < new_w and new_y < new_h:
                    scaled_img_rgb[new_y][new_x] = arr.data[y][x]

        return Array(scaled_img_rgb)

    
    def rotate_image(self, arr, angle_deg=0):
        angle_rad = math.radians(angle_deg)
        cos_a, sin_a = math.cos(angle_rad), math.sin(angle_rad)
        R = [[cos_a, -sin_a],
             [sin_a, cos_a]]

        h, w = arr.shape[0], arr.shape[1]
        cx, cy = w//2, h//2

        rotated_img_rgb = [[[0,0,0] for _ in range(w)] for _ in range(h)]

        for y in range(h):
            for x in range(w):
                xy = [[x-cx], [y-cy]]
                new_xy = self.matmul(R, xy)
                new_x = int(new_xy[0][0] + cx)
                new_y = int(new_xy[1][0] + cy)
                if 0 <= new_x < w and 0 <= new_y < h:
                    rotated_img_rgb[new_y][new_x] = arr.data[y][x]

        return Array(rotated_img_rgb)

    
    def translate_image(self, arr, tx=0, ty=0):
        h, w = arr.shape[0], arr.shape[1]
        translated_img_rgb = [[[0,0,0] for _ in range(w)] for _ in range(h)]

        for y in range(h):
            for x in range(w):
                new_x = x + tx
                new_y = y + ty
                if 0 <= new_x < w and 0 <= new_y < h:
                    translated_img_rgb[new_y][new_x] = arr.data[y][x]

        return Array(translated_img_rgb)

    
    def manipulate_colors(self, arr, red_increase=0, contrast=1, to_grayscale=False):
        h, w = arr.shape[0], arr.shape[1]
        new_img = []

        for y in range(h):
            row = []
            for x in range(w):
                pixel = arr.data[y][x]

                
                pixel[0] = min(255, pixel[0] + red_increase)

                
                pixel = self.element_wise_multiplication([[pixel[i] - 128 for i in range(3)]], [[contrast]*3])[0]
                pixel = [int(pixel[i]+128) for i in range(3)]

                
                if to_grayscale:
                    gray = sum(pixel)//3
                    pixel = [gray]*3

                row.append(pixel)
            new_img.append(row)

        return Array(new_img)

    
    def to_pil_image(self, arr):
        img = Image.new("RGB", (arr.shape[1], arr.shape[0]))
        for y in range(arr.shape[0]):
            for x in range(arr.shape[1]):
                img.putpixel((x, y), tuple(arr.data[y][x]))
        return img
    


data_3d = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

data_2d = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_2x2 = [
    [4, 7],
    [2, 6]
]

matrix_3x3 = [
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
]

arr_custom = Array(data_3d)
arr_np_3d = np.array(data_3d)
arr_custom_2d = Array(data_2d)
arr_np_2d = np.array(data_2d)


print("=== Shape & Size ===")
print("Custom 3D shape:", arr_custom.shape)
print("NumPy 3D shape:", arr_np_3d.shape)
print("Custom 3D size:", arr_custom.size)
print("NumPy 3D size:", arr_np_3d.size)


print("\n=== Reshape ===")
reshaped_custom = arr_custom.reshape(data_3d, 2, 2, 2)
reshaped_np = arr_np_3d.reshape(2, 2, 2)
print("Custom reshaped:", reshaped_custom)
print("NumPy reshaped:\n", reshaped_np)


print("\n=== Transpose 2D ===")
trans_custom = arr_custom_2d.transpose(data_2d)
trans_np = arr_np_2d.T
print("Custom transpose:", trans_custom)
print("NumPy transpose:\n", trans_np)


print("\n=== Zeros, Ones, Eye ===")
print("Custom zeros:", arr_custom_2d.zero(2, 3))
print("NumPy zeros:\n", np.zeros((2,3)))
print("Custom ones:", arr_custom_2d.one(3, 2))
print("NumPy ones:\n", np.ones((3,2)))
print("Custom eye:", arr_custom_2d.eye(3, 3))
print("NumPy eye:\n", np.eye(3))


a1 = Array([[1,2],[3,4]])
a2 = Array([[5,6],[7,8]])
np_a1 = np.array(a1.data)
np_a2 = np.array(a2.data)

print("\n=== Element-wise Operations ===")
print("Add:", a1.add(a1.data, a2.data))
print("NumPy add:\n", np_a1 + np_a2)
print("Sub:", a1.sub(a2.data, a1.data))
print("NumPy sub:\n", np_a2 - np_a1)
print("Multiplication:", a1.element_wise_multiplication(a1.data, a2.data))
print("NumPy multiplication:\n", np_a1 * np_a2)
print("Division:", a1.element_wise_dive(a2.data, a1.data))
print("NumPy division:\n", np_a2 / np_a1)
print("Double:", a1.element_wise_double(a1.data))
print("NumPy double:\n", np_a1 ** 2)


print("\n=== Math Functions ===")
print("Exp:", a1.exp(a1.data))
print("NumPy exp:\n", np.exp(np_a1))
print("Log:", a1.log(a1.data))
print("NumPy log:\n", np.log(np_a1))
print("Sqrt:", a1.sqrt(a1.data))
print("NumPy sqrt:\n", np.sqrt(np_a1))
print("Abs:", a1.abs([[-1, -2],[3,-4]]))
print("NumPy abs:\n", np.abs(np.array([[-1, -2],[3,-4]])))


print("\n=== Statistics ===")
print("Sum:", a1.sum(a1.data), "NumPy sum:", np.sum(np_a1))
print("Mean:", a1.mean(a1.data), "NumPy mean:", np.mean(np_a1))
print("Max:", a1.max(a1.data), "NumPy max:", np.max(np_a1))
print("Min:", a1.min(a1.data), "NumPy min:", np.min(np_a1))
print("Argmax:", a1.argmax(a1.data), "NumPy argmax:", np.unravel_index(np.argmax(np_a1), np_a1.shape))
print("Argmin:", a1.argmin(a1.data), "NumPy argmin:", np.unravel_index(np.argmin(np_a1), np_a1.shape))


A_1D = [1, 2, 3]
B_2D = [
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

A_2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B_2D_2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]


arr_A1D = Array(A_1D)
arr_B2D = Array(B_2D)
arr_A2D = Array(A_2D)
arr_B2D_2 = Array(B_2D_2)


np_A1D = np.array(A_1D)
np_B2D = np.array(B_2D)
np_A2D = np.array(A_2D)
np_B2D_2 = np.array(B_2D_2)

print("\n=== Test dot ===")
custom_dot = arr_A1D.dot(arr_A1D.data, arr_B2D.data)
numpy_dot = np.dot(np_A1D, np_B2D)
print("Custom dot     :", custom_dot)
print("NumPy dot      :", numpy_dot.tolist())

print("\n=== Test matmul ===")
custom_matmul = arr_A2D.matmul(arr_A2D.data, arr_B2D_2.data)
numpy_matmul = np.matmul(np_A2D, np_B2D_2)
print("Custom matmul  :", custom_matmul)
print("NumPy matmul   :", numpy_matmul.tolist())

print("\n=== Test norm ===")
custom_norm = arr_A2D.norm(arr_A2D.data)
numpy_norm = np.linalg.norm(np_A2D)
print("Custom norm    :", custom_norm)
print("NumPy norm     :", numpy_norm)


print("\n=== Determinant ===")
det_custom_2x2 = a1.det(matrix_2x2)
det_np_2x2 = np.linalg.det(np.array(matrix_2x2))
det_custom_3x3 = a1.det(matrix_3x3)
det_np_3x3 = np.linalg.det(np.array(matrix_3x3))
print("Custom 2x2 det:", det_custom_2x2, "NumPy 2x2 det:", det_np_2x2)
print("Custom 3x3 det:", det_custom_3x3, "NumPy 3x3 det:", det_np_3x3)


print("\n=== Laplace Cofactor Expansion ===")


A = [
    [2,  1,  3,  4],
    [0, -1,  2,  5],
    [7,  0,  1, -2],
    [3,  4,  0,  6]
]

arr = Array(A)
custom_det = arr.det_1(A)
numpy_det = np.linalg.det(np.array(A))

print("Custom Determinant :", custom_det)
print("NumPy Determinant  :", numpy_det)

print("\n=== TEST_Inverse ===")


A = [
    [2,  1,  3,  4],
    [0, -1,  2,  5],
    [7,  0,  1, -2],
    [3,  4,  0,  6]
]

arr = Array(A)
custom_det = arr.inv(A)
numpy_det = np.linalg.inv(np.array(A))

print("Custom Inverse :", custom_det)
print("NumPy Inverse  :", numpy_det)

print("\n=== IMAGE TRANSFORMATION TEST ===")


image_path = "C:/Users/dell/Desktop/python_pro_jawad_hassan/abstract-painting.jpg"  

arr_img, w, h = arr_custom.load_image(image_path)
print("Loaded image shape:", arr_img.shape)
arr_custom.to_pil_image(arr_img).save("original_image.jpg")


scaled_img = arr_custom.scale_image(arr_img, sx=0.5, sy=0.5)
print("Scaled image shape:", scaled_img.shape)
arr_custom.to_pil_image(scaled_img).save("scaled_image.jpg")


rotated_img = arr_custom.rotate_image(arr_img, angle_deg=45)
print("Rotated image shape:", rotated_img.shape)
arr_custom.to_pil_image(rotated_img).save("rotated_image.jpg")


translated_img = arr_custom.translate_image(arr_img, tx=10, ty=20)
print("Translated image shape:", translated_img.shape)
arr_custom.to_pil_image(translated_img).save("translated_image.jpg")


red_img = arr_custom.manipulate_colors(arr_img, red_increase=50, contrast=1, to_grayscale=False)
arr_custom.to_pil_image(red_img).save("red_increased.jpg")


gray_img = arr_custom.manipulate_colors(arr_img, red_increase=0, contrast=1, to_grayscale=True)
arr_custom.to_pil_image(gray_img).save("grayscale.jpg")


contrast_img = arr_custom.manipulate_colors(arr_img, red_increase=0, contrast=1.5, to_grayscale=False)
arr_custom.to_pil_image(contrast_img).save("contrast_adjusted.jpg")


combined_width = arr_img.shape[1] * 3
combined_height = arr_img.shape[0]

final_img = Image.new("RGB", (combined_width, combined_height))


final_img.paste(arr_custom.to_pil_image(red_img), (0, 0))
final_img.paste(arr_custom.to_pil_image(gray_img), (arr_img.shape[1], 0))
final_img.paste(arr_custom.to_pil_image(contrast_img), (arr_img.shape[1]*2, 0))

final_img.save("final_manipulated_result.jpg")
print("All images saved and final combined image created: 'final_manipulated_result.jpg'")

