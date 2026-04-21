import matplotlib.pyplot as  plt  
import numpy as np 

#data
x=np.array([1,2,3,4,5])
y=np.array([2,4,5,6,7])

#fit linw(degree 1 polynomial)
#polyfit(slope,intercept)
a,b=np.polyfit(x,y,1)

#print equation
print(f"Fitted line:y={a:.2f}x+{b:.2f}")

#scatter plot(dot lines)
plt.scatter(x,y,label="Data")
#plot fitted line
plt.plot(x,a*x+b,label="fitted line")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("fitted line:y=ax+b")
plt.legend() #info 
plt.show()