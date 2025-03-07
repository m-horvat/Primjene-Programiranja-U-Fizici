loop = True

while loop == True:
    x1 = input("Unesite prvu točku: ")
    y1 = input("Unesite drugu točku: ")

    if type(x1) != int or type(y1) != int:
        print('Pokušajte ponovno.')
        continue

    print('Prva točka glasi: ({},{})'.format(x1,y1))
    break

while loop == True:
    x2 = input("Unesite prvu točku: ")
    y2 = input("Unesite drugu točku: ")

    if type(x2) != int or type(y2) != int:
        print('Pokušajte ponovno.')
        continue

    print('Druga točka glasi: ({},{})'.format(x2,y2))
    break

k = (y2-y1)*(x2-x1)
print('Pravac koji povezuje dvije točke je y={}x'.format(str(k))