import numpy as np
import matplotlib.pyplot as plt
import math as m

def sgn(x):
    return np.sign(x) if x != 0 else 0

def akc(v,q,B,E,m):

    Ex, Ey, Ez = E[0], E[1], E[2]
    Bx, By, Bz = B[0], B[1], B[2]
    vx, vy, vz = v[0], v[1], v[2]

    ax = (q/m)*(Ex+vy*Bz-vz*By)
    ay = (q/m)*(Ey-(vx*Bz-vz*Bx))
    az = (q/m)*(Ez+vx*By-vz*By)
    return (ax,ay,az)

def explicit_step(s,v,dt,q,B,E,m):

    vx0, vy0, vz0 = v[0], v[1], v[2]
    x0, y0, z0 = s[0], s[1], s[2]

    ax0,ay0 = akc(vx0,vy0,q,B,E,m)
    vx = vx0+ax0*dt
    vy = vy0+ay0*dt
    vz = vz0+ay0*dt
    x = x0+vx0*dt
    y = y0+vx0*dt
    z = z0+vz0*dt
    return(x,y,z,vx,vy,vz)

def runge_kutta(s,v,q,B,E,m,dt):

    x1, y1, z1 = s[0], s[1], s[2]
    vx1, vy1, vz1 = v[0], v[1], v[2]

    k1x, k1y, k1z = akc(v,q,B,E,m)
    l1x = vx1
    l1y = vy1
    l1z = vz1

    vx2 = vx1 + 0.5*dt*k1x
    vy2 = vy1 + 0.5*dt*k1y
    vz2 = vz1 + 0.5*dt*k1z
    V2 = [vx2,vy2,vz2]
    k2x, k2y, k2z = akc(V2,q,B,E,m)
    l2x = vx1 + 0.5*dt*k2x
    l2y = vy1 + 0.5*dt*k2y
    l2z = vz1 + 0.5*dt*k2z

    vx3 = vx2 + 0.5*dt*k2x
    vy3 = vy2 + 0.5*dt*k2y
    vz3 = vz2 + 0.5*dt*k2z
    V3 = [vx3,vy3,vz3]
    k3x, k3y, k3z = akc(V3,q,B,E,m)
    l3x = vx2 + 0.5*dt*k3x
    l3y = vy2 + 0.5*dt*k3y
    l3z = vz2 + 0.5*dt*k3z

    vx4 = vx3 + dt*k3x
    vy4 = vy3 + dt*k3y
    vz4 = vz3 + dt*k3z
    V4 = [vx4,vy4,vz4]
    k4x, k4y, k4z = akc(V4,q,B,E,m)
    l4x = vx3 + dt*k4x
    l4y = vy3 + dt*k4y
    l4z = vz3 + dt*k4z
    
    vx = vx1 + (dt/6)*(k1x+2*k2x+2*k3x+k4x)
    vy = vy1 + (dt/6)*(k1y+2*k2y+2*k3y+k4y)
    vz = vz1 + (dt/6)*(k1z+2*k2z+2*k3z+k4z)

    x = x1 + (dt/6)*(l1x+2*l2x+2*l3x+l4x)
    y = y1 + (dt/6)*(l1y+2*l2y+2*l3y+l4y)
    z = z1 + (dt/6)*(l1z+2*l2z+2*l3z+l4z)

    return (x,y,z,vx,vy,vz)

x0 = 0
y0 = 0
z0 = 0

m = 10**-10
q = 10**-3
v0 = [1,0,0]
E =  [0,0,0]
B =  [0,1,0]

x_RK,    y_RK,    z_RK        = [x0],    [y0],    [z0]
x_expl,  y_expl,  z_expl      = [x0],    [y0],    [z0]
vx_expl, vy_expl, vz_expl     = [v0[0]], [v0[1]], [v0[2]]
vx_RK,   vy_RK,   vz_RK       = [v0[0]], [v0[1]], [v0[2]]

time = 0
dt = 0.01
t = np.range(0,time,dt)

for i in range(len(t)):
    s_list = [x_expl[-1],  y_expl[-1],  z_expl[-1] ]
    v_list = [vx_expl[-1], vy_expl[-1], vz_expl[-1]]
    X, Y, Z, VX, VY, VZ = explicit_step(s_list,v_list,dt,q,B,E,m)
    x_expl.append(X)
    y_expl.append(Y)
    z_expl.append(Z)
    vx_expl.append(VX)
    vy_expl.append(VY)
    vz_expl.append(VZ)

    s_list = [x_RK[-1],  y_RK[-1],  z_RK[-1] ]
    v_list = [vx_RK[-1], vy_RK[-1], vz_RK[-1]]
    X, Y, Z, VX, VY, VZ = runge_kutta(s_list,v_list,q,B,E,m,dt)
    x_RK.append(X)
    y_RK.append(Y)
    z_RK.append(Z)
    vx_RK.append(VX)
    vy_RK.append(VY)
    vy_RK.append(VZ)

plt.style('mpl-gallery')
fig, ax = plt.subplots(subplot_kw=('projection': '3d'))
ax.plot(x_expl,y_expl,z_expl,'r')

plt.figure(figsize=(10,8))
plt.plot(x_expl,y_expl,z_expl,'r')
plt.plot(x_RK,y_RK,z_RK,'g')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.show()