import numpy as np
import matplotlib.pyplot as matplot

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
phi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]

# M = Dt*phi --> y = ax || y = M || x = phi ||

Nx = []
Ny = []
x2 = 0
xy = 0

for i in phi:
    Nx.append(i-np.mean(phi))
for j in M:
    Ny.append(j-np.mean(M))

for idx,i in enumerate(Nx):
    x2 += i*i
    for idy,j in enumerate(Ny):
        if idx == idy:
            xy += i*j

a = xy/x2
b = np.mean(M)-a*np.mean(phi)

X = np.linspace(phi[0],phi[-1])
Y = a*X+b

fig, ax = matplot.subplots()

ax.grid(visible=None, linestyle='dotted', which='major', axis='both')
ax.plot(X,Y,label='$D_t$')
ax.plot(phi,M,'r.',label='Data points')
ax.set_title(r'Graf linearne regresije modula torzije $D_t = \frac{M}{\phi}$')
ax.set_ylabel('M(Nm)')
ax.set_xlabel(r'$\phi$(rad)')
ax.legend()

matplot.show()
