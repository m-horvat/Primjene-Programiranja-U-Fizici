import calculus as calc
import matplotlib.pyplot as matplot
import numpy as np

def f_quad(x):
    y=2*x**2+3
    return y

# Raspon točaka od A do B
a = -2
b = 5
Nd = 100
Nu = 200
N = [x for x in range(Nd,Nu)]

reg_integ_list_g = []
reg_integ_list_d = []
trap_integ_list = []

for i in N:
    x = calc.integracija(f_quad,a,b,i)
    reg_integ_list_d.append(x[0])
    reg_integ_list_g.append(x[1])
    trap_integ_list.append(calc.trapezna_integracija(f_quad,a,b,i))

# - - - - - - - - - - - - - -
# Stvaranje analitičkog rješenja

def F_quad(x):
    return 2/3*x**3+3*x

analytical_solution = F_quad(b)-F_quad(a)

# - - - - - - - - - - - - - -

fig, axes = matplot.subplots(nrows=1, ncols=2)

axes[0].plot(N,reg_integ_list_d,'ro',markersize=1,label='Donja granica integracije')
axes[0].plot(N,reg_integ_list_g,'bo',markersize=1,label='Gornja granica integracije')
axes[0].axhline(analytical_solution,color='#BBBBBB',linestyle='dotted')
axes[1].plot(N,trap_integ_list,'ro',markersize=1,label='Trapezna integracija')
axes[1].axhline(analytical_solution,color='#BBBBBB',linestyle='dotted')
matplot.legend()
matplot.show()