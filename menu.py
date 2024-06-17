from os import system
validacion_salida = False

while validacion_salida == False:
    print("Seleccione una opción: ")
    print("1-) ")
    print("2-) ")
    print("3-) ")
    print("4-) ")
    try:
        opcion = int(input(">>> "))
        match opcion:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                print("Adíos...")
                validacion_salida = True
            case _:
                print("Opción no válida.")
    except ValueError:
        print("El valor debe ser un número")