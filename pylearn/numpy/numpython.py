# numpy
"""
numpy adalah library Python yang digunakan untuk komputasi ilmiah dan analisis data. 
Library ini menyediakan struktur data array multidimensi yang efisien,
serta berbagai fungsi matematika untuk operasi pada array tersebut. 
Numpy sangat populer di kalangan ilmuwan data, insinyur, 
dan peneliti karena kemampuannya dalam menangani data besar dan kompleks dengan cepat.
"""

import numpy as np

arr = np.array([[1,2],[3,4]])
print(arr)
print(arr.shape) # Output: (2, 2)
print(arr.size) # Output: 4
print(arr.dtype) # Output: int64 (atau int32 tergantung pada platform)

# membuat array dengan np.array
arr1 = np.array([1, 2, 3, 4, 5]) # arrar 1D
arr2 = np.array([[1, 2, 3], [4, 5, 6]]) # array 2D
print(arr1)
print(arr2)

#fungsi khusus untuk membuat array
zeros = np.zeros((2, 3)) # Array 2x3 yang diisi dengan nol
ones = np.ones((3, 4)) # Array 3x4 yang diisi
random_arr = np.random.rand(2, 3) # Array 2x3 dengan nilai acak antara 0 dan 1
range_arr = np.arange(0, 10, 2) # Array dengan nilai dari 0 hingga 10 dengan langkah 2
linspace_arr = np.linspace(0, 1, 5) # Array dengan 5 nilai yang terdistribusi merata antara 0 dan 1
print(zeros)
print(ones)
print(random_arr)
print(range_arr)
print(linspace_arr)


# operasi pada array
# Operasi aritmatika
a = np.array([1, 2, 3,])
b = np.array([4, 5, 6,])
print(a + b) # Output: [5 7 9]
print(a - b) # Output: [-3 -3 -3]
print(a * b) # Output: [ 4 10 18]
print(a / b) # Output: [0.25 0.4  0

#pengindeksan dan slicing
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[0]) # Output: [1 2 3]
print(arr[1, 2]) # Output: 6
print(arr[:, 1]) # Output: [2 5 8]
print(arr[1:3, 0:2]) # Output: [[4 5]
print(arr[-1,-1]) # Output: 9

# mengubah bentuk array
arr = np.array([1, 2, 3,4,5])
reshaped_arr = arr.reshape((2, 3)) # Mengubah array menjadi bentuk 2x3
print(reshaped_arr) # Output: [[1 2 3]

#vstack array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
stacked_arr = np.vstack((arr1, arr2))
print(stacked_arr) # Output: [[1 2 3]

concatenated_arr = np.concatenate((arr1, arr2))
print(concatenated_arr) # Output: [1 2 3 4 5 6]

#fungsi matermatika
arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr)) # Output: 15
print(np.mean(arr)) # Output: 3.0
print(np.median(arr)) # Output: 3.0
print(np.std(arr)) # Output: 1.4142135623730951

#fungsi aljabar linear
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B)) # Output: [[19 22]



