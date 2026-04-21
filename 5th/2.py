import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 5, 3, 8, 7])

# Returns a correlation matrix
correlation_matrix = np.corrcoef(x, y)

# The coefficient is the value at index [0, 1]
correlation_xy= correlation_matrix[0, 1]

print(f"\nCorrelation Coefficient (r): {correlation_xy:.4f}\n")