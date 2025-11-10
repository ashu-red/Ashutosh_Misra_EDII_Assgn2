import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Meshgrid
xy_max=5
x, y , z= np.meshgrid(np.linspace(-xy_max, xy_max, 10), 
                   np.linspace(-xy_max, xy_max, 10),np.linspace(-xy_max, xy_max, 10))

vel = float(input('Enter vx/c (0<v/c<1):'))



x0=-xy_max
#ct=np.linspace(0,tf,40)
v_dot=0.9 #in x-direction
arrow_length=0.01
v0x=vel
dt=0.00001
timesteps=100

print("\n Time= 0 to ",dt*timesteps) 

print("\nInitial Position taken as x0=",x0)

save_path="./E_field_lines_vx={vel:.2f} for vdot =0.9 x.mp4".format(vel=v0x)
print("\n A MP4 file will be saved in the current folder, save path and title= ", save_path)



t1=0.0001

vx=v0x + v_dot*t1
v=vx**2
gamma=1/(1-v**2)
xb=(x-vx*t1-x0)
k=(z**2 + y**2 + (gamma*xb)**2)**(1/2)
R=gamma**2*(vx*xb) + gamma*k
#Radiation Electric Field per unit charge times c, in Ei(ct,x,y,z) axes
Ex = gamma**3 * (v_dot*(z**2 - y**2))/k**3
Ey = gamma**3 * (v_dot*(xb*y + y*vx*R))/k**3
Ez= -gamma**3 * (v_dot*(xb*z + z*vx*R))/k**3

fig1 = plt.figure()
ax1 = fig1.add_subplot(projection='3d')
ll=ax1.quiver(x, y, z, Ex, Ey, Ez, color='r',length=arrow_length)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

def init():
    ax1.set_xlim(-xy_max,xy_max)
    ax1.set_ylim(-xy_max,xy_max)
    ax1.set_zlim(-xy_max,xy_max)

def update(i):
    ct=dt*i
    vx=v0x + v_dot*ct
    v=vx**2
    gamma=1/(1-v**2)
    xb=(x-vx*ct-x0)
    k=(z**2 + y**2 + (gamma*xb)**2)**(1/2)
    R=gamma**2*(vx*xb) + gamma*k
    #Radiation Electric Field per unit charge times c, in Ei(ct,x,y,z) axes
    Ex = gamma**3 * (v_dot*(z**2 - y**2))/k**3
    Ey = gamma**3 * (v_dot*(xb*y + y*vx*R))/k**3
    Ez= -gamma**3 * (v_dot*(xb*z + z*vx*R))/k**3
    # Plotting Vector Field with QUIVER
    ax1.clear()
    ax1.set_title('Radiation Electric Field for v={vel:.2f}c for vdot =0.9 x'.format(vel=v0x))
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
    ax1.quiver(x, y, z, Ex, Ey, Ez, color='r',length=arrow_length)



ani = animation.FuncAnimation(fig1, update, frames=timesteps,init_func=init, repeat=True)
ani.save(save_path, writer=writer)

