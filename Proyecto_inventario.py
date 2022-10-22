
from ast import For
import pandas as pd
import csv

def main():
    df = pd.read_csv(r'inventario1.csv', nrows=200)
    v = pd.read_csv(r'vendedor1.csv', nrows=200)

    while True:
        pregunta_inicio = input('\n ¿Desea acceder al programa? si/no: ')
        if pregunta_inicio != 'no':
            num = Menu()
            if num == 1:                
                registrar_ventas(df,v)
            elif num == 2:
                articulos_nuevos(df,v)
            elif num == 3:
                datos_inventario(df,v)
            elif num == 4:
                datos_ventas(df,v) 
            elif num == 5:
                actualizar_articulos_vendedor(df,v)
            else:
                break 

        else:
            print('\nSalir\n')
            break

def Menu():
    print('''
    1) Registrar ventas
    2) Registrar llegada de artículos al almacén
    3) Consultar datos del inventario
    4) Consultar datos de las ventas
    5) Actualizar artículos del vendedor
    6) salir
    ''')
    num = int(input('Elija la opción que desee consultar: '))
    return num

def registrar_ventas(df,v):
    print(f'\n{v.iloc[:,:]}')
    num = int(input(f'\nDame un numero del 0 al 3: '))

    if num == 0:
        print(f'\n{df.iloc[:5,:5]}')
        articulo = int(input('dame el id del producto que vendió: '))
        cantidad_nueva = int(input('Dame la nueva cantidad del producto: '))
        if cantidad_nueva > df.iat[articulo,2]:
            print('Error, no existe esa cantidad en el inventario. ')
        else:
            try:
                df.iat[articulo,4] = cantidad_nueva
                df.to_csv('/Users/ximixsm/Documents/PRIMER SEMESTRE/Programación/inventario1.csv', index=False)
            except KeyError:
                pass
            print(f'\n{df.iloc[:5,:5]}')

    elif num == 1:
        print(f'\n{df.iloc[5:10,:5]}')
        articulo = int(input('dame el id del producto que vendió: '))
        cantidad_nueva = int(input('Dame la nueva cantidad del producto: '))
        if cantidad_nueva > df.iat[articulo,2]:
            print('Error, no existe esa cantidad en el inventario. ')
        else:
            try:
                df.iat[articulo,4] = cantidad_nueva
                df.to_csv('/Users/ximixsm/Documents/PRIMER SEMESTRE/Programación/inventario1.csv', index=False)
            except KeyError:
                pass
            print(f'\n{df.iloc[5:10,:5]}')

    elif num == 2:
        print(f'\n{df.iloc[10:15,:5]}')
        articulo = int(input('dame el id del producto que vendió: '))
        cantidad_nueva = int(input('Dame la nueva cantidad del producto: '))
        if cantidad_nueva > df.iat[articulo,2]:
            print('Error, no existe esa cantidad en el inventario. ')
        else:
            try:
                df.iat[articulo,4] = cantidad_nueva
                df.to_csv('/Users/ximixsm/Documents/PRIMER SEMESTRE/Programación/inventario1.csv', index=False)
            except KeyError:
                pass
            print(f'\n{df.iloc[10:15,:5]}')

    elif num == 3:
        print(f'\n{df.iloc[15:20,:5]}') 
        articulo = int(input('dame el id del producto que vendió: '))
        cantidad_nueva = int(input('Dame la nueva cantidad del producto: '))
        if cantidad_nueva > df.iat[articulo,2]:
            print('Error, no existe esa cantidad en el inventario. ')
        else:
            try:
                df.iat[articulo,4] = cantidad_nueva
                df.to_csv('/Users/ximixsm/Documents/PRIMER SEMESTRE/Programación/inventario1.csv', index=False)
            except KeyError:
                pass   
            print(f'\n{df.iloc[15:20,:5]}')
    return df

def datos_inventario(df,v):
    print(df)
    return df

def articulos_nuevos(df,v):
    print('POR FAVOR, TEN EN CUENTA QUE SI EL PRODUCTO QUE SE ESTÁ\nAGREGANDO Y YA EXISTE AUTOMÁTICAMENTE SE ELIMINARÁ')
    nombre = input('Dame el nombre del artículo que deseas agregar: ')
    cantidad = input('Dame la cantidad del articulo que agregaste: ')
    precio = input('Dame el precio individual del articulo: ')
    codigo = input('Dame el codigo de identificacion del articulo: ')
   

    df = df.append({
        'Código producto': codigo,
        'Nombre del artículo': nombre,
        'Cantidad': cantidad,
        'Precio individual': precio,
        'ventas x art': 0
        }, ignore_index=True)
    df.duplicated(subset=['Nombre del artículo'])
    df = df.drop_duplicates(subset=['Nombre del artículo'])
    df.to_csv('/Users/ximixsm/Documents/PRIMER SEMESTRE/Programación/inventario1.csv', index=None)
    return df

def datos_inventario(df,v):
    print(df)
    return df

def datos_ventas(df,v):
    print(f'\n{df.iloc[:,1:5]}')
    return df

def actualizar_articulos_vendedor(df,v):
    suma1 = 0
    suma2 = 0
    suma3 = 0
    suma4 = 0
    print('\nEste es el dataframe de los vendedores anterior')
    print(f'\n{v.iloc[:,:]}')
    for i in range(0,5):
        suma1 += df.iat[i,4]
    v.iat[0,1] += suma1

    for i in range(5,10):
        suma2 += df.iat[i,4]
    v.iat[1,1] += suma2

    for i in range(10,15):
        suma3 += df.iat[i,4]
    v.iat[2,1] += suma3

    for i in range(15,20):
        suma4 += df.iat[i,4]
    v.iat[3,1] += suma4

    print('\nEste es el dataframe de los vendedores actualizado')
    print(f'\n{v.iloc[:,:]}')
    df.to_csv('/Users/ximixsm/Documents/PRIMER SEMESTRE/Programación/inventario1.csv', index=None)
    return df


if __name__ == '__main__':
    main()

#:D