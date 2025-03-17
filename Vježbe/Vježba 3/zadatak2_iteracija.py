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

# 