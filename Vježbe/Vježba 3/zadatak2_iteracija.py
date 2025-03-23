N = 20
broj = 5
rez = []

for tick in range(0,3):
    N *= 10
    for i in range(0,N):
        broj += 1/3
    for i in range(0,N):
        broj -= 1/3
    rez.append(broj)

print(rez)

# Rezultati koji nastaju nakon neprestanog zbrajanja i oduzimanja 1/3 su različiti.
# Razlog greške je također zbog memorije (vidi zadatak 1.)
# Međutim, možemo primjetiti da greška postaje veća kad je petlja dodavanja i oduzimanja znatno veći. 
# (200 je strogo manji od 20000, pa je greška veća.)