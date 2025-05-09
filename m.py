import numpy as np
import matplotlib.pyplot as plt
import math as m

def sgn(x):
    return np.sign(x) if x != 0 else 0

def akc(vx,vy,D,m,g=9.81):
    ax = -(D/m)*vx**2*sign(vx)
    ay = -g-(D/m)*vy**2*sign(vy)
    return (ax,ay)

def explicit_step(x0,y0,vx0,vy0,dt,D,m,g=9.81):
    ax0,ay0 = akc(vx0,vy0,D,m)
    vx = vx0+ax0*dt
    vy = vy0+ay0*dt
    x = x0+vx0*dt
    y = y0+vx0*dt
    return(x,y,vx,vy)

def runge_kutta(x1,y1,vx1,vy1,dt,D,m,g=9.81):
    k1x, k1y = akc(vx1,vy1,D,m,g)
    l1x = vx1
    l1y = vy1

    vx2 = vx1 + 0.5*dt*k1x
    vy2 = vy1 + 0.5*dt*k1y
    k2x, k2y = akc(vx2,vy2,D,m,g)
    l2x = vx1 + 0.5*dt*k2x
    l2y = vx1 + 0.5*dt*k2y

    vx3 = vx2 + 0.5*dt*k2x
    vy3 = vy2 + 0.5*dt*k2y
    k3x, k3y = akc(vx3,vy3,D,m,g)
    l3x = vx2 + 0.5*dt*k3x
    l3y = vx2 + 0.5*dt*k3y

    vx4 = vx3 + dt*k3x
    vy4 = vy3 + dt*k3y
    k4x, k4y = akc(vx4,vy4,D,m,g)
    l4x = vx3 + dt*k4x
    l4y = vx3 + dt*k4y
    
    vx = vx1 + (dt/6)*(k1x+2*k2x+2*k3x+k4x)
    vy = vy1 + (dt/6)*(k1y+2*k2y+2*k3y+k4y)

    x = x1 + (dt/6)*(l1x+2*l2x+2*l3x+l4x)
    y = y1 + (dt/6)*(l1y+2*l2y+2*l3y+l4y)

    return (x,y,vx,vy)

x0 = 0
y0 = 0

theta = 30
v0 = 5
v0x = v0*np.cos(np.radians(theta))
v0y = v0*np.sin(np.radians(theta))

ro = 2.34
A = 0.015
C = 1.05
D = ro*A*C/2

m = 2
dt = 0.02

x_expl = [x0]
y_expl = [y0]
vx_expl = [v0x]
vy_expl = [v0y]
x_RK = [x0]
y_RK = [y0]
vx_RK = [v0x]
vy_RK = [v0y]
t = 0

while y_expl[-1] >= 0 or vy_expl[-1] >= 0:
    X, Y, VX, VY = explicit_step(x_expl[-1],y_expl[-1],vx_expl[-1],vy_expl[-1])
    x_expl.append(X)
    y_expl.append(Y)
    vx_expl.append(VX)
    vy_expl.append(VY)

    X, Y, VX, VY = runge_kutta(x_RK[-1],y_RK[-1],vx_RK[-1],vy_RK[-1])
    x_RK.append(X)
    y_RK.append(Y)
    vx_RK.append(VX)
    vy_RK.append(VY)
    t+=dt

plt.figure(figsize=(10,8))
plt.plot(x_expl,y_expl,'r')
plt.plot(x_RK,y_RK,'g')
plt.xlabel('Udaljenost [s]')
plt.ylabel('Visina [m]')
plt.show()