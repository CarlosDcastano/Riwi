




opciones = ("1", "2", "3", "4")
opcion = ""
while opcion not in opciones:
    print("MENÚ DE OPCIONES")
    print("1. Agregar producto. \n2. Mostrar inventario. \n3. Calcular estadísticas. \n4. Salir")
    opcion = input("Seleccione la opción a realizar")
    if opcion not in opciones:
        print("Debe ingresar un valor numérico y debe estar dentro de las opciones indicadas")
    elif opcion == "1":
        print("agregar_producto()")
    elif opcion == "2":
        print("mostrar_inventario()")
    elif opcion == "3":
        print("calcularEstadisticas()")
    else:
        print("Hasta luego")
        break        
 
 
    
    