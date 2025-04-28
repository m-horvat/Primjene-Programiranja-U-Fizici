class HarmonicOscillator:
    def __init__(self,m,k,t,x0=5,v0=0,dt=0.01):
        self.constant = k
        self.time = t
        self.deltat = dt
        self.mass = m
        self.startingpoint = x0
        self.startingspeed = v0

    def __move(self,x0,v0):
        a = -(self.constant*x0)/self.mass
        v = v0 + a*self.deltat
        x = x0 + v*self.deltat

        return(x,v,a)
    
    def long_movement(self):
        x0 = self.startingpoint
        v0 = self.startingspeed
        a_list = []
        v_list = []
        x_list = []
        cycles = self.time/self.deltat
        for idx in range(0,int(cycles)):
            movement = self.__move(x0,v0)
            x_list.append(movement[0])
            v_list.append(movement[1])
            a_list.append(movement[2])
            x0 = x_list[idx]
            v0 = v_list[idx]
        return(x_list,v_list,a_list)
    
    def plotting(self,t,dt):
        import matplotlib.pyplot as matplot
        import numpy as np

        time = np.linspace(0,t,int(t/dt))

        lists = test.long_movement()
        matplot.plot(time,lists[0],label='at')
        matplot.plot(time,lists[1],label='vt')
        matplot.plot(time,lists[2],label='xt')
        matplot.legend()
        matplot.show()


m = 1
k = 10
t = 7
x0 = 2
dt = 0.001

test = HarmonicOscillator(m,k,t,x0,0,dt)
test.plotting(t,dt)









