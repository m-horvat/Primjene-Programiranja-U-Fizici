def derivacija(function,x,delta=0.01,O='three-step'):
    if O == 'two-step':
        deriv = (function(x+delta)-function(x))/delta
    else:
        deriv = (function(x+delta)-function(x-delta))/(2*delta)
    return deriv

def derivacija_raspon(function,xL,xH,delta=0.01):
    import numpy as np
    dots = np.linspace(xL,xH)
    deriv_dots = []
    for i in dots:
        deriv = derivacija(function,i,delta)
        deriv_dots.append(deriv)
    return dots,deriv_dots
    
# - - - - - - - - - - - - - - - - - - - - - - - - -

def integracija(function,xL,xH,N):
    import numpy as np
    dots = np.linspace(xL,xH,N)
    donj_med = 0
    gornj_med = 0
    for idx,i in enumerate(dots):
        if i == dots[-1]:
            break
        integ_dio = function(dots[idx])*(dots[idx+1]-i)
        if idx != 0:
            gornj_med += integ_dio
        if idx != N-1:
            donj_med += integ_dio
    return(donj_med, gornj_med)

def trapezna_integracija(function,xL,xH,N):
    import numpy as np
    dots = np.linspace(xL,xH,N)
    print(dots[-1], dots[0])
    integral = 0
    delta_x = (xH-xL)/N
    for idx,i in enumerate(dots):
        if i == dots[-1]:
            break
        integ_dio = function(dots[idx]) + function(dots[idx+1])
        integral += integ_dio
    integral *= (delta_x/2)
    return(integral)


