estudiantes = {}
nota = []

def mostrar_menu():
    print("""1. Agregar estudiante
2. Agregar nota
3. Mostrar estudiantes
4. Mostrar promedio de un estudiante
5. Mostrar todos los promedios
6. Salir""")
    return

def validar_opcion():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese la opción que desee (1-6): "))
            if opcion >=1 and opcion <=6:
                return opcion
            print("Error! Ingrese un número entero entre 1 y 6")
        except:
            print("Error! Debe ingresar un número entero")

def agregar_estudiante(estudiantes:dict):
    estudiante = input("Ingrese el nombre del estudiante que desea agregar: ").title().strip()
    if len(estudiante)<1:
        print("Error, el nombre no debe estar vacío")
    print("Estudiante agregado exitosamente")
    estudiantes[estudiante] = None
    return estudiante

def agregar_nota(estudiantes:dict):
    estudiante = input("Ingrese el nombre del estudiante que desea agregarle nota: ").title().strip()
    if estudiante not in estudiantes:
        print("Error! el estudiante no existe")
    else:
        while True:
            try:
                estudiantes[estudiante] = nota
                notita = float(input("Ingrese la nota del estudiante: "))
                if notita >= 1 and notita <= 7:
                    nota.append(notita)
                    return
            except:
                print("Error! Debe ingresar un número")

def promedio_estudiante(estudiantes:dict):
    estudiante = input("Ingrese el nombre del estudiante que desea ver el promedio: ").title().strip()
    if estudiante not in estudiantes:
        print("Error! el estudiante no existe")
        return
    else:
        suma = sum(estudiantes[estudiante])
        largo = len(estudiantes[estudiante])
        promedio = suma/largo
        print(f"{estudiante} -> Promedio: {promedio}")


while True:
    opcion = validar_opcion()
    if opcion == 1:
        estudiante = agregar_estudiante(estudiantes)
    elif opcion == 2:
        agregar_nota(estudiantes)
    elif opcion == 3:
        for e in estudiantes:
            print(e)
    elif opcion == 4:
        promedio_estudiante(estudiantes)
    elif opcion == 5:
        if len(estudiantes) == 0:
            print("no hay estudiantes registrados")
        else:
            if len(estudiante) == 0:
                print("no hay notas")
            else:
                for estudiante in estudiantes:
                    promedito = sum(estudiante)/len(estudiante)
                    print(f"{estudiante} -> Promedio: {promedito}")
    else:
        print("Gracias por usar nuestros servicios, chaitou")
        break