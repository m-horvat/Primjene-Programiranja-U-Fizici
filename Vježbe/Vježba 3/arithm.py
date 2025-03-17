# zadatak kaže da napravimo aritmetičku sredinu i standardnu devijaciju za 10 broja,
# ali sam produžio zadatak tako da radi sa više i manje točaka :)

# funkcije koriste listu kao input !!!!!

def arithmetic_average(list):
    N = 0
    for i in list:
        N += i
    avg = N/len(list)

    return(avg)

# i have no clue what i did wrong with this standard deviation because it doesnt give me the output that i want

def standard_deviation(list):
    import numpy as np

    N = 0
    avg = arithmetic_average(list)
    for i in list:
        N += (i-avg)**2
    
    sd = np.sqrt(N/(len(list)*(len(list)-1)))
    return(sd)

numbers = [2.5,1.9,6.7,3.4,4,5.6,4.5,6.8,3.5,7.8]
numbers = [1,2,3,4,5,6,7,8,9,10]

aa = arithmetic_average(numbers)
sd = standard_deviation(numbers)

print(aa,sd)