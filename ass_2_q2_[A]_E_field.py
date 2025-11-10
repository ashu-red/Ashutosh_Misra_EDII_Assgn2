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
v_dot=0.3 #in z-direction
arrow_length=5
vx=vel
dt=0.005
timesteps=100

print("\n Time= 0 to ",dt*timesteps) 

print("\nInitial Position taken as x0=",x0)

save_path="./E_field_lines_vx={vel:.2f} for vdot =0.3 z.mp4".format(vel=vx)
print("\n A MP4 file will be saved in the current folder, save path and title= ", save_path)



t1=0.001

vz=v_dot*t1
v=vx**2 + vz**2
gamma=1/(1-v**2)
xb=(x-vx*t1-x0)
zb=(z-vz*t1)
k=((gamma*zb)**2 + y**2 + (gamma*xb)**2)**(1/2)
R=gamma**2*(vx*xb + vz*zb) + gamma*k
#Radiation Electric Field per unit charge times c, in Ei(ct,x,y,z) axes
Ex = gamma**3 * (v_dot*xb*zb + v_dot*xb*vz*R)/k**3
Ey = gamma**3 * (v_dot*y*zb + v_dot*y*vz*R)/k**3
Ez= -gamma**3 * (v_dot*xb**2 + v_dot*y**2 + v_dot*xb*R)/k**3

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
    vz=v_dot*ct
    v=vx**2 + vz**2
    gamma=1/(1-v**2)
    xb=(x-vx*ct-x0)
    zb=(z-vz*ct)
    k=((gamma*zb)**2 + y**2 + (gamma*xb)**2)**(1/2)
    R=gamma**2*(vx*xb + vz*zb) + gamma*k
    #Radiation Electric Field per unit charge times c, in Ei(ct,x,y,z) axes
    Ex = gamma**3 * (v_dot*xb*zb + v_dot*xb*vz*R)/k**3
    Ey = gamma**3 * (v_dot*y*zb + v_dot*y*vz*R)/k**3
    Ez= -gamma**3 * (v_dot*xb**2 + v_dot*y**2 + v_dot*xb*R)/k**3
    # Plotting Vector Field with QUIVER
    ax1.clear()
    ax1.set_title('Radiation Electric Field  for vdot =0.3 z for v={vel:.2f}c'.format(vel=vx))
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

