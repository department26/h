import numpy as np

x = np.array([6, 2, 10, 4, 8])
y = np.array([9, 11, 5, 8, 7])

# Returns a correlation matrix
correlation_matrix = np.corrcoef(x, y)

# The coefficient is the value at index [0, 1]
correlation_xy= correlation_matrix[0, 1]

print(f"\nCorrelation Coefficient (r): {correlation_xy:.4f}\n")