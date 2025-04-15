import numpy as np
from scipy import integrate, optimize, stats

# Example 1: Numerical Integration

# Define a simple function to integrate
def f(x):
    return x**2

# Calculate the integral of f(x) from 0 to 1
integral_result, error = integrate.quad(f, 0, 1)
print(f"Integral of x^2 from 0 to 1: {integral_result:.4f} (error estimate: {error:.4g})")

# Example 2: Optimization

# Define a simple cost function to minimize
def cost_function(x):
    return (x - 2) ** 2

# Use SciPy's minimize function to find the value of x that minimizes the cost_function
result = optimize.minimize(cost_function, x0=0)  # x0 is the initial guess
print(f"Minimum value found at x = {result.x[0]:.4f} with a minimum cost of {result.fun:.4f}")

# Example 3: Interpolation

# Create some data points
x_data = np.array([0, 1, 2, 3, 4])
y_data = np.array([1, 2, 0, 2, 1])

# Perform linear interpolation
from scipy.interpolate import interp1d

# Create the interpolation function
interp_func = interp1d(x_data, y_data, kind='linear')

# Generate new x values for interpolation
x_new = np.linspace(0, 4, 100)
y_new = interp_func(x_new)

# Displaying some of the interpolated results
print("Interpolated values:")
print(y_new)