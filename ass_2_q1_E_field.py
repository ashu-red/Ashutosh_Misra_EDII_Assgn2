import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Meshgrid
xy_max=5
x, y , z= np.meshgrid(np.linspace(-xy_max, xy_max, 10), 
                   np.linspace(-xy_max, xy_max, 10),np.linspace(-xy_max, xy_max, 10))

vel = float(input('Enter v/c (0<v/c<1):'))
tf = 2*xy_max/vel #float(input('Enter final time:'))


print("\n Time= 0 to ",tf) 

x0=-xy_max
ct=np.linspace(0,tf,20)
v=vel
arrow_length=1

print("\nInitial Position taken as x0=",x0)

save_path="./pE_field_lines_v={vel:.2f}.gif".format(vel=v)
save_path1="./pE_lines_x0=0_v={vel:.2f}.png".format(vel=v)

print("\n A MP4 file will be saved in the current folder, save path and title= ", save_path)

print("\n A plot for E_field lines at x0=0 will also be saved, save path and title=", save_path1)


gamma=1/(1-v**2)


xb=(x-v*ct[10])
Ex = xb*gamma/(z**2 + y**2 + (gamma*xb)**2)**(3/2)
Ey = y*gamma/(z**2 + y**2 + (gamma*xb)**2)**(3/2)
Ez=  z*gamma/(z**2 + y**2 + (gamma*xb)**2)**(3/2)

fig=plt.figure(figsize=(10,10),layout='tight')
ax=fig.add_subplot(projection='3d')
ax.set_title('Electric Field for v={vel:.2f}c'.format(vel=v))
ax.set_xlim(-xy_max, xy_max)
ax.set_ylim(-xy_max, xy_max)
ax.set_zlim(-xy_max, xy_max)
ax.set_xticks(np.linspace(-xy_max,xy_max,3))
ax.set_yticks(np.linspace(-xy_max,xy_max,3))
ax.set_zticks(np.linspace(-xy_max,xy_max,3))
ax.set_ylabel("y")
ax.set_xlabel("x")
ax.set_zlabel("z")
ax.grid()
ax.quiver(x, y, z, Ex, Ey, Ez, color='r',length=arrow_length,linewidths=2)
fig.savefig(save_path1)


xb=(x-v*ct[0]-x0)
Ex = xb*gamma/(z**2 + y**2 + (gamma*xb)**2)**(3/2)
Ey = y*gamma/(z**2 + y**2 + (gamma*xb)**2)**(3/2)
Ez=  z*gamma/(z**2 + y**2 + (gamma*xb)**2)**(3/2)

fig1 = plt.figure(figsize=(10,10),layout='tight')
ax1 = fig1.add_subplot(projection='3d')
ll=ax1.quiver(x, y, z, Ex, Ey, Ez, color='r',length=arrow_length)
type(ll)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

def init():
    ax1.set_xlim(-xy_max,xy_max)
    ax1.set_ylim(-xy_max,xy_max)
    ax1.set_zlim(-xy_max,xy_max)

def update(i):
    xb=(x-v*ct[i]-x0)
    #Electric Field per unit charge in Ei(ct,x,y,z) axes
    Ex = xb*gamma/(z**2 + y**2 + (gamma*xb)**2)**(3/2)
    Ey = y*gamma/(z**2 + y**2 + (gamma*xb)**2)**(3/2)
    Ez=  z*gamma/(z**2 + y**2 + (gamma*xb)**2)**(3/2)
    print(i,"hehe\n")
    # Plotting Vector Field with QUIVER
    ax1.clear()
    ax1.set_title('Electric Field for v={vel:.2f}c'.format(vel=v))
    ax1.set_xlim(-xy_max, xy_max)
    ax1.set_ylim(-xy_max, xy_max)
    ax1.set_zlim(-xy_max, xy_max)
    ax1.set_xticks(np.linspace(-xy_max,xy_max,3))
    ax1.set_yticks(np.linspace(-xy_max,xy_max,3))
    ax1.set_zticks(np.linspace(-xy_max,xy_max,3))
    ax1.set_ylabel("y")
    ax1.set_xlabel("x")
    ax1.set_zlabel("z")
    ax1.grid()
    ax1.quiver(x, y, z, Ex, Ey, Ez, color='r',length=arrow_length,linewidths=2)



ani = animation.FuncAnimation(fig1, update, frames=len(ct),init_func=init, repeat=True)
ani.save(save_path, writer=writer)

