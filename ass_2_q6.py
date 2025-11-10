import numpy as np
import matplotlib.pyplot as plt


nu=np.arange(0,10,0.1)
T=3
dP_dw=np.exp(-nu/T)*(0.6*nu**2/T**2 + 1.6 + 2.2*nu/T)*T**(-1/2)

fig, ax1 = plt.subplots(2,1,figsize=(6,6))

ax1[0].plot(nu,dP_dw,'b-',label="T=small")

T=100
dP_dw=np.exp(-nu/T)*(0.6*nu**2/T**2 + 1.6 + 2.2*nu/T)*T**(-1/2)


ax1[0].set_title("Power Emitted per unit frequency")
ax1[1].plot(nu,dP_dw,'b-',label="T=large")
ax1[0].legend()
ax1[1].legend()
ax1[1].set_ylabel("dP_dw")
ax1[1].set_xlabel("nu")
ax1[1].set_xlim(0,10)
plt.show()
