
palabra = str(input("Introduce una palabra mayor o igual de 3 letras: "))

letra = str(input("Introduce la a letra a contar: "))
contador =0
for i in range(len(palabra)):
    if palabra[i] == letra[0]:
        contador+=1

if len(palabra)>=3 or contador>0:
    print("La palabra se repite",contador,"veces")
else:
    print("La palabra no tiene 3 letras o no se repite la letra")