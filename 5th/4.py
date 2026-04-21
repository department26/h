import numpy as np

x = np.array([10,15,25,20,35,40,50,45,30])
y = np.array([7,8,3,5,9,7,19,15,17])

# Returns a correlation matrix
correlation_matrix = np.corrcoef(x, y)

# The coefficient is the value at index [0, 1]
correlation_xy= correlation_matrix[0, 1]

print(f"\nCorrelation Coefficient (r): {correlation_xy:.4f}\n")