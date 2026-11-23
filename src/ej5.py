nombres=[]
telefonos=[]
contador=0
option=-1

while(option!=0):
    print("====================================================")
    print("MENU")
    print("1. Introducir un contacto")
    print("2. Leer agenda")
    print("Introduce una opcion (0 para salir)")
    print("====================================================")
    try:
        option=int(input(": "))
    except:
        print("Opcion Incorrecta")
        continue
    if option==1:
        nombre=str(input("Introduce el nombre: "))
        telefono=int(input("Introduce el telefono: "))

        nombres.append(nombre)
        telefonos.append(telefono)
        contador+=1
    elif option==2:
        for i in range(contador):
            print("nombre:",nombres[i],", telefono",telefonos[i])