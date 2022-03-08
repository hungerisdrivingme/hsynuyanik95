from turtle import color
import matplotlib.pyplot as plt
import numpy as np

"""
x=[1,2,3,4]
y=[1,4,9,16]
# plt.plot(x,y,color="red",linewidth="5")
plt.plot(x,y,"o-r")
plt.axis([0,6,0,20])
plt.title("Grafik")
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")
plt.show()
"""
"""
x=np.linspace(0,2,100)
plt.plot(x,x, label="linear",color="red")
plt.plot(x,x**2, label="quadratic")
plt.plot(x,x**3, label="cubic")

plt.xlabel("xlabel")
plt.ylabel("ylabel")

plt.title("Grafik")

plt.legend()
plt.show()
"""

"""
x=np.linspace(0,2,100)
fig,axs=plt.subplots(3)
axs[0].plot(x,x,color="red")
axs[0].set_title("linear")

axs[1].plot(x,x**2,color="yellow")
axs[1].set_title("quadratic")

axs[2].plot(x,x**3,color="black")
axs[2].set_title("qubic")

plt.tight_layout()
plt.show()
"""

"""
x=np.linspace(0,2,100)
fig,axs=plt.subplots(2,2)
axs[0,0].plot(x,x,color="red")
axs[0,1].plot(x,x**2,color="blue")
axs[1,0].plot(x,x**3,color="green")
axs[1,1].plot(x,x**4,color="gray")


plt.show()
"""