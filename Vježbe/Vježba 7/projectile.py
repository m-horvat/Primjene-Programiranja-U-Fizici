import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self,x0,y0,m,v0,theta,ro,A,C,dt=0.01):
        self.x0 = x0
        self.y0 = y0
        self.m = m
        self.v0 = v0
        self.theta = theta
        self.ro = ro
        self.A = A
        self.C = C
        self.dt = dt

    def __sgn(self,x):
        return np.sign(x) if x != 0 else 0

    def __akc(self,vx,vy,D,m,g=9.81):
        ax = -(D/m)*vx**2*self.__sgn(vx)
        ay = -g-(D/m)*vy**2*self.__sgn(vy)
        return (ax,ay)

    def __explicit_step(self,x0,y0,vx0,vy0,dt,D,m,g):
        ax0,ay0 = self.__akc(vx0,vy0,D,m,g)

        vx = vx0+ax0*dt
        vy = vy0+ay0*dt
        x = x0+vx0*dt
        y = y0+vy0*dt
        return(x,y,vx,vy)

    def __runge_kutta(self,x1,y1,vx1,vy1,dt,D,m,g):
        k1x, k1y = self.__akc(vx1,vy1,D,m,g)
        l1x = vx1
        l1y = vy1

        vx2 = vx1 + 0.5*dt*k1x
        vy2 = vy1 + 0.5*dt*k1y
        k2x, k2y = self.__akc(vx2,vy2,D,m,g)
        l2x = vx1 + 0.5*dt*k2x
        l2y = vy1 + 0.5*dt*k2y

        vx3 = vx2 + 0.5*dt*k2x
        vy3 = vy2 + 0.5*dt*k2y
        k3x, k3y = self.__akc(vx3,vy3,D,m,g)
        l3x = vx2 + 0.5*dt*k3x
        l3y = vy2 + 0.5*dt*k3y

        vx4 = vx3 + dt*k3x
        vy4 = vy3 + dt*k3y
        k4x, k4y = self.__akc(vx4,vy4,D,m,g)
        l4x = vx3 + dt*k4x
        l4y = vy3 + dt*k4y
    
        vx = vx1 + (dt/6)*(k1x+2*k2x+2*k3x+k4x)
        vy = vy1 + (dt/6)*(k1y+2*k2y+2*k3y+k4y)

        x = x1 + (dt/6)*(l1x+2*l2x+2*l3x+l4x)
        y = y1 + (dt/6)*(l1y+2*l2y+2*l3y+l4y)

        return (x,y,vx,vy)
    
    def calculate(self,dt=0.01,type='RK',analytical=True,g=9.81):

        v0x = self.v0*np.cos(np.radians(self.theta))
        v0y = self.v0*np.sin(np.radians(self.theta))
        x_expl,  x_RK  = [self.x0], [self.x0]
        y_expl,  y_RK  = [self.y0], [self.y0]
        vx_expl, vx_RK = [v0x]    , [v0x]
        vy_expl, vy_RK = [v0y]    , [v0y]
        x_A, y_A =       [self.x0], [self.y0]

        D = self.ro*self.A*self.C/2

        t = 0

        while y_expl[-1] >= 0 and y_RK[-1] >= 0:
            if type == 'euler' or type == 'both':
                X, Y, VX, VY = self.__explicit_step(x_expl[-1],y_expl[-1],vx_expl[-1],vy_expl[-1],dt,D,self.m,g)
                x_expl.append(X)
                y_expl.append(Y)
                vx_expl.append(VX)
                vy_expl.append(VY)
            
            if type == 'RK' or type == 'both':
                X, Y, VX, VY = self.__runge_kutta(x_RK[-1],y_RK[-1],vx_RK[-1],vy_RK[-1],dt,D,self.m,g)
                x_RK.append(X)
                y_RK.append(Y)
                vx_RK.append(VX)
                vy_RK.append(VY)

            t+=dt

        plt.figure(figsize=(10,8))
        if type == 'euler' or type == 'both':
            plt.plot(x_expl,y_expl, 'b', label='Eulerova metoda')
        if type == 'RK' or type == 'both':
            plt.plot(x_RK,y_RK, 'g', label='Runge-Kutta 4. reda')
        plt.xlabel('Udaljenost [m]')
        plt.ylabel('Visina [m]')
        plt.legend()
        plt.show()
