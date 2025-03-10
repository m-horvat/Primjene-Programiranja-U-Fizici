# napravio sam zadatak 4 na drugom kompjuteru pa ću samo napraviti program koji može stvoriti pdf s grafom i kasnije sve spojiti

# repeat = True
# while repeat == True:
#     repeat = False
#     print('-----------------------------------')
#     x1 = input("Unesite x-koordinatu prve točke: ")
#     y1 = input("Unesite y-koordinatu prve točke: ")
#     x2 = input("Unesite x-koordinatu druge točke: ")
#     y2 = input("Unesite y-koordinatu druge točke: ")
#     print('-----------------------------------')

#     lista_brojeva = [x1,y1,x2,y2]
    
#     for broj in lista_brojeva:
#         for idx, i in enumerate(broj):
#             if i not in '0123456789.':
#                 repeat = True
#                 print('Nastala je greška, pokušaj ponovno!')
#                 print('-----------------------------------')
#         if repeat == True:
#                 break 

# k = (int(y2)-int(y1))/(int(x2)-int(x1))
# l = int(y1) - k*int(x1)
# print('Pravac koji povezuje dvije točke je y={}x+{}'.format(str(k),str(l)))
# print('-----------------------------------')

import os
import matplotlib.pyplot as matplot
import numpy as np

repeat = True

x = np.linspace(0,10)
y = np.sin(x)
matplot.plot(x,y)

print('Kako želite prikaziti svoj rezultat? \n0 = Prikaži u programu, 1 = Spremi kao PDF')

while repeat == True:
    print('------------------------------------------')
    saving = input()

    if saving == '1':
        os.chdir("C:/Users/Student/Primjene-Programiranja-U-Fizici/Vježbe/Vježba 1")
        matplot.savefig("line_graph.pdf", format="pdf")
        break
    elif saving == '0':
        matplot.show()
        break
    else:
        print('Pokušaj ponovno!')

