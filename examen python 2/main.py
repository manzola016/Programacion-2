
# MANUEL ANZOLA - 32666091

import os
from db.connection import *
from db.Bibliotecas import *

SERVER = 'DESKTOP-J0LTP9S\SQLEXPRESS'
DATABASE = 'Escuela'
TABLE = 'Bibliotecas'

menu = {
    1 : 'Añadir',
    2 : 'Leer',
    3 : 'Actualizar',
    4 : 'Eliminar'
}

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def main():
    try:
        connection = conectar(SERVER, DATABASE)
        cursor = connection.cursor()
        opc = None
        while opc == None:
            clear()
            print(f'BIBLIOTECA\n* * * * * * * * * * * * * * * * * * * * * * *\nBASE DE DATOS: {DATABASE} | TABLA: {TABLE}')
            for key, value in menu.items():
                print(f'{key} - {value}')
            opc = input('Ingrese una opcion: ')
            if not opc.isdigit():
                input('Solo puede ingresar numeros. Presione ENTER para continuar...')
                opc = None
                continue 
            opc = int(opc)
            if not opc in menu.keys():
                input('Ingrese una opcion valida. Precione ENTER para continuar...')
                opc = None
                continue    
            match opc:
                case 1:
                    clear()
                    añadir(connection)
                    opc = None
                case 2:
                    clear()
                    leer(connection)
                    opc = None
                case 3:
                    clear()
                    actualizar(connection)
                    opc = None
                case 4:
                    clear()
                    eliminar(connection)
                    opc = None
    except pyodbc.Error as err:
        print(f'Error: {err}')
        cursor.close()
        input('Presione ENTER para continuar...')
if __name__ == '__main__':
    main()