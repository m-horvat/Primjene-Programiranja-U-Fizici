repeat = True

while repeat == True:
    repeat = False
    print('-----------------------------------')
    x1 = input("Unesite x-koordinatu prve točke: ")
    y1 = input("Unesite y-koordinatu prve točke: ")
    x2 = input("Unesite x-koordinatu druge točke: ")
    y2 = input("Unesite y-koordinatu druge točke: ")
    print('-----------------------------------')

    lista_brojeva = [x1,y1,x2,y2]
    
    for broj in lista_brojeva:
        for idx, i in enumerate(broj):
            if i not in '0123456789.':
                repeat = True
                print('Nastala je greška, pokušaj ponovno!')
                print('-----------------------------------')
        if repeat == True:
                break 

k = (int(y2)-int(y1))/(int(x2)-int(x1))
l = int(y1) - k*int(x1)
print('Pravac koji povezuje dvije točke je y={}x+{}'.format(str(k),str(l)))
print('-----------------------------------')

print('hello')
print('hello2')