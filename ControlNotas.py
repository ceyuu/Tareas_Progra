notas = {
"Pedro": 5.5,
"María": 6.2,
"Juan": 4.8,
"Ana": 7.0
}

def validar_nota(nota):
    if nota >= 4.0:
        return "Aprobado"
    return "Reprobado"

def solicitar_nombre(notas:dict):
    nombre = input("Ingrese su nombre: ").title().strip()
    if nombre in notas:
        nota = notas[nombre]
        notita = validar_nota(nota)
        print(f"La nota de {nombre} es {nota}")
        print(f"Estado del alumno: {notita}")
        return 
    print("Alumno no encontrado")

nombre = solicitar_nombre(notas)