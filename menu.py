from os import system

validacion_salida = False
trabajadores = {}


def Registrar_Trabajador():
    nombre = input("Ingrese el nombre y apellido del trabajador: ")
    cargo = input("Ingrese el cargo del trabajador: ")
    sueldo_bruto = int(input("Ingrese el sueldo bruto del trabajador: "))

    trabajador = {
        'cargo':cargo,
        'sueldo_bruto':sueldo_bruto
    }

    trabajadores[nombre] = trabajador
    print("Se ha registradro con exitos")


while validacion_salida == False:
    print("Seleccione una opción: ")
    print("1-) Registrar trabajador")
    print("2-) ")
    print("3-) ")
    print("4-) ")
    try:
        opcion = int(input(">>> "))
        match opcion:
            case 1:
                Registrar_Trabajador()
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