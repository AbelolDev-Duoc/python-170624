from os import system

validacion_salida = False
trabajadores = []

def Registrar_Trabajador():
    nombre = input("Ingrese el nombre y apellido del trabajador: ")
    cargo = input("Ingrese el cargo del trabajador: ")
    sueldo_bruto = int(input("Ingrese el sueldo bruto del trabajador: "))
    desc_salud =  int(round(sueldo_bruto *  7/100,0))
    desc_afp =  int(round(sueldo_bruto*12/100,0))
    liquido = sueldo_bruto - desc_salud - desc_afp

    trabajadores.append({
            "nombre": nombre,
            "cargo": cargo,
            "sueldo_bruto": sueldo_bruto,
            "desc_salud": desc_salud,
            "desc_afp": desc_afp,
            "liquido": liquido,
        })
    
    print("Se ha registradro con exito al trabajador")
    input("Presione ENTER para continuar")

    return

def Listar_Trabajadores():
    print(f"Nombres\t    Cargo\t    Sueldo_bruto\t    Desc_Salud\t    Desc_afp\t    Sueldo_líquido\t")
    for trabajador in trabajadores:
        print(f"{trabajador['nombre']}\t    {trabajador['cargo']}\t    {trabajador['sueldo_bruto']}\t    {trabajador['desc_salud']}\t    {trabajador['desc_afp']}\t    {trabajador['liquido']}\t") #No se puede hacer un recorrido para N llaves
        input("Presione ENTER para continuar")
    return

def Imprimir_Panilla_Sueldos(trabajadores:list):
    with open("Datos.txt","w",) as archivo:
        for trabajador in trabajadores:
            archivo.write(F"Nombre: {trabajador['nombre']}\n")
            archivo.write(F"Cargo: {trabajador['cargo']}\n")
            archivo.write(F"Sueldo bruto: {trabajador['sueldo_bruto']}\n")
            archivo.write(F"Descuento de salud: {trabajador['desc_salud']}\n")
            archivo.write(F"Descuento de AFP: {trabajador['desc_afp']}\n")
            archivo.write(F"Sueldo liquido: {trabajador['liquido']}\n")
    print("Se han almacenado los datos")
    input("Presione ENTER para continuar")

    return

while validacion_salida == False:
    system("cls")
    print("Seleccione una opción: ")
    print("1-) Registrar trabajador")
    print("2-) Listar todos los trabajadores")
    print("3-) Imprimir planilla de sueldos")
    print("4-) Salir del programa")
    try:
        opcion = int(input(">>> "))
        match opcion:
            case 1:
                Registrar_Trabajador()
            case 2:
                Listar_Trabajadores()
            case 3:
                Imprimir_Panilla_Sueldos(trabajadores)
            case 4:
                print("Adíos...")
                validacion_salida = True
            case _:
                print("Opción no válida.")
    except ValueError:
        print("El valor debe ser un número")