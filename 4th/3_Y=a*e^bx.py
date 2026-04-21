import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2.5, 7.1, 19.8, 55.2, 150.4])

# 1. Fit: ln(y) = bx + ln(a)
b, log_a = np.polyfit(x, np.log(y), 1)
a = np.exp(log_a)

# 2. Plot
plt.scatter(x, y)
plt.plot(x, a * np.exp(b * x), color='red')
plt.title(f"Fit: $y = {a:.2f} \cdot e^{{{b:.2f}x}}$")
plt.show()