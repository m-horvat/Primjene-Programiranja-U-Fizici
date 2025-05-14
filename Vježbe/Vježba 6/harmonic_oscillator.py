class HarmonicOscillator:
    def __init__(self,m,k,t,x0=5,v0=0,dt=0.01):
        self.constant = k
        self.time = t
        self.deltat = dt
        self.mass = m
        self.startingpoint = x0
        self.startingspeed = v0

    def __move(self,x0,v0,dt):
        a = -(self.constant*x0)/self.mass
        v = v0 + a*dt
        x = x0 + v*dt

        return(x,v,a)
    
    def long_movement(self,dt):
        x0 = self.startingpoint
        v0 = self.startingspeed
        a_list = []
        v_list = []
        x_list = []
        cycles = self.time/dt
        for idx in range(0,int(cycles)):
            movement = self.__move(x0,v0,dt)
            x_list.append(movement[0])
            v_list.append(movement[1])
            a_list.append(movement[2])
            x0 = x_list[idx]
            v0 = v_list[idx]
        return(x_list,v_list,a_list)
    
    def __analyt_sol_displacement(self,time):
        import numpy as np
        omega = np.sqrt(self.constant/self.mass)
        A = self.startingpoint
        result = []
        for i in time:
            x = A*np.cos(omega*i)
            result.append(x)
        return(result)
    
    def __analyt_sol_period(self):
        import numpy as np
        T = 2*np.pi*np.sqrt(self.mass/self.constant)
        return(T)

    def plotting(self,t):
        import matplotlib.pyplot as matplot
        import numpy as np

        time = np.linspace(0,t,int(t/self.deltat))
        lists = self.long_movement(dt)
        comparison = self.__analyt_sol_displacement(time)

        fig, axes = matplot.subplots(nrows=1, ncols=3)

        axes[0].plot(time,comparison,label='analytical solution')
        axes[0].plot(time,lists[0],'ro',markersize=1,label='xt')
        axes[1].plot(time,lists[1],'go',markersize=1,label='vt')
        axes[2].plot(time,lists[2],'bo',markersize=1,label='at')
        matplot.show()

    def multiple_dt(self,t,dt1,dt2,dt3):
        import matplotlib.pyplot as matplot
        import numpy as np

        dt_list = []
        multi_dt = [dt1,dt2,dt3]

        for i in multi_dt:
            Ndt = i
            dt_list.append(self.long_movement(Ndt)[0])

        for idx,i in enumerate(dt_list):
            time = np.linspace(0,t,int(t/multi_dt[idx]))
            comparison = self.__analyt_sol_displacement(time)
            matplot.plot(time,i,'ro',markersize=0.5,label='dt = {}'.format(multi_dt[idx]))
        matplot.plot(time,comparison,label='analytical solution')
        matplot.show()

    def period_titranja(self,dt1,dt2,dt3):

        multi_dt = [dt1,dt2,dt3]

        for idx, dt in enumerate(multi_dt):
            loop = True
            v0 = self.startingspeed
            x0 = self.startingpoint
            t = 0
            goal_range = self.__move(x0,v0,dt)[0]
            if x0 >= 0:
                direction = 'down'
            else:
                direction = 'up'
            while loop == True:
                movement = self.__move(x0,v0,dt)
                x0 = movement[0]
                v0 = movement[1]
                t = t+dt
                if direction == 'down' and x0>goal_range:
                    break
                if direction == 'up' and x0<goal_range:
                    break 
            actual_result = self.__analyt_sol_period()
            print('Period titranja za dt{} numerički je {}, dok je stvarni rezultat {}'.format(idx,t,actual_result))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

m = 1
k = 10
t = 7
x0 = 9
v0 = 0
dt = 0.01

dt1 = 0.001
dt2 = 0.01
dt3 = 0.05

test = HarmonicOscillator(m,k,t,x0,v0,dt)
test.plotting(t)
test.multiple_dt(t,dt1,dt2,dt3)
test.period_titranja(dt1,dt2,dt3)









