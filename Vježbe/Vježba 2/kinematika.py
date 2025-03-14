def jednoliko_gibanje(F,m,v0,s0):
    a = F*m
    v = v0 + a*t
    s = s0 + v*t

def kosi_hitac(v0,t,theta,g=9.81):
    vx = np.cos(theta/180*np.pi)*v0
    x = vx*t

    vy = np.sin(theta/180*np.pi)*v0
    y = vy*t - 0.5*g*t**2