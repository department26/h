import numpy as np

x = np.array([24,13,27,12,31,42,13,29,17,11])
y = np.array([24,25,21,25,22,19,24,20,25,26])

# Returns a correlation matrix
correlation_matrix = np.corrcoef(x, y)

# The coefficient is the value at index [0, 1]
correlation_xy= correlation_matrix[0, 1]

print(f"\nCorrelation Coefficient (r): {correlation_xy:.4f}\n")