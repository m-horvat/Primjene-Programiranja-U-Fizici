import numpy as np

numbers = [2.5,1.9,6.7,3.4,4,5.6,4.5,6.8,3.5,7.8]

aa = np.mean([numbers])
sd = np.std([numbers])

print('Aritmetička sredina navedenih brojeva je {}, dok je standardna devijacija {}.'.format(aa,sd))