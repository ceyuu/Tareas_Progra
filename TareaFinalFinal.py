# Cada prestamo deberá almacenarse como un registro independiente. un diccionario

prestamos = []

def mostrar_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Registrar préstamo")
    print("2. Buscar préstamo")
    print("3. Eliminar préstamo")
    print("4. Actualizar seguimiento")
    print("5. Mostrar préstamos")
    print("6. Salir")

def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción (1-6): "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Error, opción inválida, debe ser un número entre 1-6")
        except:
            print("Error, debe ingresar un número entero")

def mostracion_prestamos(lista):
    if not lista:
        print("No hay prestamos registrados aún")
        return
    for prestamos in lista:
        print("Código del préstamo:" ,prestamos["codigo_prestamo"])
        print("Titulo del libro:"    ,prestamos["titulo_libro"])
        print("Categoría:"           ,prestamos["categoria"])
        print("Días de préstamo:"    ,prestamos["dias_prestamo"])
        print("Multa pendiente:"     ,prestamos["multa_pendiente"])
        print("Seguimiento:"         ,prestamos["seguimiento"])

# Buscando buscando
# Se busca por el código
def el_busquedas(valor, lista):
    for posicion, prestamo in enumerate(lista):
        if prestamo["codigo_prestamo"] == valor:
            return posicion
    return -1

# Eliminar préstamo
# DEBE apoyarse en la función de búsqueda
def eliminar_prestamo(lista):
    codigo = input("Ingrese el código del préstamo que desea eliminar: ")
    posicion = el_busquedas(codigo,lista)
    if posicion!= -1:
        lista.pop(posicion)
        print("Préstamo aniquilado (¬_¬'')")
    else:
        print("Préstamo no encontrado")


# VALIDACIONES
def validar_codigo_prestamo(valor,lista):
    if len(valor) == 0:
        return False, "Error, debe ingresar un código"
    elif valor[0]!= "P":
        return False, "Error, el código debe comenzar con la letra 'P'"
    elif len(valor)!=6 or " " in valor:
        return False, "Error, el código debe tener exactamente 6 caracteres y no debe contener espacios"
    
    for prestamo in lista:
        if prestamo["codigo_prestamo"]==valor:
            return False, "Error, código ya registrado"
    return True, ""

def validar_titulo_libro(valor):
    if len(valor)<5:
        return False, "Error, el título debe tener al menos 5 carácteres"
    solo_numeritos = True
    for caracter in valor:
        if not caracter.isdigit():
            solo_numeritos = False
    if solo_numeritos==True:
        return False, "Error, el título del libro no debe estar compuesto solo por números"
    return True, ""

def validar_categoria(valor):
    if len(valor) == 0:
        return False, "Error, debe ingresar una categoría"
    if valor[0].upper() not in ("A","L","C"):
        return False, "Error, la categoría debe ser: Académico, Literatura o Ciencia"
    return True, ""

def validar_dias_prestamo(valor):
    if len(valor) == 0:
        return False, "Error, debe ingresar un número"
    try:
        dias = int(valor)
        if dias<1 or dias>30:
            return False, "Error, debe ingresar un número entre 1 y 30"
        return True, ""
    except:
        return False, "Error, debe ingresar un número"

def validar_multa_pendiente(valor):
    if len(valor) == 0:
        return False, "Error, debe ingresar un número"
    try:
        multa = int(valor)
        if multa < 0:
            return False, "Error, debe ingresar un número mayor o igual a 0"
        return True, ""
    except:
        return False, "Error, debe ingresar un número"
    

# Registro de préstamo 
def registro_prestamo(lista):
    while True:
        codigo = input("Ingrese el código del préstamo: ")
        validacion, mensajito = validar_codigo_prestamo(codigo, prestamos)
        if validacion:
            break
        else:
            print(mensajito)
    
    while True:
        titulo_libro = input("Ingrese título del libro: ")
        validacion, mensajito = validar_titulo_libro(titulo_libro)
        if validacion:
            break
        else:
            print(mensajito)

    while True:
        categoria = input("Ingrese categoría: ")
        validacion, mensajito = validar_categoria(categoria)
        if validacion:
            break
        else:
            print(mensajito)

    while True:
        dias_prestamo = input("ingrese los días de préstamo: ")
        validacion, mensajito = validar_dias_prestamo(dias_prestamo)
        if validacion:
            break
        else:
            print(mensajito)

    while True:
        multa_pendiente = input("Ingrese el valor de su multa pendiente: ")
        validacion, mensajito = validar_multa_pendiente(multa_pendiente)
        if validacion:
            break
        else:
            print(mensajito)

    prestamo = {
        "codigo_prestamo" : codigo,
        "titulo_libro" : titulo_libro,
        "categoria" : categoria,
        "dias_prestamo" : int(dias_prestamo),
        "multa_pendiente" : int(multa_pendiente),
        "seguimiento" : False
    }

    prestamos.append(prestamo)
    print("Préstamo registrado exitosamente ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧")

# actualización de seguimiento:
def actualizacion_seguimiento(lista):
    if len(lista) == 0:
        print("No hay préstamos registrados aún")
        return
    for prestamo in lista:
        if prestamo["multa_pendiente"] >= 5000:
            prestamo["seguimiento"] = True
        else:
            prestamo["seguimiento"] = False
    print("Préstamos actualizados correctamente!")

while True:
    mostrar_menu()
    opc = validar_opcion()
    if opc==1:
        registro_prestamo(prestamos)
    elif opc==2:
        codigo_a_buscar = input("Ingrese el código del préstamo que desea buscar: ")
        posicion = el_busquedas(codigo_a_buscar, prestamos)
        if posicion == -1:
            print("Error, préstamo inexistente")
        else:
            print(f"El préstamo se encuentra en la posición {posicion} de la lista")
    elif opc==3:
        eliminar_prestamo(prestamos)
    elif opc==4:
        actualizacion_seguimiento(prestamos)
    elif opc==5:
        mostracion_prestamos(prestamos)
    elif opc==6:
        print("Sayonara")
        break