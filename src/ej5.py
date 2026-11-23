nombres=[]
telefonos=[]
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
        nombres.append(str(input("Introduce el nombre: ")))
        telefonos.append(int(input("Introduce el telefono: ")))
    elif option==2:
        for i in range(len(nombres)):
            print("nombre:",nombres[i],", telefono",telefonos[i])
    elif option !=0:
        print("Opcion Incorrecta")