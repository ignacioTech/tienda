
#Practico Integrador CRUD de productos
productos = []
#Menu
while True :
    print("")
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
        opcion = int(input("Ingrese una opción del 1 - 6 || 0(cero) para salir "))

        if opcion == 0:
            print("Salir")
            break

        elif opcion == 1:
            print("1-Registro-")
            print("")
            registro = False
            while registro == False:
                try:
                    nombre = input("Ingrese Nombre o 0 (Cero) para ir al menú anterior ")
                    if nombre == "0":
                        break
                    else:
                        while registro == False:
                            try:
                                cantidad = int(input("Ingrese Cantidad - 0 (cero) para volver al menu anterior "))
                                if cantidad == 0:
                                    break
                                else:
                                    while registro == False:
                                        try:
                                            precio = float(input("Ingrese Precio  - 0 (cero) para volver al menu anterior "))
                                            if precio == 0:
                                                break
                                            else:
                                                producto = [nombre, cantidad, precio]
                                                try: 
                                                    confirmacion = input("Confirma el ingreso del precio? s/n ")

                                                    if confirmacion.lower() == "s":
                                                        productos.append(producto)
                                                        print("El producto: ", producto, " Ha ingresado al stock ")
                                                        registro = True
                    
                                                except ValueError:
                                                    print("Ingreso no valido")
                                        except ValueError:
                                            print("Ingreso no valido")
                            except ValueError:
                                print("Ingreso no valido")
                except ValueError:
                    print("Ingreso no valido")
                try:
                    seguir = input("desea ingresar otro producto? s/n ")
                    
                    if seguir.lower() == "s":
                        registro = False 
                except ValueError:
                    print("Ingreso no valido")

        elif opcion == 2:
            print("2-Visualizacion-")
            
        elif opcion == 3:
            print("3-Actualizacion-")
        elif opcion == 4:
            print("4-Eliminacion-")
        elif opcion == 5:
            print("5-Listado-")
            print("")
            for producto in productos:
                print(producto)
        elif opcion == 6:
            print("6-Reporte Bajo Stock-")
        else:
            print("Ingrese un valor valido entre  1 - 6 || 0(cero) para salir ")
    except ValueError:
        print("ingrese un valor numerico valido")
