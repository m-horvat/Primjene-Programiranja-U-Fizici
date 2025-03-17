import numpy as np

# this all feels wrong, idk
# i'll redo this sometime later :\

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
phi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]

# M = Dt*phi --> y = ax
y = M
x = phi

Nx = []
Ny = []
x2 = 0
xy = 0

for i in x:
    Nx.append(i-np.mean(x))
for j in y:
    Ny.append(j-np.mean(y))

for idx,i in enumerate(Nx):
    x2 += i*i
    for idy,j in enumerate(Ny):
        if idx == idy:
            xy += i*j

a = xy/x2
b = np.mean(y)-a*np.mean(x)

print(a,b)

import matplotlib.pyplot as matplot

X = np.linspace(0,1)
Y = a*X+b

matplot.plot(X,Y)
matplot.show()





        



