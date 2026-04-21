import matplotlib.pyplot as plt 
import numpy as np

x=np.linspace(0,15)
y=-x
plt.plot(x,y,label="y=-x",color="grey")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.title("Graph Of the function y=-x")
plt.show()