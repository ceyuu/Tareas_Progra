# Ejercicio:
def mostrar_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Agregar solicitud")
    print("2. Buscar solicitud")
    print("3. Eliminar solicitud")
    print("4. Actualizar estado de solicitudes")
    print("5. Mostrar solicitudes")
    print("6. Salir")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción(1-6): "))
            if opcion>=1 and opcion<=6:
                return opcion
            print("Error! opción no válida!")
        except:
            print("Error! debe ingresar un número entero!")

def validar_id_solicitud(valor, lista:list):
    if len(valor)<6:
        return False,"Error, el id debe tener al menos 6 caracteres!"
    if " " in valor:
        return False,"Error, el id no puede tener espacios!"
    if valor in lista:
        return False,"Error, el id ya existe!"
    return True,"Id correcto!"

def validar_nombre_solicitud(nombrecito):
    if len(nombrecito)<4:
        return False, "Error, el nombre debe tener al menos 4 carácteres"
    elif " " in nombrecito:
        return False, "Error, el nombre no debe contener espacios"
    return True, "Nombre registrado"

def validar_area_solicitud(parametro_area):
    if parametro_area[0] not in ('S','R','M'):
        return False, "Error, área no encontrada, debe ser 'Soporte', 'Redes' o 'Mantención'"
    return True, "Área ingresada"

def validar_prioridad_solicitud(numerito_prioridad):
    if numerito_prioridad<1 or numerito_prioridad>5:
        return False, "Error, la prioridad debe estar entre 1 y 5"
    return True, "Prioridad registrada"

def validar_costo_estimado(valor):
    if valor < 0:
        return False, "Error"
    return True, "Costo agregado exitosamente"

def buscar_registro(registros, id_solicitud:list):
    # Lista_de_diccionario = [solicitudes]
    # llave = "id"
    for d in enumerate(id_solicitud,1):
        if registros in id_solicitud: # podría ocupar un ciclo for
            return d, "ID encontrado!!"
        return False, "Error, ID no existente"

# Comienza mi ejercicio:
solicitudes = []
while True:
    mostrar_menu()
    opcion = leer_opcion()
    if opcion==1:
        id = input("Ingrese id: ")
        validacion,mensajito = validar_id_solicitud(id, solicitudes)
        if not validacion:
            print(mensajito)
            continue
        nombre = input("Ingrese nombre: ")
        validacion, mensajito = validar_nombre_solicitud(nombre)
        if not validacion:
            print(mensajito)
            continue
        area = input("Ingrese área: ").title()
        validacion, mensajito = validar_area_solicitud(area)
        if not validacion:
            print(mensajito)
            continue
        prioridad = int(input("Ingrese prioridad(1-5): "))
        # DEBE SER UN NUMERO ENTERO ENTRE 1 Y 5
        # TRUE OR FALSE
        validacion, mensajito = validar_prioridad_solicitud(prioridad)
        if not validacion:
            print(mensajito)
            continue
        costo = int(input("Ingrese costo: "))
        # TRUE OR FALSE
        validacion, mensajito = validar_costo_estimado(costo)
        if not validacion:
            print(mensajito)
            continue
        solicitud = {
            "id": id,
            "nombre": nombre,
            "area": area,
            "prioridad": prioridad,
            "costo": costo,
            "estado": False
        }
        solicitudes.append(solicitud)
        print("Solicitud agregada con éxito!")
    elif opcion==2:
        print(" *** BUSCAR SOLICITUD ***")
        # Debe permitir consultar un registro según su id_solicitud.
        # Recibe el dato a validar y retorna si es válido o no. true or False
        # Si el registro existe, se debe entregar su posición dentro de la lista.
        id_buscado = input("Ingrese el ID que desea buscar: ")
        validacion, mensajito = buscar_registro(id_buscado, solicitudes)
        if not validacion:
            print(mensajito)
            continue
        else:
            print(d)
    elif opcion==3:
        pass
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    else:
        print("Adios!")
        break
