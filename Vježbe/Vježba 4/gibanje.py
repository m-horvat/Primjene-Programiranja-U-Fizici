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


matplot.plot(x_final,y_final,color='#004400',linestyle='dotted', label='Analitičko rješenje (pravo rješenje)')

# Numeričko rješavanje zadatka

p1 = Part.Particle(v0,theta,x0,y0)
p1.range(dt)
p1.plot_trajectory(dt,t)