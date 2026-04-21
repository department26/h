import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 5, 12, 30, 80])

# Fit linear line to log(y)
p = np.polyfit(x, np.log(y), 1)

# Extract a and b
a, b = np.exp(p[1]), np.exp(p[0])

# Plot
plt.scatter(x, y)
plt.plot(x, a * b**x, color='red')
plt.show()

print(f"y = {a:.2f} * {b:.2f}^x")