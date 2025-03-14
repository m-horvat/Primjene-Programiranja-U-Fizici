import matplotlib.pyplot as matplot
import numpy as np

v0 = 70       # m/s
theta = 30   # stupnjeva
t = np.linspace(0,10)
g = 9.81     # m/s^2

vx = np.cos(theta/180*np.pi)*v0
x = vx*t

vy = np.sin(theta/180*np.pi)*v0
y = vy*t - 0.5*g*t**2

print(y)

# figure, axis = matplot.subplots(3)

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