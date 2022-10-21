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
                artículos_nuevos(df)
            elif num == 3:
                datos_inventario(df)
            elif num == 4:
                datos_ventas(df) 
            elif num == 5:
                ventas_vendedor(df)

        else:
            print('\nSalir\n')
            break

def Menu():
    print('''
    1) Registrar ventas
    2) Registrar llegada de artículos al almacén
    3) Consultar datos del inventario
    4) Consultar datos de las ventas
    5) Mostrar reportes de ventas por vendedor o por artículo
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
    return

def datos_inventario(df):
    print(df)


    return df

if __name__ == '__main__':
    main()
    
