import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 4, 5, 6, 7])

# Fit: log(y) = b*log(x) + log(a)
b, log_a = np.polyfit(np.log(x), np.log(y), 1)
a = np.exp(log_a)

# Plot
plt.scatter(x, y)
plt.plot(x, a * x**b, color='red')
plt.title(f"Power Fit: y = {a:.2f} * x^{b:.2f}")
plt.show()