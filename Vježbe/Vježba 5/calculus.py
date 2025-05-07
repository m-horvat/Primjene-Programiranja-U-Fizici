def derivacija(function,x,delta=0.01,O='three-step'):
    if O == 'two-step':
        deriv = (function(x+delta)-function(x))/delta
    else:
        deriv = (function(x+delta)-function(x-delta))/(2*delta)
    return deriv

def derivacija_raspon(function,xL,xH,delta=0.01,O='three-step'):
    import numpy as np
    dots = np.linspace(xL,xH)
    deriv_dots = []
    for i in dots:
        deriv = derivacija(function,i,delta,O)
        deriv_dots.append(deriv)
    return dots,deriv_dots
    
# - - - - - - - - - - - - - - - - - - - - - - - - -

def integracija(function,xL,xH,N):
    import numpy as np
    dots = np.linspace(xL,xH,N)
    donj_med = 0
    gornj_med = 0
    diff = dots[2]-dots[1]
    for idx,i in enumerate(dots):
        integ_dio = function(dots[idx])*diff
        if idx != 0:
            gornj_med += integ_dio
        if idx != N-1:
            donj_med += integ_dio
    return(donj_med, gornj_med)

def trapezna_integracija(function,xL,xH,N):
    import numpy as np
    dots = np.linspace(xL,xH,N)
    integral = 0
    delta_x = (xH-xL)/N
    for idx,i in enumerate(dots):
        if i == dots[-1]:
            break
        integ_dio = function(dots[idx]) + function(dots[idx+1])
        integral += integ_dio
    integral *= (delta_x/2)
    return(integral)


