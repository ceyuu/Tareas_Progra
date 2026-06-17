def mostrar_menu():
    print("""1. Agregar estudiante
2. Agregar nota
3. Mostrar estudiantes
4. Mostrar promedio de un estudiante
5. Mostrar todos los promedios
6. Salir""")

def validar_opcion():
    mostrar_menu()
    try:
        opcion = int(input("Ingrese la opción que desee (1-6): "))
        if opcion >=1 and opcion <=6:
            return opcion
        print("Error! Ingrese un número entero entre 1 y 6")
    except:
        print("Error! Debe ingresar un número entero")