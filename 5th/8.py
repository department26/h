import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9])
y = np.array([9,8,10,12,11,13,14,16,15])

# Returns a correlation matrix
correlation_matrix = np.corrcoef(x, y)

# The coefficient is the value at index [0, 1]
correlation_xy= correlation_matrix[0, 1]

print(f"\nCorrelation Coefficient (r): {correlation_xy:.4f}\n")