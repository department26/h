import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,15)
y=np.cos(x)  
plt.plot(x,y,label="y=cos(x)",color="grey")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Graph of the function y=cos(x)")
plt.grid(True)
plt.show()
