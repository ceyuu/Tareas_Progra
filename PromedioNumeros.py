lista =[]

def solicitud_numero(lista:list):
    for n in range(1,5+1):
        while True:
            try:
                numero = int(input(f"Ingrese un número entero {n}: "))
                lista.append(numero)
                break
            except:
                print("Ingresa un número entero")
    return lista

listita = solicitud_numero(lista)
suma = sum(listita)
largo= len(listita)
promedio = suma/largo

print(f"Lista: {listita}")
print(f"la suma de todos los números ingresados es: {suma}")
print(f"El promedio es: {int(promedio)}")