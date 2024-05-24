import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

detalles = {}
inventario = {}
opci = {
    1 : "Cantidad",
    2 : "Precio"
}

def añadir_producto():
    clear()
    producto = input('Ingrese el nombre del producto: ')
    precio = None
    while precio == None:
        precio = input('Ingrese el precio del producto: ')
        if not precio.isdigit():
            input('Solo puede ingresar numeros\nPresione ENTER para continuar...')
            precio = None
            continue
    precio = int(precio)
    cantidad = None
    while cantidad == None:
        cantidad = input('Ingrese la cantidad del producto: ')
        if not cantidad.isdigit():
            input('Solo puede ingresar numeros\nPresione ENTER para continuar...')
            cantidad = None
            continue
    cantidad = int(cantidad)
    detalles = {
        "Producto" : producto,
        "Precio" : precio,
        "Cantidad" : cantidad
    }
    inventario[producto] = detalles
    input('Producto agregado exitosamente\nPresione ENTER para continuar...')
    
def actualizar_producto():
    clear()
    producto = None
    while producto == None:
        producto = input('Ingrese el nombre del producto: ')
        if not producto in inventario.keys():
            input('Producto inexistente\nPresione ENTER para continuar...')
            producto = None
            continue
    opc = None
    while opc == None:
        for key, value in opci.items():
            print(f'{key} - {value}')
        opc = input('Ingrese una opcion: ')
        if not opc.isdigit():
            input('Solo puede ingresar numeros\nPresione ENTER para continuar...')
            opc = None
            continue
        opc = int(opc)
        if not opc in opci.keys():
            input('Ingrese una opcion valida\nPresione ENTER para continuar...')
            opc = None
            continue   
    match opc:
        case 1:
            clear()
            if producto in inventario.keys():
                detalles = inventario[producto]
                cantidad = None
                while cantidad == None:
                    cantidad = input('Ingrese la nueva cantidad: ')
                    if not cantidad.isdigit():
                        input('Solo puede ingresar numeros\nPresione ENTER para continuar...')
                        cantidad = None
                        continue
                    detalles["Cantidad"] = cantidad
            input('Cantidad actualizada\nPresione ENTER para continuar...')
        case 2:
            clear()
            if producto in inventario.keys():
                detalles = inventario[producto]
                precio = None
                while precio == None:
                    precio = input('Ingrese el nuevo precio: ')
                    if not precio.isdigit():
                        input('Solo puede ingresar numeros\nPresione ENTER para continuar...')
                        precio = None
                        continue
                    detalles["Precio"] = precio
            input('Precio actializado\nPresione ENTER para continuar...')
    
def mostrar_inventario():
    clear()
    for key, value in inventario.items():
        print(value)
    input('Presione ENTER para continuar...')

def buscar_producto():
    clear()
    producto = input('Ingrese el nombre del producto: ')
    inventario.get(producto, 'Producto no encontrado')
    print(inventario[producto])
    input('Presione ENTER para continuar...')
    
def eliminar_producto():
    clear()
    producto = None
    while producto == None:
        producto = input('Ingrese el nombre del producto: ')
        if not producto in inventario.keys():
            input('Producto inexistente\nPresione ENTER para continuar...')
            producto = None
            continue
    if producto in inventario.keys():
        inventario.pop(producto)
    input('Producto eliminado\nPresione ENTER para continuar...')