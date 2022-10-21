import pandas as pd
import csv

def main():
    df= pd.read_csv(r'/home/m0lm0s/Descargas/Code/Proyecto_inventario/inventario1.csv', nrows=200)
    while True:
        pregunta_inicio = input('\n ¿Desea acceder al programa? si/no: ')
        if pregunta_inicio != 'no':
            num = Menu()
            if num == 1:                
                registrar_ventas(df)
            elif num == 2:
                articulos_nuevos(df)
            elif num == 3:
                datos_inventario(df)
            elif num == 4:
                datos_ventas(df) 
            elif num == 5:
                actualizar_articulos_vendedor(df)

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

def registrar_ventas(df):
    print(f'\n{df.iloc[:4,6:]}')
    num = int(input(f'\nDame un numero del 0 al 3: '))

    if num == 0:
        print(f'\n{df.iloc[:5,:5]}')
        articulo = int(input('dame el id del producto que vendió: '))
        cantidad_nueva = int(input('Dame la nueva cantidad del producto: '))
        try:
            df.iat[articulo,4] = cantidad_nueva
            df.to_csv('/home/m0lm0s/Descargas/Code/Proyecto_inventario/inventario1.csv', index=False)
        except KeyError:
            pass
        print(f'\n{df.iloc[:5,:5]}')

    elif num == 1:
        print(f'\n{df.iloc[5:10,:5]}')
        articulo = int(input('dame el id del producto que vendió: '))
        cantidad_nueva = int(input('Dame la nueva cantidad del producto: '))
        try:
            df.iat[articulo,4] = cantidad_nueva
            df.to_csv('/home/m0lm0s/Descargas/Code/Proyecto_inventario/inventario1.csv', index=False)
        except KeyError:
            pass
        print(f'\n{df.iloc[5:10,:5]}')

    elif num == 2:
        print(f'\n{df.iloc[10:15,:5]}')
        articulo = int(input('dame el id del producto que vendió: '))
        cantidad_nueva = int(input('Dame la nueva cantidad del producto: '))
        try:
            df.iat[articulo,4] = cantidad_nueva
            df.to_csv('/home/m0lm0s/Descargas/inventario1.csv', index=False)
        except KeyError:
            pass
        print(f'\n{df.iloc[10:15,:5]}')

    elif num == 3:
        print(f'\n{df.iloc[15:20,:5]}') 
        articulo = int(input('dame el id del producto que vendió: '))
        cantidad_nueva = int(input('Dame la nueva cantidad del producto: '))
        try:
            df.iat[articulo,4] = cantidad_nueva
            df.to_csv('/home/m0lm0s/Descargas/inventario1.csv', index=False)
        except KeyError:
            pass   
        print(f'\n{df.iloc[15:20,:5]}')

def datos_inventario(df):
    print(df)

def articulos_nuevos(df):
    nombre = input('Dame el nombre del articulo que deseas agregar: ')
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
    df.to_csv('/home/m0lm0s/Descargas/inventario1.csv', index=None)
    return df

def datos_inventario(df):
    print(df)

def datos_ventas(df):
     print(f'\n{df.iloc[:,1:5]}')

def actualizar_articulos_vendedor(df):
    suma1 = 0
    suma2 = 0
    suma3 = 0
    suma4 = 0
    print('\nEste es el dataframe de los vendedores anterior')
    print(f'\n{df.iloc[:4,6:]}')
    for i in range(0,5):
        suma1 += df.iat[i,4]
    df.iat[0,7] += suma1

    for i in range(5,10):
        suma2 += df.iat[i,4]
    df.iat[1,7] += suma2

    for i in range(10,15):
        suma3 += df.iat[i,4]
    df.iat[2,7] += suma3

    for i in range(15,20):
        suma4 += df.iat[i,4]
    df.iat[3,7] += suma4

    print('\nEste es el dataframe de los vendedores actualizado')
    print(f'\n{df.iloc[:4,6:]}')
    df.to_csv('/home/m0lm0s/Descargas/inventario1.csv', index=None)



if __name__ == '__main__':
    main()
    
