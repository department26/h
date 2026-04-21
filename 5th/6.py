import numpy as np

x = np.array([1,3,4,6,8,9,11,14])
y = np.array([1,2,4,4,5,7,8,9])

# Returns a correlation matrix
correlation_matrix = np.corrcoef(x, y)

# The coefficient is the value at index [0, 1]
correlation_xy= correlation_matrix[0, 1]

print(f"\nCorrelation Coefficient (r): {correlation_xy:.4f}\n")