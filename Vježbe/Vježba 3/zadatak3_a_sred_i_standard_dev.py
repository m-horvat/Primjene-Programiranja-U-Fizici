import numpy as np

numbers = [2.5,1.9,6.7,3.4,4,5.6,4.5,6.8,3.5,7.8]
numbers = [1,2,3,4,5,6,7,8,9,10]
numbers = [2,8,10,13,17,17,19,21,23,30]

aa = np.mean([numbers])
sd = np.std([numbers])

# aa = arithmetic_average(numbers)
# sd = standard_deviation(numbers)

print('Aritmetička sredina navedenih brojeva je {}, dok je standardna devijacija {}.'.format(aa,sd))