import matplotlib.pyplot as matplot
import numpy as np

F = 2
m = 5
a = []

dt = 0.01
t = 10
total_time = np.arange(0,t+1,dt)

v0 = 0
s0 = 0
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