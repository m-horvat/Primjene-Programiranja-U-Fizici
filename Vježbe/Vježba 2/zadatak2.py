import matplotlib.pyplot as matplot
import numpy as np

g = -9.81
theta = 30

t = 2
dt = 0.01
total_time = np.arange(0,t,dt)

x0 = 0
x = [x0]
y0 = 0
y = [y0]

v0 = 5
vx = np.cos(theta/180*np.pi)*v0
vy = np.sin(theta/180*np.pi)*v0
v = [vy]

for i in range(0,len(total_time)):

    x.append(x[i]+vx*dt)
    v.append(v[i]+g*dt)
    y.append(y[i]+v[i+1]*dt)

v.remove(vy)
x.remove(x0)
y.remove(y0)

fig, axes = matplot.subplots(nrows=1, ncols=3)

axes[0].plot(x,y,color='red')
axes[0].set_title('x-y graf')
axes[0].set_xlabel('x (m)')
axes[0].set_ylabel('y (m)')

axes[1].plot(total_time,x,color='green')
axes[1].set_title('x-t graf')
axes[1].set_xlabel('t (s)')
axes[1].set_ylabel('x (m)')

axes[2].plot(total_time,y,color='blue')
axes[2].set_title('y-t graf')
axes[2].set_xlabel('t (s)')
axes[2].set_ylabel('y (m)')

matplot.show()