# A)

a = 5.0-4.935
print(a)

# Rezultat koji se očekuje nakon što se oduzme ova dva broja je 0.065.
# Međutim, to se ne događa u Python-u i dobijemo rezultat 0.06500000000000039. 
# Uzrok toga je zbog načina kako Python sprema podatke u memoriji (u obliku binarnog zapisa) 
# te koliko je velik rezervirani dio memorije na računalu.

# B)

b = 0.1 + 0.2 + 0.3
if b == 0.6:
    print('Suma iznosi 0.6.')
else:
    print('Suma ne iznosi 0.6.')

# Zbog navedenog u vježbi 1.A, suma ne iznosi 0.6 iako bi moralo.

