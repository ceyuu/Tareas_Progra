inventario = {
"Laptop": 10,
"Mouse": 25,
"Teclado": 15
}

def menu_inventario(inventario:dict):
    print(inventario)

def solicitar_producto(inventario:dict):
    producto = input("Ingrese un producto: ").title().strip()
    if producto in inventario:
        stock = inventario[producto]
        print(f"Producto: {producto} - stock: {stock}")
        return producto
    print("Producto no encontrado")

def solicitar_cantidad(producto):
    cantidad = int(input("Ingrese cantidad a vender: "))
    if cantidad <= inventario[producto]:
        inventario[producto] -= cantidad
        print("Venta realizada")
        print(f"{producto}: {inventario[producto]} unidades")
        
inventarito = menu_inventario(inventario)
producto = solicitar_producto(inventario)
cantidad = solicitar_cantidad(producto)