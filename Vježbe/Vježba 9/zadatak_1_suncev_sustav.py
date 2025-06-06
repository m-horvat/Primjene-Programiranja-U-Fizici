import matplotlib.pyplot as matplot
import numpy as np
import math as math

def step(m1,s1,v1,m2,s2,v2,dt,theta,phi,G=6.67408*10**-11):

    s1x, s1y, s2x, s2y = s1[0],s1[1],s2[0],s2[1]
    s1u = np.sqrt(s1x**2+s1y**2)
    s2u = np.sqrt(s2x**2+s2y**2)

    # Pomak Sunca
    a_n1 = -G * (m2/(abs(s1u-s2u))**3)*(s1u-s2u)

    v_n1x = v1*np.sin(theta) + a_n1*dt*np.cos(theta)
    s_n1x = s1x + v_n1x*dt
    v_n1y = v1*np.cos(theta) + a_n1*dt*np.sin(theta)
    s_n1y = s1y + v_n1y*dt


    # Pomak Zemlje
    a_n2 = -G * (m1/(abs(s2u-s1u))**3)*(s2u-s1u)
    
    v_n2x = v2*np.cos(theta+phi) + a_n2*dt*np.cos(theta)
    s_n2x = s2x + v_n2x*dt
    v_n2y = v2*np.sin(theta+phi) + a_n2*dt*np.sin(theta)
    s_n2y = s2y + v_n2y*dt

    print(v_n2x, v_n2y)

    v_n1 = np.sqrt(v_n1x**2+v_n1y**2)
    v_n2 = np.sqrt(v_n2x**2+v_n2y**2)
    s_n1 = [s_n1x, s_n1y]
    s_n2 = [s_n2x, s_n2y]

    return (s_n1, s_n2)

# Sunce:
m1 = 1.989 * 10**30
s1 = [0 , 0]
v1 = 0

# Zemlja:
m2 = 5.9742 * 10**24
s2 = [1.486 * 10**11 , 0]

phi = 90

dt = 12000
t = [x for x in range(0,1000)]

m1_path_x, m1_path_y, m2_path_x, m2_path_y = [],[],[],[]

v1_list, v2_list = [],[]

for i in t:
    v2 = 29783
    m1_path_x.append(s1[0])
    m1_path_y.append(s1[1])
    m2_path_x.append(s2[0])
    m2_path_y.append(s2[1])

    # debugging
    v1_list.append(v1)
    v2_list.append(v2)

    diag = np.sqrt((s2[1]-s1[1])**2+(s2[0]-s1[0])**2)

    if s2[0]-s1[0] != 0: theta = math.degrees(np.arcsin((s2[0]-s1[0])/diag))
    else: theta = 90
    print(theta)

    s1, s2 = step(m1,s1,v1,m2,s2,v2,dt,theta,phi)



matplot.plot(m1_path_x, m1_path_y, 'y.', label = 'sunce' )
matplot.plot(m2_path_x, m2_path_y, 'b', label = 'zemlja')
# matplot.plot(t, m2_path_y, 'b', label = 'zemlja')
matplot.legend
matplot.show()


    