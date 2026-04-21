import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 7.9, 18.2, 32.5, 51.1])

# Fit degree 2: returns [a, b, c] for ax^2 + bx + c
a, b, c = np.polyfit(x, y, 2)

# Generate smooth line for the curve
x_smooth = np.linspace(x.min(), x.max(), 100)
y_fit = a*x_smooth**2 + b*x_smooth + c

# Plot
plt.scatter(x, y, label="Data")
plt.plot(x_smooth, y_fit, color='red', label="Quadratic Fit")
plt.title(f"Fit: {a:.2f}x² + {b:.2f}x + {c:.2f}")
plt.legend()
plt.show()