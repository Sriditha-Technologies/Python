import numpy as np

# Creating a 1-dimensional array
array1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array1d)

# Creating a 2-dimensional array (matrix)
array2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", array2d)

# Performing element-wise operations
array1d_squared = array1d ** 2
print("\nSquared 1D Array:", array1d_squared)

# Adding a scalar to an array
array1d_plus_two = array1d + 2
print("\n1D Array + 2:", array1d_plus_two)

# Broadcasting example
array2d_broadcasted = array2d + np.array([1, 0, 2])  # Adding a 1D array to each row of the 2D array
print("\nBroadcasted 2D Array:\n", array2d_broadcasted)

# Summing elements along an axis
row_sum = np.sum(array2d, axis=0)  # Sum each column
print("\nSum of each column:", row_sum)

# Reshaping an array
reshaped_array = np.reshape(array1d, (5, 1))  # Reshape 1D array to 5x1 array
print("\nReshaped Array (5x1):\n", reshaped_array)

# Creating a random array
random_array = np.random.rand(3, 3)  # Create a 3x3 array of random floats between 0 and 1
print("\nRandom 3x3 Array:\n", random_array)