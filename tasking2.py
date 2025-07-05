#Import NumPy and print the version.
import numpy as np
print("NumPy version:", np.__version__)
#Create a 1D NumPy array from a Python list.
def create_1d_array_from_list(lst):
    return np.array(lst)
lst = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))
array_1d = create_1d_array_from_list(lst)
print("1D NumPy array:", array_1d)
#Create a NumPy array of all zeros with size 5.
def create_zeros_array(size):
    return np.zeros(size)
size = int(input("Enter the size of the zeros array: "))
zeros_array = create_zeros_array(size)
print("Array of zeros:", zeros_array)
#Create a NumPy array of all ones with size 3.
def create_ones_array(size):
    return np.ones(size)
size = int(input("Enter the size of the ones array: "))
ones_array = create_ones_array(size)
print("Array of ones:", ones_array)
#Create a NumPy array with values ranging from 10 to 20.
def create_range_array(start, end):
    return np.arange(start, end + 1)
start = int(input("Enter the start value of the range: "))
end = int(input("Enter the end value of the range: "))
range_array = create_range_array(start, end)
print("Array with values from", start, "to", end, ":", range_array)
#Create an array of even numbers from 2 to 20.
def create_even_array(start, end):
    return np.arange(start, end + 1, 2)
start = int(input("Enter the start value for even numbers: "))
end = int(input("Enter the end value for even numbers: "))
even_array = create_even_array(start, end)
print("Array of even numbers from", start, "to", end, ":", even_array)
#Create a 3x3 matrix with random integers from 1 to 10.
def create_random_matrix(rows, cols, low, high):
    return np.random.randint(low, high + 1, size=(rows, cols))
rows = int(input("Enter the number of rows for the random matrix: "))
cols = int(input("Enter the number of columns for the random matrix: "))
low = int(input("Enter the lower bound for random integers: "))
high = int(input("Enter the upper bound for random integers: "))
random_matrix = create_random_matrix(rows, cols, low, high)
print("3x3 matrix with random integers from", low, "to", high, ":\n", random_matrix)
#Create a 2D array of shape (2, 3) filled with any number.
def create_2d_array(shape, fill_value):
    return np.full(shape, fill_value)
shape = (2, 3)
fill_value = int(input("Enter the fill value for the 2D array: "))
array_2d = create_2d_array(shape, fill_value)
print("2D array of shape", shape, "filled with", fill_value, ":\n", array_2d)
#Create a NumPy array and find its shape and data type.
def create_array_and_get_info(lst):
    array = np.array(lst)
    return array.shape, array.dtype
lst = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))
shape, dtype = create_array_and_get_info(lst)
print("Array shape:", shape)
print("Array data type:", dtype)
