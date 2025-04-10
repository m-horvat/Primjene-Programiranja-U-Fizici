# this was honestly my favourite problem so far. genuinely so fun :)

class Particle:
    def __init__(self,v0,theta,x0=0,y0=0):
        self.poc_brzina = v0
        self.kut_otklona = theta
        self.poc_pol_x = x0
        self.poc_pol_y = y0

    def reset(self):
        v0 = self.poc_brzina
        theta = self.kut_otklona
        x0 = self.poc_pol_x
        xy = self.poc_pol_y

        print(v0,theta,x0,xy)

    def __move(self,vy,vx,x0,y0,deltat):

        x0 += vx*deltat
        vy -= 9.81*deltat
        y0 += vy*deltat

        return(y0,x0)

    def range(self,deltat):
        import numpy as np
        x_final = [self.poc_pol_x]
        y_final = [self.poc_pol_y]

        vy = np.sin(self.kut_otklona/180*np.pi)*self.poc_brzina
        vx = np.cos(self.kut_otklona/180*np.pi)*self.poc_brzina

        x0 = self.poc_pol_x
        y0 = self.poc_pol_y

        while y0 >= 0:
            result = self.__move(vy,vx,x0,y0,deltat)
            y0 = result[0]
            x0 = result[1]

            x_final.append(x0)
            y_final.append(y0)
        return (x_final,y_final)

    def plot_trajectory(self,deltat,t):
        import matplotlib.pyplot as matplot
        
        matplot.title('Prikaz kosoga hitca u koordinatnom sustavu')
        matplot.ylabel('y (m)')
        matplot.xlabel('x (m)')

        # honestly im really happy with how this looks !! i really like it :)

        coordinates = self.range(deltat)
        matplot.plot(coordinates[0],coordinates[1],color='#AAAAAA')

        x_new_coordinates = coordinates[0][0:int(t/deltat)]
        y_new_coordinates = coordinates[1][0:int(t/deltat)]

        matplot.axvline(x_new_coordinates[-1],color='#BBBBBB', linestyle='dotted')
        matplot.axhline(y_new_coordinates[-1],color='#BBBBBB', linestyle='dotted')
        matplot.plot(x_new_coordinates,y_new_coordinates,color='#AA0000')
        matplot.plot(x_new_coordinates[-1],y_new_coordinates[-1],color='#AA0000',marker='o',label='Trenutni položaj tijela u t={}s'.format(t))
        matplot.legend()
            
        matplot.show()
