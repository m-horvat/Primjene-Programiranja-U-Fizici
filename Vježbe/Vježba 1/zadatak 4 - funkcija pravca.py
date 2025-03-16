def pravac_dva_tocaka(t1,t2):
    skup = [t1,t2]
    for idx, t in enumerate(skup):
        t = t.strip('()').split(',')
        for idx_i, i in enumerate(t):
            t[idx_i] = float(i)
        skup[idx] = t
    skup = skup[0] + skup[1] # << simplifying this list into a singular list

    x1 = skup[0]
    y1 = skup[1]
    x2 = skup[2]
    y2 = skup[3]

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
    
    return rez

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

print('-----------------------------------\nNapišite dvije točke u obliku (x,y).')
loop = True
while loop == True:
    loop = False
    print('-----------------------------------')
    tocka_1 = input("Unesite koordinatu prve točke:  ")
    tocka_2 = input("Unesite koordinatu druge točke: ")
    print('-----------------------------------')
    skup = [tocka_1,tocka_2] 
    for nums in skup:
        if ',' not in nums and loop == False:
            loop = True
            print('Pokušaj ponovno!')
        for idx, i in enumerate(nums):
            if i in '(1234567890)':
                continue
            elif i == '.' and nums[idx-1] in '1234567890':
                continue
            elif i == '-' and nums[idx+1] in '1234567890':
                continue
            elif i == ',' and nums[idx] != nums[0] and nums[idx] != nums[-1]:
                continue
            elif loop == False: # << this is here so that if this is triggered once it doesn't trigger a second time
                loop = True
                print('Pokušaj ponovno!')

pravac = pravac_dva_tocaka(tocka_1,tocka_2)
print('Pravac koji povezuje dvije točke je {}'.format(pravac))