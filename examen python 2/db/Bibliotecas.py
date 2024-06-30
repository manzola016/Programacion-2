import os
import pyodbc

menu = {
    1 : 'Nombre',
    2 : 'Ubicacion',
    3 : 'Todos los campos'
}

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def añadir(connection):
    try:
        cursor = connection.cursor()
        id = None
        while id == None:
            id = input('Ingrese el ID de la biblioteca: ')
            if not id.isdigit():
                input('Solo puede ingresar numeros. Presione ENTER para continuar...')
                id = None
                continue
        id = int(id)
        nombre = input('Ingrese el nombre de la biblioteca: ')
        ubicacion = input('Ingrese la ubicacion de la biblioteca: ')
        cursor.execute('INSERT INTO Bibliotecas (BibliotecaID, Nombre, Ubicacion) VALUES (?, ?, ?)', id, nombre, ubicacion)
        connection.commit()
        input('Biblioteca añadida. Precione ENTER para continuar...')
    except pyodbc.Error as err:
        print(f'Error: {err}')
        cursor.close()
        input('Presione ENTER para continuar...')
    
def leer(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT BibliotecaID, Nombre, Ubicacion FROM Bibliotecas')
        bibliotecas = cursor.fetchall()
        for i in bibliotecas:
            print(f'ID: {i[0]} - Nombre: {i[1]} - Ubicacion: {i[2]}')
        input('Presione ENTER para continuar...')
    except pyodbc.Error as err:
        print(f'Error: {err}')
        cursor.close()
        input('Presione ENTER para continuar...')
    
def actualizar(connection):
    try:
        cursor = connection.cursor()
        id = None
        while id == None:
            id = input('Ingrese el ID de la biblioteca: ')
            if not id.isdigit():
                input('Solo puede ingresar numeros. Presione ENTER para continuar...')
                id = None
                continue
        id = int(id)
        clear()
        res = None
        while res == None:
            print('ACTUALIZAR\n* * * * * *')
            for key, value in menu.items():
                print(f'{key} - {value}')
            res = input('Ingrese una opcion: ')
            if not res.isdigit():
                input('Solo puede ingresar numeros. Presione ENTER para continuar...')
                res = None
                continue 
            res = int(res)
            if not res in menu.keys():
                input('Ingrese una opcion valida. Precione ENTER para continuar...')
                resp = None
                continue
        match res:
            case 1:
                clear()
                nombre = input('Ingrese el nuevo nombre: ')
                query = 'UPDATE Bibliotecas SET Nombre = ? WHERE BibliotecaID = ?'
                cursor.execute(query, nombre, id)
                input('Nombre actualizado. Presione ENTER para continuar...')
            case 2:
                clear()
                ubicacion = input('Ingrese la nueva ubicacion: ')
                query = 'UPDATE Bibliotecas SET Ubicacion = ? WHERE BibliotecaID = ?'
                cursor.execute(query, ubicacion, id)
                input('Ubicacion actualizada. Presione ENTER para continuar...')
            case 3:
                clear()
                nombre = input('Ingrese el nuevo nombre: ')
                ubicacion = input('Ingrese la nueva ubicacion: ')
                query = 'UPDATE Bibliotecas SET Nombre = ?, Ubicacion = ? WHERE BibliotecaID = ?'
                cursor.execute(query, nombre, ubicacion, id)
                input('Campos actualizados. Presione ENTER para continuar...')
        connection.commit()
    except pyodbc.Error as err:
        print(f'Error: {err}')
        cursor.close()
        input('Presione ENTER para continuar...')
        
def eliminar(connection):
    try:
        cursor = connection.cursor()
        id = None
        while id == None:
            id = input('Ingrese el ID de la biblioteca: ')
            if not id.isdigit():
                input('Solo puede ingresar numeros. Presione ENTER para continuar...')
                id = None
                continue
        id = int(id)
        cursor.execute(f'DELETE FROM Bibliotecas WHERE BibliotecaID = {id}')
        connection.commit()
        input('Biblioteca eliminada. Presione ENTER para continuar...')
    except pyodbc.Error as err:
        print(f'Error: {err}')
        cursor.close()
        input('Presione ENTER para continuar...')