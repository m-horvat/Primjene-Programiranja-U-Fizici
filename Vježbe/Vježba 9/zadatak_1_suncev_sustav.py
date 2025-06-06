import matplotlib.pyplot as matplot
import numpy as np

def step(s1,m1,v1,s2,m2,v2,dt,G=6.67408*10**-11):

    s = s2-s1
    d = np.sqrt(s[0]**2+s[1]**2)
    
    a  =  G*m1*m2/d**2*(s/d)

    # Pomak Sunca

    a1 =  a/m1
    v_n1 = v1 + a1*dt
    s_n1 = s1 + v_n1*dt

    # Pomak Zemlje
    
    a2 = -a/m2
    v_n2 = v2 + a2*dt
    s_n2 = s2 + v_n2*dt

    return (s_n1,s_n2,v_n1,v_n2)

# Sunce:
m1 = 1.989 * 10**30
s1 = np.array([0 , 0])
v1 = np.array([0 , 0])

# Zemlja:
m2 = 5.9742 * 10**24
s2 = np.array([1.486 * 10**11 , 0])
v2 = np.array([0, 29783])

# 86400 = 1 dan, 365 = 1 godina
dt = 86400
t = [x for x in range(0,365)]
m1_path_x, m1_path_y, m2_path_x, m2_path_y = [],[],[],[]

for i in t:
    m1_path_x.append(s1[0])
    m1_path_y.append(s1[1])
    m2_path_x.append(s2[0])
    m2_path_y.append(s2[1])

    s1, s2, v1, v2= step(s1,m1,v1,s2,m2,v2,dt)

matplot.plot(m1_path_x, m1_path_y, 'y.', label = 'Sunce' )
matplot.plot(m2_path_x, m2_path_y, 'b', label = 'Zemlja')
matplot.axis('equal')
matplot.xlabel('x[m]')
matplot.ylabel('y[m]')
matplot.legend()
matplot.show()