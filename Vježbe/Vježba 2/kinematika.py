import numpy as np
import matplotlib.pyplot as matplot

def jednoliko_gibanje(F,m,t1,t2,v0=0,s0=0):
    t = np.linspace(t1,t2)

    a = F*m
    v = v0 + a*t
    s = s0 + v*t

    at = matplot.figure(0)
    matplot.title('a-t graf')
    matplot.xlabel('t (s)')
    matplot.ylabel('a (m/s^2)')
    matplot.plot(t,np.linspace(a,a))

    vt = matplot.figure(1)
    matplot.title('v-t graf')
    matplot.xlabel('t (s)')
    matplot.ylabel('v (m/s)')
    matplot.plot(t,v)

    st = matplot.figure(2)
    matplot.title('s-t graf')
    matplot.xlabel('t (s)')
    matplot.ylabel('s (m)')
    matplot.plot(t,s)

    matplot.show()


def kosi_hitac(v0,theta,t1,t2,g=9.81):
    t = np.linspace(t1,t2)

    vx = np.cos(theta/180*np.pi)*v0
    x = vx*t

    vy = np.sin(theta/180*np.pi)*v0
    y = vy*t - 0.5*g*t**2

    xy = matplot.figure(0)
    matplot.title('x-y graf')
    matplot.xlabel('y (m)')
    matplot.ylabel('x (m)')
    matplot.plot(x,y)

    xt = matplot.figure(1)
    matplot.title('x-t graf')
    matplot.xlabel('t (s)')
    matplot.ylabel('x (m)')
    matplot.plot(t,x)

    yt = matplot.figure(2)
    matplot.title('y-t graf')
    matplot.xlabel('t (s)')
    matplot.ylabel('y (m)')
    matplot.plot(t,y)

    matplot.show()