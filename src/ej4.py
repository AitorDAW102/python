identificarNumero=int(input("Dime un numero y te digo su primo: "))
esPrimo = True

for divisor in range(2,identificarNumero):
    if (identificarNumero%divisor)==0:
        esPrimo=False
        break

if esPrimo:
    print(identificarNumero,"es primo")
else:
    print(identificarNumero,"no es primo")