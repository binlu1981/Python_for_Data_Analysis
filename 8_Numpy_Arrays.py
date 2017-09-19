# -*- coding:utf-8 -*-
"""
@author:BinLu
@file:8_Numpy_Arrays.py
@time:2017-9-199:16
"""

"""Numpy and ndarray Basics
The numpy library is one of the core packages in Python's scientific software stack.
Many other Python data analysis libraries require numpy as a prerequisite,
because they use its ndarray data structure as a building block.
The Anaconda Python distribution we installed in part 1 comes with numpy.

Numpy implements a data structure called the N-dimensional array or ndarray.
ndarrays are similar to lists in that they contain a collection of items
that can be accessed via indexes. On the other hand, ndarrays are homogeneous,
meaning they can only contain objects of the same type and they can be multi-dimensional,
 making it easy to store 2-dimensional tables or matrices.
"""

import numpy as np
my_list = [1, 2, 3, 4]             # Define a list
my_array = np.array(my_list)       # Pass the list to np.array()
type(my_array)                     # Check the object's type

second_list = [5, 6, 7, 8]
#To create an array with more than one dimension, pass a nested list to np.array():
two_d_array = np.array([my_list, second_list])
print(two_d_array)
"""
[[1 2 3 4]
 [5 6 7 8]]
"""
two_d_array.shape
#(2,4)

"""The output above shows that this ndarray is 2-dimensional, since there are two values listed,
and the dimensions have length 2 and 4.
Check the total size (total number of items) in an array with the size attribute:
"""
two_d_array.size
#8
two_d_array.dtype
#dtype('int32')

# np.identity() to create a square 2d array with 1's across the diagonal
np.identity(n = 5)      # Size of the array
"""
array([[ 1.,  0.,  0.,  0.,  0.],
       [ 0.,  1.,  0.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  0.,  0.,  1.,  0.],
       [ 0.,  0.,  0.,  0.,  1.]])
"""

# np.eye() to create a 2d array with 1's across a specified diagonal
np.eye(N = 3,  # Number of rows
       M = 5,  # Number of columns
       k = 1)  # Index of the diagonal (main diagonal (0) is default)
"""
array([[ 0.,  1.,  0.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  0.,  0.,  1.,  0.]])
"""

# np.ones() to create an array filled with ones:
np.ones(shape= [2,4])
"""
array([[ 1.,  1.,  1.,  1.],
       [ 1.,  1.,  1.,  1.]])
"""
# np.zeros() to create an array filled with zeros:
np.zeros(shape= [4,6])
"""
array([[ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.]])
"""

#If an ndarray has more than one dimension, separate indexes for each dimension with a comma:
# Create a new 2d array
two_d_array = np.array([one_d_array, one_d_array + 6, one_d_array + 12])
print(two_d_array)
"""
[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]
 [13 14 15 16 17 18]]
"""
# Get the element at row index 1, column index 4
two_d_array[1, 4]
#11

# Slice elements starting at row 2, and column 5
two_d_array[1:, 4:]
"""
array([[11, 12],
       [17, 18]])
"""
# Reverse both dimensions (180 degree rotation)
two_d_array[::-1, ::-1]
"""
array([[18, 17, 16, 15, 14, 13],
       [12, 11, 10,  9,  8,  7],
       [ 6,  5,  4,  3,  2,  1]])
"""

### Reshaping Arrays ###
#Reshape an array into a new array with the same data but different structure with np.reshape():
np.reshape(a=two_d_array,        # Array to reshape
           newshape=(6,3))       # Dimensions of the new array
"""
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [10, 11, 12],
       [13, 14, 15],
       [16, 17, 18]])
"""

#Unravel a multi-dimensional into 1 dimension with np.ravel():
np.ravel(a=two_d_array,
         order='C')         # Use C-style unraveling (by rows)
#array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

np.ravel(a=two_d_array,
         order='F')  # Use Fortran-style unraveling (by columns)
#array([1, 7, 13, 2, 8, 14, 3, 9, 15, 4, 10, 16, 5, 11, 17, 6, 12, 18])

#Alternatively, use ndarray.flatten() to flatten a multi-dimensional into 1 dimension and return a copy of the result:
two_d_array.flatten()
#array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

#Get the transpose of an array with ndarray.T:
"""
array([[ 1,  7, 13],
       [ 2,  8, 14],
       [ 3,  9, 15],
       [ 4, 10, 16],
       [ 5, 11, 17],
       [ 6, 12, 18]])
"""
#Flip an array vertically or horizontally with np.flipud() and np.fliplr() respectively:
np.flipud(two_d_array)
"""
array([[13, 14, 15, 16, 17, 18],
       [ 7,  8,  9, 10, 11, 12],
       [ 1,  2,  3,  4,  5,  6]])
"""
np.fliplr(two_d_array)
"""
array([[ 6,  5,  4,  3,  2,  1],
       [12, 11, 10,  9,  8,  7],
       [18, 17, 16, 15, 14, 13]])
"""

#Rotate an array 90 degrees counter-clockwise with np.rot90():
np.rot90(two_d_array,
         k=1)             # Number of 90 degree rotations
"""
array([[ 6, 12, 18],
       [ 5, 11, 17],
       [ 4, 10, 16],
       [ 3,  9, 15],
       [ 2,  8, 14],
       [ 1,  7, 13]])
"""

#Shift elements in an array along a given dimension with np.roll():
np.roll(a= two_d_array,
        shift = 2,        # Shift elements 2 positions
        axis = 1)         # In each row
"""
array([[ 5,  6,  1,  2,  3,  4],
       [11, 12,  7,  8,  9, 10],
       [17, 18, 13, 14, 15, 16]])
"""

#Leave the axis argument empty to shift on a flattened version of the array (shift across all dimensions):
np.roll(a= two_d_array,
        shift = 2)
"""
array([[17, 18,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15, 16]])
"""

#Join arrays along an axis with np.concatenate():
array_to_join = np.array([[10,20,30],[40,50,60],[70,80,90]])

np.concatenate( (two_d_array,array_to_join),  # Arrays to join
               axis=1)                        # Axis to join upon
"""
array([[ 1,  2,  3,  4,  5,  6, 10, 20, 30],
       [ 7,  8,  9, 10, 11, 12, 40, 50, 60],
       [13, 14, 15, 16, 17, 18, 70, 80, 90]])
"""


##### Array Math Operations #####
two_d_array + 100    # Add 100 to each element
"""
array([[101, 102, 103, 104, 105, 106],
       [107, 108, 109, 110, 111, 112],
       [113, 114, 115, 116, 117, 118]])
"""
two_d_array - 100    # Subtract 100 from each element
"""
array([[-99, -98, -97, -96, -95, -94],
       [-93, -92, -91, -90, -89, -88],
       [-87, -86, -85, -84, -83, -82]])
"""
two_d_array * 2      # Multiply each element by 2
"""
array([[ 2,  4,  6,  8, 10, 12],
       [14, 16, 18, 20, 22, 24],
       [26, 28, 30, 32, 34, 36]])
"""

two_d_array / 2      # Divide each element by 2
"""
array([[ 0.5,  1. ,  1.5,  2. ,  2.5,  3. ],
       [ 3.5,  4. ,  4.5,  5. ,  5.5,  6. ],
       [ 6.5,  7. ,  7.5,  8. ,  8.5,  9. ]])
"""
two_d_array ** 2      # Square each element
"""
array([[  1,   4,   9,  16,  25,  36],
       [ 49,  64,  81, 100, 121, 144],
       [169, 196, 225, 256, 289, 324]])
"""
two_d_array % 2       # Take modulus of each element
"""
array([[1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0]], dtype=int32)
"""
"""
Beyond operating on each element of an array with a single scalar value,
you can also use the basic math operators on two arrays with the same shape.
When operating on two arrays, the basic math operators function in an element-wise fashion,
returning an array with the same shape as the original:
"""
small_array1 = np.array([[1,2],[3,4]])
small_array1 + small_array1
"""
array([[2, 4],
       [6, 8]])
"""
small_array1 - small_array1
"""
array([[0, 0],
       [0, 0]])
"""
small_array1 * small_array1
"""
array([[ 1,  4],
       [ 9, 16]])
"""
small_array1 / small_array1
"""
array([[ 1.,  1.],
       [ 1.,  1.]])
"""
small_array1 ** small_array1
"""
array([[  1,   4],
       [ 27, 256]], dtype=int32)
"""

# Get the mean of all the elements in an array with np.mean()
np.mean(two_d_array)
#9.5
# Provide an axis argument to get means across a dimension
np.mean(two_d_array,
        axis = 1)     # Get means of each row
#array([  3.5,   9.5,  15.5])
# Get the standard deviation all the elements in an array with np.std()
np.std(two_d_array)
# 5.1881274720911268

# Provide an axis argument to get standard deviations across a dimension
np.std(two_d_array,
        axis = 0)     # Get stdev for each column
"""
array([ 4.89897949,  4.89897949,  4.89897949,  4.89897949,  4.89897949,
        4.89897949])
"""
# Sum the elements of an array across an axis with np.sum()
np.sum(two_d_array,
       axis=1)        # Get the row sums
#array([21, 57, 93])
np.sum(two_d_array,
       axis=0)        # Get the column sums
#array([21, 24, 27, 30, 33, 36])

# Take the log of each element in an array with np.log()
np.log(two_d_array)
"""
array([[ 0.        ,  0.69314718,  1.09861229,  1.38629436,  1.60943791,
         1.79175947],
       [ 1.94591015,  2.07944154,  2.19722458,  2.30258509,  2.39789527,
         2.48490665],
       [ 2.56494936,  2.63905733,  2.7080502 ,  2.77258872,  2.83321334,
         2.89037176]])
"""
# Take the square root of each element with np.sqrt()
np.sqrt(two_d_array)
"""
array([[ 1.        ,  1.41421356,  1.73205081,  2.        ,  2.23606798,
         2.44948974],
       [ 2.64575131,  2.82842712,  3.        ,  3.16227766,  3.31662479,
         3.46410162],
       [ 3.60555128,  3.74165739,  3.87298335,  4.        ,  4.12310563,
         4.24264069]])
"""

"""
take the dot product of two arrays with np.dot().
This function performs an element-wise multiply and then a sum
for 1-dimensional arrays (vectors) and matrix multiplication for 2-dimensional arrays
"""
# Take the vector dot product of row 0 and row 1
np.dot(two_d_array[0,0:],  # Slice row 0
       two_d_array[1,0:])  # Slice row 1
#217

# Do a matrix multiply
np.dot(small_array1, small_array1)
"""
array([[7, 10],
       [15, 22]])
"""


