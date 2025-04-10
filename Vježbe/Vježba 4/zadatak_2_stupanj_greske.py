import particle as Part
import numpy as np
import matplotlib.pyplot as matplot

v0 = 10
theta = 60
x0 = 0
y0 = 0
g = -9.81

t_graph = [t/100 for t in range(0,1000)]
t_graph.remove(0)

vy = v0*np.sin(theta/180*np.pi)
vx = v0*np.sin(theta/180*np.pi)

p1 = Part.Particle(v0,theta,x0,y0)

analytic = []
all_approx = []
Error = []
Analyte = []

#for deltat in t_graph:
#    x = x0+vx*deltat
#    y = y0+vy*deltat+0.5*g*deltat**2
#    analytic.append(np.sqrt(x**2+y**2))

for deltat in t_graph:
    print(deltat)
    analit = y0+vy*deltat+0.5*g*deltat**2
    z = p1.range(deltat)
    if z[1][1] > 0:
        all_approx.append(z[1][1])
        Analyte.append(analit)

for j_idx, numerit in enumerate(all_approx):
    for i_idx, analit in enumerate(Analyte):
        if i_idx == j_idx:
            Error.append((abs(analit-numerit)/analit)*100)

x = 88
t_graph = t_graph[0:x]
Error = Error[0:x]

print(all_approx)

matplot.plot(t_graph,Error)
matplot.show()