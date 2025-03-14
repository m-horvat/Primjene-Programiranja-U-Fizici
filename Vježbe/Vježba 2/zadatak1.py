import matplotlib.pyplot as matplot
import numpy as np

F = 2     # N
m = 5     # kg
t = np.linspace(0,10)
v0 = 0
s0 = 0

a = F*m
v = v0 + a*t
s = s0 + v*t

# i forgot everything about matplot,
# but i know that theres a better way of doing this, 
# so this will probably change :)

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