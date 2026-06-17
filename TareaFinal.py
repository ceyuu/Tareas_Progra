reservas = []

def mostrar_menu():
    print("""\n=== MENÚ PRINCIPAL ===
1. Registrar reserva
2. Buscar reserva
3. Eliminar reserva
4. Actualizar confirmaciones
5. Mostrar reservas
6. Salir""")

def leer_opcion():
    while True:
        try:
            opc = int(input("Ingrese una opción (1-6): "))
            if opc in (1,2,3,4,5,6):
                return opc
            print("Error, debe ingresar una opción entre 1 y 6")
        except:
            print("Error, debe ingresar un número entero")

def validar_codigo_reserva(valor):
    if len(valor)==7 and " " not in valor:
        if valor[0]=='R':
            return True
        return False
    return False
# ***Falta verificar que sea único en la lista

def validar_nombre_solicitante(valor:str):
    if len(valor)>=5 and valor.isalpha():
        return True
    return False

def validar_tipo_sala(valor):
    letra = valor[0]
    if letra in ('P','M','G'):
        return True
    return False

def validar_cantidad_personas(valor):
    try:
        cantidad = int(valor)
        if cantidad>0 and cantidad<=20:
            return True
        return False
    except:
        return False
    
def validar_horas_reserva(valor):
    try:
        horas = int(valor)
        if horas > 0 and horas <= 8:
            return True
        return False
    except:
        return False

def buscar_reserva(reservas,codigo_reserva):
    for posicion in range(len(reservas)):
        if reservas[posicion]["codigo_reserva"] == codigo_reserva:
            return posicion+1
    return None

# SOLICITUD Y VALIDACION DE LOS DATOS ANTES DE LA CREACION DEL DICCIONARIO
def agregar_reserva(reservas:list):
    while True:
        codigo_reserva = input("Ingrese un código para su reserva (debe empezar con la letra 'R' y debe contener 7 caracteres): ")
        if not validar_codigo_reserva(codigo_reserva):
            print("Error, código inválido")
            continue
        if buscar_reserva(reservas, codigo_reserva) is not None:
            print("Error, el código ya fue registrado")
            continue
        break

    while True:
        nombre_solicitante = input("Ingrese el nombre del solicitante: ").title().strip()
        if validar_nombre_solicitante(nombre_solicitante):
            break
        print("Error, nombre inválido")

    while True:
        tipo_sala = input("Ingrese el tipo de sala a reservar (Pequeña, Mediana o Grande): ").title().strip()
        if validar_tipo_sala(tipo_sala):
            break
        print("Error, sala inválida")

    while True:
        cantidad_personas = input("Ingrese cantidad de personas que ocuparán el servicio: ")
        if validar_cantidad_personas(cantidad_personas):
            break
        print("Error, cantidad inválida")

    while True:
        horas_reserva = input("Ingrese horas a reservas: ")
        if validar_horas_reserva(horas_reserva):
            break
        print("Error, cantidad de horas inválidas")

    # CONSTRUCCION DEL DICCIONARIO
    reserva = {
        "codigo_reserva" : codigo_reserva,
        "nombre_solicitante" : nombre_solicitante,
        "tipo_sala" : tipo_sala,
        "cantidad_personas" : int(cantidad_personas),
        "horas_reserva" : int(horas_reserva),
        "estado" : False
    }
    # AGREGAR A LA LISTA
    reservas.append(reserva)
    print("Reserva registrada excitosamente")

# BUSCAR RESERVA    -   AGREGARLA AL MENU, NO NECESITA BLOQUE FUNCION
    
# ELIMINAR RESERVA  -   PEDIR EL CODIGO DE RESERVA A ELIMINAR EN EL MENU
def eliminar_reserva(reservas,codigo_reserva):
    posicion =  buscar_reserva(reservas, codigo_reserva)
    if posicion is None:
        print("Reserva no encontrada")
    else:
        reservas.pop(posicion)
        print("Reserva eliminada exitosamente")

# ACTUALIZAR CONFIRMACIONES
def actualizar_confirmaciones(reservas):
    for reserva in reservas:
        if int(reserva["cantidad_personas"]) >= 10:
            reserva["estado"] = True
        else:
            reserva["estado"] = False
    print("Estado actualizado correctamente")

def mostrar_reservas(reservas:list):
    for index, reserva in enumerate(reservas):
        print(f"Reserva {index}: {reserva}")

while True:
    mostrar_menu()
    opc = leer_opcion()
    if opc==1:
        print("Registrar Reserva")
        agregar_reserva(reservas)
    elif opc==2:
        print("Buscar Reserva")
        codigo = input("Ingrese el código de la reserva que busca: ").title().strip()
        busqueda = buscar_reserva(reservas,codigo)
        if busqueda is None:
            print("La reserva no existe")
        else:
            print(f"Reserva encontrada en posición {busqueda}")
    elif opc==3:
        print("Eliminar Reserva")
        codigo = input("Ingrese el código de la reserva que desea eliminar: ")
        eliminar = eliminar_reserva(reservas,codigo)
    elif opc==4:
        print("Actualizar Confirmaciones")
        actualizar_confirmaciones(reservas)
    elif opc==5:
        print("Mostrar Reservas")
        mostrar_reservas(reservas)
    elif opc==6:
        print("Gracias por usar nuestro servicio, adios! (˶ˆᗜˆ˵)")
        break