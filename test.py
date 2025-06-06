import numpy as np
import matplotlib.pyplot as matplot

a = 10000000
t = 0
v = 1
pull = 5

listx = []
listy = []
angles = []

for i in range(0,100):
    v_x = v*np.cos(t) + pull*np.sin(t)
    v_y = v*np.sin(t) + pull*np.cos(t)
    a_x = a*np.cos(t)+v_x
    a_y = a*np.sin(t)+v_y
    listx.append(a_x)
    listy.append(a_y)
    angles.append(t)
    t=  np.degrees(np.arctan(a_y/a_x))

print(listx)
print(angles)

matplot.plot(listx,listy)
matplot.show()

print (np.degrees(np.arctan(-1)))