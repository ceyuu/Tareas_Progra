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
# Falta verificar que sea único en la lista

def validar_nombre_solicitante(valor:str):
    if len(valor)>=5 and valor.isalpha():
        return True
    return False

def validar_tipo_sala(valor):
    if valor in ('P','M','G'):
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
    
# --------------

def buscar_reserva(reservas,codigo_reserva):
    for posicion in range(len(reservas)):
        if codigo_reserva[posicion]["codigo_reserva"] == codigo_reserva:
            return posicion
        return -1

def agregar_reserva(reservas):
    while True:
        codigo_reserva = input("Ingrese el código de reserva: ")
        if not validar_codigo_reserva:
            print("Error, código inválido")
            continue
        if buscar_reserva(reservas, codigo_reserva) == -1:
            print("Error, el código ya fue registrado")
            continue
        break
    
# 3.    CONDICION DE ACTUALIZACION

def actualizar_confirmaciones(reservas:list):
    pass