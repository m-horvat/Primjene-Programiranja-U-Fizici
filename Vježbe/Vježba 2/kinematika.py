import numpy as np
import matplotlib.pyplot as matplot

def jednoliko_gibanje(F,m,t0,t,v0=0,s0=0,dt=0.001):

    a = []
    total_time = np.arange(t0,t+1,dt)
    v = [v0]
    s = [s0]

    for i in range(len(total_time)):
        a.append(F/m)
        v.append(v[i] + a[i]*dt)
        s.append(s[i] + v[i+1]*dt)

    v.remove(v0)
    s.remove(s0)

    fig, axes = matplot.subplots(nrows=1, ncols=3)

    axes[0].plot(total_time,a,color='red')
    axes[0].set_title('a-t graf')
    axes[0].set_xlabel('t (s)')
    axes[0].set_ylabel('a (m/s^2)')

    axes[1].plot(total_time,v,color='green')
    axes[1].set_title('v-t graf')
    axes[1].set_xlabel('t (s)')
    axes[1].set_ylabel('v (m/s)')

    axes[2].plot(total_time,s,color='blue')
    axes[2].set_title('s-t graf')
    axes[2].set_xlabel('t (s)')
    axes[2].set_ylabel('s (m)')
    axes[2].axis([0, t, 0, s[-1]])

    matplot.show()


def kosi_hitac(v0,theta,t0,t,x0=0,y0=0,dt=0.001,g=-9.81):

    total_time = np.arange(t0,t,dt)

    x = [x0]
    y = [y0]

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