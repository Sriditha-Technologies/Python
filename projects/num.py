import numpy as np

# Creating a 1D NumPy array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(array_1d)

# Creating a 2D NumPy array (matrix)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(array_2d)

# Accessing elements
print("\nAccessing an element:")
print("Element at row 1, column 2:", array_2d[1, 2])  # Output: 6

# Array operations
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

print("\nArray Addition:")
print("Array A + Array B:", array_a + array_b)  # Element-wise addition

print("\nArray Multiplication:")
print("Array A * Array B:", array_a * array_b)  # Element-wise multiplication

# Broadcasting example
array_c = np.array([[1], [2], [3]])
print("\nBroadcasting Example:")
print("Array C:")
print(array_c)
print("Array A + Array C (Broadcasting):")
print(array_a + array_c)