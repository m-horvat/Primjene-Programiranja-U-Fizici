# SIDENOTE: i overcomplicated the assigned task because i wanted to have fun whilst making this
# thank you for understanding <3

import matplotlib.pyplot as matplot
import numpy as np
import os

def plotting(k,l,x1,x2,y1,y2,rez):

    # this is a mess and i hate how this looks
    x = np.linspace(-30,30)
    matplot.grid(visible=None, linestyle='dotted', which='major', axis='both')
    matplot.axis([-30, 30, -30, 30])
    matplot.title('Crtanje izabranog pravca y=kx+l')
    matplot.plot(x,x-x,'#999999')
    matplot.plot(x-x,x,'#999999')
    
    if k != 'inf':
        y = (k*x)+l
    else:
        y = x
        x = x-x+l
        
    matplot.plot(x,y,'#000000', label=rez)
    matplot.plot(x1, y1,'ro', label='Točka ({},{})'.format(x1,y1)) 
    matplot.plot(x2, y2,'bo', label='Točka ({},{})'.format(x2,y2)) 
    matplot.legend()
    saving()

def saving():
    repeat = True
    while repeat == True:
        print('Kako želite prikaziti svoj rezultat? \n0 = Prikaži u programu, 1 = Spremi kao PDF\n------------------------------------------')
        saving = input()

        if saving == '1':
            # os.chdir("C:/Users/Student/Primjene-Programiranja-U-Fizici/Vježbe/Vježba 1")
            matplot.savefig("line_graph.pdf", format="pdf")
            break
        elif saving == '0':
            matplot.show()
            break
        else:
            print('Pokušaj ponovno!\n------------------------------------------')

def numberify(t1,t2): # << turns the coordinates of two points into a single list of numbers
    skup = [t1,t2]
    for idx, t in enumerate(skup):
        t = t.strip('()').split(',')
        for idx_i, i in enumerate(t):
            t[idx_i] = float(i)
        skup[idx] = t
    skup = skup[0] + skup[1] # << simplifying this list into a singular list
    return(skup)

def pravac_dva_tocaka(t1,t2):
    lista = numberify(t1,t2)

    # i guess i dont have to do this, but its more readable this way
    x1 = lista[0]
    y1 = lista[1]
    x2 = lista[2]
    y2 = lista[3]

    if x2-x1 != 0:
        k = (y2-y1)/(x2-x1)
        l = y1-k*x1
        rez = 'y={}x+{}'.format(str(k),str(l))
    else:
        if y1 != y2:
            l = x1
            rez = 'x={}'.format(l)
            k = 'inf'
        else:
            rez = 'svaki mogući pravac, jer su obje točke na istoj koordinati.'
            k = 0
            l = 0
    
    plotting(k,l,x1,x2,y1,y2,rez)
    return rez

def checking_validity(t1,t2):
    valid = True
    skup = [t1,t2] 
    for nums in skup:
        if ',' not in nums:
            valid = False
        for idx, i in enumerate(nums):
            if i in '(1234567890)':
                continue
            elif i == '.' and nums[idx-1] in '1234567890':
                continue
            elif i == '-' and nums[idx+1] in '1234567890':
                continue
            elif i == ',' and nums[idx] != nums[0] and nums[idx] != nums[-1]:
                continue
            elif valid == True: # << this is here so that if this is triggered once it doesn't trigger a second time
                valid = False
    return valid

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

print('-----------------------------------\nNapišite dvije točke u obliku (x,y).')
loop = True
while loop == True:
    print('-----------------------------------')
    tocka_1 = input("Unesite koordinatu prve točke:  ")
    tocka_2 = input("Unesite koordinatu druge točke: ")
    print('-----------------------------------')
    valid = checking_validity(tocka_1,tocka_2)
    if valid == True:
        break
    else:
        print('Pokušaj ponovno!')

pravac = pravac_dva_tocaka(tocka_1,tocka_2)
print('Pravac koji povezuje dvije točke je {}'.format(pravac))