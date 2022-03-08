import matplotlib.pyplot as plt
import numpy as np
"""
x= np.linspace(-10,9,20)
y= x**3
z=x**2

figure=plt.figure()
axes=figure.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y,"b")
axes.set_xlabel("X axis")
axes.set_ylabel("Y axis")
"""
"""
x= np.linspace(-10,9,20)
y= x**3
z= x**2
figure=plt.figure()
axes=figure.add_axes([0,0,1,1])
axes.plot(x,z,label="Square")
axes.plot(x,y,label="cube")
axes.legend()
plt.show()
"""
"""
x= np.linspace(-10,9,20)
y= x**3
z= x**2

fig,axes=plt.subplots(2,1,figsize=(8,8))
axes[0].plot(x,y)
axes[0].set_title("Cube")

axes[1].plot(x,z)
axes[1].set_title("Square")

plt.tight_layout()
fig.savefig("figure1.png")
plt.show()
"""