import particle as Part
import numpy as np
import matplotlib.pyplot as matplot

# Analitičko rješavanje zadatka
v0 = 10
theta = 60
x0 = 0
y0 = 0
g = -9.81
dt = 0.001
t = 0
y = y0

x_final = []
y_final = []

vx = np.cos(theta/180*np.pi)*v0
vy = np.sin(theta/180*np.pi)*v0

loop = True
while loop == True:
    x = x0+vx*t
    y = y0+vy*t+0.5*g*t**2
    if y < 0:
        break
    t += dt
    x_final.append(x)
    y_final.append(y)

# Numeričko rješavanje zadatka

p1 = Part.Particle(v0,theta,x0,y0)
numerical_calc = p1.range(dt)

Error = []
t = 0
t_graph = []

print([abs(x-y)/x*100 for x,y in zip(y_final,numerical_calc[1])])

d_analit = []
d_numerit = []

for i_idx, x in enumerate(x_final):
    for j_idx, y in enumerate(y_final):
        if i_idx == j_idx:
            d_analit.append(np.sqrt(x**2+y**2))

print(d_analit)

for i_idx, x in enumerate(numerical_calc[0]):
    for j_idx, y in enumerate(numerical_calc[1]):
        if i_idx == j_idx:
            d_numerit.append(np.sqrt(x**2+y**2))

for i_idx, analit in enumerate(d_analit):
    for j_idx, numerit in enumerate(d_numerit):
        if i_idx == j_idx and i_idx < 10000:
            Error.append((abs(analit-numerit)/analit)*100)
            # print((numerit-analit),analit,numerit)
            t_graph.append(t+dt*i_idx)

matplot.plot(t_graph,Error)
matplot.show()