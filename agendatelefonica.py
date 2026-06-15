# AGENDA TELEFONICA


def validacion_nombre():
    while True:
        nombre = input(f"Ingrese el nombre del usuario {y}: ")
        if not nombre.isalpha():
            print("Error, el nombre no debe contener carácteres especiales ni números")
        elif len(nombre)==0:
            print("Error! El nombre no debe estar vacío")
        else:
            return nombre

def validacion_telefono():
    while True:
        try:
            telefono = int(input(f"Ingrese el telefono de persona {y}: "))
            largo = len(str(abs(telefono))) 
            if largo <= 8:
                print("Error! El teléfono debe ser real")
            else:
                return telefono
        except ValueError:
            print("Error! Debe ingresar un número entero")

agenda = {}
for y in range(1,4):
    nombre = validacion_nombre()
    telefono = validacion_telefono()

    agenda[nombre] = telefono

for k in agenda:
    print(f"{k} -> {agenda[k]}")