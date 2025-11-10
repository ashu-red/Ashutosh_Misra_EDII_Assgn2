import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0,1000,0.1)
b=1/100
a=30
scale=1e-7
F_r=scale*np.exp(t*b)*( (b**2 - a**2)*np.sin(a*t) + 2*a*b*np.cos(a*t))

fig, ax1 = plt.subplots(figsize=(11,6))
left, bottom, width, height = [0.25, 0.6, 0.2, 0.2]
ax2 = fig.add_axes([left, bottom, width, height])

ax2.plot(t,F_r,'b-',label="Zoomed")
ax1.plot(t,F_r,'b-',label="Radiation Reaction Force")


ax1.legend()
ax1.set_ylabel("F_r")
ax1.set_xlabel("t")
ax1.set_xlim(0,1000)
ax2.set_xlim(900,1000)
plt.show()
