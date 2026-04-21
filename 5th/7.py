import numpy as np

x = np.array([5,7,8,10,11,13,16])
y = np.array([33,30,28,20,18,16,9])

# Returns a correlation matrix
correlation_matrix = np.corrcoef(x, y)

# The coefficient is the value at index [0, 1]
correlation_xy= correlation_matrix[0, 1]

print(f"\nCorrelation Coefficient (r): {correlation_xy:.4f}\n")