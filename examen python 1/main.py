
# MANUEL ANZOLA - 32666091

import os
import paquetes.utilidades as utilidades

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

menu = {
    1 : "Agrear producto",
    2 : "Actualizar producto",
    3 : "Mostrar inventario completo",
    4 : "Buscar producto",
    5 : "Eliminar producto"
}

def main():
    opc = None
    while opc == None:
        clear()
        print('SISTEMA DE GESTION DE INVENTARIO\n* * * * * * * * *')
        for key, value in menu.items():
            print(f'{key} - {value}')
        opc = input('Ingrese una opcion: ')
        if not opc.isdigit():
            input('Solo puede ingresar numeros\nPresione ENTER para continuar...')
            opc = None
            continue
        opc = int(opc)
        if not opc in menu.keys():
            input('Ingrese una opcion valida\nPresione ENTER para continuar...')
            opc = None
            continue
        match opc:
            case 1:
                utilidades.añadir_producto()
                opc = None
            case 2:
                utilidades.actualizar_producto()
                opc = None
            case 3:
                utilidades.mostrar_inventario()
                opc = None
            case 4:
                utilidades.buscar_producto()
                opc = None
            case 5:
                utilidades.eliminar_producto()
                opc = None
main()