import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,15)
y=np.log(x)  
plt.plot(x,y,label="y=log(x)",color="grey")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Graph of the function y=log(x)")
plt.grid(True)
plt.show()
