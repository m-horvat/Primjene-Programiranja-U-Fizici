import calculus as calc
import matplotlib.pyplot as matplot
import numpy as np

def f_quad(x):
    y=2*x**2+3
    return y

# Raspon točaka od A do B
a = -2
b = 2
N = 500
T = np.linspace(a,b)

reg_integ = (calc.integracija(f_quad,a,b,N))
trapez_integ =(calc.trapezna_integracija(f_quad,a,b,N))

fig, axes = matplot.subplots(nrows=1, ncols=2)

axes[0].plot(N,reg_integ[1],'ro',markersize=1)
axes[1].plot(N,trapez_integ[1],'ro',markersize=1)
matplot.show()