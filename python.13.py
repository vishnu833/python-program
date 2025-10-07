import math
import matplotlib.pyplot as plt
x_values=[]
y_values=[]
steps=100
for i in range(steps+1):
    x=(2*math.pi)*i/steps
    y=math.sin(x)
    x_values.append(x)
    y_values.append(y)
plt.plot(x_values,y_values)
plt.xlabel('X')
plt.ylabel('sin(X)')
plt.title('Sine Wave')
plt.grid(True)
plt.show()
