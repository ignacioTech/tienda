
#Practico Integrador CRUD de productos
productos = []
#Menu
while True :
    print("Gestion de Productos")
    print("")
    print("1- Registro: Ingreso de Productos")
    print("2- Visualización: Consulta de Productos")
    print("3- Actualizacion: Modificacion de Productos")
    print("4- Eliminacion: dar de baja un Producto")
    print("5- Listado: Listado completo de los productos de la base de datos")
    print("6- Reporte de Bajo Stock: Listado de productos con cantidad bajo mínimo")
    print("0- Salir")

    #PROCESO ENTRADA OPCIONES
    try:
        opcion = int(input("Ingrese una opción del 1 - 6 || 0(cero) para salir"))

        if opcion == 0:
            print("Salir")
            break
        elif opcion == 1:
            print("1-Registro-")
        elif opcion == 2:
            print("2-Visualizacion-")
        elif opcion == 3:
            print("3-Actualizacion-")
        elif opcion == 4:
            print("4-Eliminacion-")
        elif opcion == 5:
            print("5-Listado-")
        elif opcion == 6:
            print("6-Reporte Bajo Stock-")
        else:
            print("Ingrese un valor valido entre  1 - 6 || 0(cero) para salir ")
    except ValueError:
        print("ingrese un valor numerico valido")
