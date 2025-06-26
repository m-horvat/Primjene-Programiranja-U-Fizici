import numpy as np
import matplotlib.pyplot as matplot

class starcounting:
    def __init__(self,angle_boundary, offset, filename,luminosity_limit):
        self.angle_boundary = angle_boundary
        self.offset = offset
        self.filename = filename
        self.library = self.__data(filename,luminosity_limit)
    # - - - - - - - - - - - - data extraction - - - - - - - - - - - -

    def __data(self,filename,luminosity_limit):
        library = []
        with open(filename, 'r') as file:
            for id, line in enumerate(file):
                if id == 0:
                    continue
                template = {'ID':0,'phi':0,'theta':0,'magnitude':0}
                split_line = line.split()
                for id, item in enumerate(split_line):
                    if item[-1] == ',':
                        item = item[0:-1]
                    if ',' in item:
                        item = item.replace(',','.')
                    split_line[id] = item
                for id, variable in enumerate(template):
                    template[variable] = template[variable]+float(split_line[id])

                if template['magnitude'] < luminosity_limit:
                    library.append(template)
        return(library)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # figuring out which stars can be seen depending on the angle that is being looked at

    def __boundarycorrection(self,angle_boundary):
        true_sight_RA = [0+angle_boundary[0],0-angle_boundary[0]]
        true_sight_RD = [0+angle_boundary[1],0-angle_boundary[1]]

        # phi (right ascension)
        for id,i in enumerate(true_sight_RA):
            if i < 0:
                true_sight_RA[id] = 360+i
            elif i > 360:
                true_sight_RA[id] = i-360

        # theta (right declination)
        for id,i in enumerate(true_sight_RD):
            if i < -90:
                true_sight_RD[id] = -90
            elif i > 90:
                true_sight_RD[id] = 90

        return(true_sight_RA,true_sight_RD)

    def seeablestars(self,angle_boundary,offset,filename):

        library = self.library
        star_list_offset = []
        
        true_sight = self.__boundarycorrection(angle_boundary)


        for idx, star in enumerate(library):

            # right ascension movement
            new_phi = star['phi']

            if star['phi'] > true_sight[0][0] and star['phi'] < true_sight[0][1]:
                new_theta = star['theta']+offset[1]

                # special case for the stars that go above 90 degrees on RA
                if new_theta > 90:

                    new_theta = star['theta'] + offset[1]
                    if new_theta > 90:
                        new_theta = 90-(new_theta-90)

                    phi_offset = 180 - star['phi']*2
                    new_phi = star['phi'] + phi_offset
                    while new_phi < 0:
                        new_phi = new_phi + 360

            else:
                new_theta = star['theta']-offset[1]

                # special case for the stars that go below 90 -degrees on RA
                if new_theta < -90:

                    new_theta = star['theta'] - offset[1]
                    if new_theta < -90:
                        new_theta = -90-(new_theta+90)

                    phi_offset = 180 - star['phi']*2
                    new_phi = star['phi'] + phi_offset
                    while new_phi < 0:
                        new_phi = new_phi + 360

            # right declination movement

            new_phi = new_phi + offset[0]
            if new_phi < 0:
                new_phi = 360+new_phi
            elif new_phi > 360:
                new_phi = new_phi-360

            template = star.copy()
            template['ID'] = idx
            template['theta'] = new_theta
            template['phi'] = new_phi
            star_list_offset.append(template)

            visible_star_list = []

            for star in star_list_offset:
                cond_1, cond_2 = False, False
                if star['phi'] > true_sight[0][0] and star['phi'] < true_sight[0][1]:
                    cond_1 = True
                if star['theta'] < true_sight[1][0] and star['theta'] > true_sight[1][1]:
                    cond_2 = True
                if cond_1 == True and cond_2 == True:
                    visible_star_list.append(star)

        return(visible_star_list)

    def plot(self):

        visible_star_list = self.seeablestars(angle_boundary,offset,filename)

        x, y = [], []

        for star in visible_star_list:
            line = str(star['magnitude'])
            if star['magnitude'] < 10:
                colorstar = '#000000'
            if line[0] != '-':
                colorstar = '#'+str(line[0]+line[0]+line[0]+line[0]+line[0]+line[0])
            matplot.plot(star['phi'],star['theta'],color=colorstar,marker='.',linestyle='none')

        matplot.grid('both')
        matplot.xlabel('RA (Right ascension) $\phi$')
        matplot.ylabel('RD (Right declination) $\dot{\Theta}$')
        matplot.title('Coordinate system of stars')
        matplot.show()

    def count_circle(self,degrees,count):
        divider = (degrees[1]-degrees[0])/count
        divider = str(divider).split('.')
        x, y = [], []
        for t in range(degrees[0],degrees[1],int(divider[0])):
            new_offset = [t,0]
            y.append(len(self.seeablestars(self.angle_boundary,new_offset,self.filename)))
            x.append(t)
        return(x,y)
    
    def count_circle_plot(self,degrees,count):
        coordinates = self.count_circle(degrees,count)
        matplot.plot(coordinates[0],coordinates[1],color="#E67309",marker='.')
        matplot.grid('both')
        matplot.xlabel('RA (Right ascension) $\phi$')
        matplot.ylabel('Visible stars (x)')
        matplot.title('Stars visible at a certain angle')
        matplot.show()


        



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# the point im looking at right now is in the center of the earth Lol !!

#theta = [x['theta'] for x in library]
#phi   = [x['phi']   for x in library]

# this determines the range of theta and phi of stars that can be seen
# what that means is that the first number's range will deviate 90 degrees from the starting angle in both directions
# ex. start angle = 10, boundary = 50, it will search all stars from 0 to 60 and 320 to 360
# preferably don't go past 90 (its not realistic to see more than 180 degrees of the sky anyway)
angle_boundary = [90,90]
luminosity_limit = 5

# offsetted from the vernal equinox, assume that the vernal equinox is in the constellation pisces
offset   = [0,0]        
filename = 'dataset'   
degrees  = [0,360]       # the span at which you want to analyze (do not put the same number twice if you're counting in a circle)
count    = 50            # how many times (data points on the x axis) do you want to analyze

stars     = starcounting(angle_boundary, offset, filename, luminosity_limit)

# offset = [90,0]
stars.plot()

stars.count_circle_plot(degrees,count)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 