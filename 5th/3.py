import numpy as np

x = np.array([2, 4, 5, 6, 8,11])
y = np.array([18, 12, 10, 8, 7,5])

# Returns a correlation matrix
correlation_matrix = np.corrcoef(x, y)

# The coefficient is the value at index [0, 1]
correlation_xy= correlation_matrix[0, 1]

print(f"\nCorrelation Coefficient (r): {correlation_xy:.4f}\n")