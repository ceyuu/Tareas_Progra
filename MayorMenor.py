lista =[]

def solicitud_numero(lista:list):
    for n in range(1,8+1):
        while True:
            try:
                numero = int(input(f"Ingrese un número entero {n}: "))
                lista.append(numero)
                break
            except:
                print("Ingresa un número entero")
    return lista

lista2 = solicitud_numero(lista)
lista2.sort() # MENOR A MAYOR
print(f"El número menor ingresado es: {lista2[0]}")
lista2.sort(reverse=True) # MAYOR A MENOR
print(f"El número mayor ingresado es: {lista2[0]}")

print("La cantidad de elementos ingresados es 8")