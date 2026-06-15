estudiantes= []


def mostrar_menu():
    print("""1. Agregar estudiante
2. Buscar estudiante
3. Eliminar estudiante
4. Mostrar estudiantes
5. Salir""")
    return

def validar_opcion():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese la opción que desee (1-5): "))
            if opcion >=1 and opcion <=5:
                return opcion
            print("Error! Ingrese un número entero entre 1 y 5")
        except:
            print("Error! Debe ingresar un número entero")

# AGREGAR ESTUDIANTE

def agregar_estudiante(estudiantes:list):
    estudiante = input("Ingrese el nombre del estudiante que desea agregar: ").title().strip()
    if len(estudiante)<1:
        print("Error, el nombre no debe estar vacío")
    print("Estudiante agregado exitosamente")
    estudiantes.append(estudiante)
    return

def buscar_estudiante(estudiantes:list):
    estudiante = input("Ingrese el nombre del estudiante que desea buscar: ").title().strip()
    if estudiante not in estudiantes:
        print("Error, estudiante no encontrado")
    print("El estudiante si existe")

def eliminar_estudiante(estudiantes:list):
    estudiantito = input("Ingrese el nombre del estudiante que desee eliminar: ").title().strip()
    if estudiantito not in estudiantes:
        print("Error, estudiante no encontrado")
    estudiantes.remove(estudiantito)
    print("Se ha eliminado al estudiante")


while True:
    opcion = validar_opcion()
    if opcion == 1:
        agregar_estudiante(estudiantes)
    elif opcion == 2:
        buscar_estudiante(estudiantes)
    elif opcion == 3:
        eliminar_estudiante(estudiantes)
    elif opcion == 4:
        print("*** ESTUDIANTES ***")
        for e in estudiantes:
            print(e)
    else:
        print("Gracias por usar nuestros servicios, adiositou!")
        break