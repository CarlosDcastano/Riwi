

######################## Función Agregar Producto ########################

def agregar_producto(lista):
    producto = {}
    while True:
        totalProducto = input("ingrese el total de los productos a registrar")
        if totalProducto.isdigit():
            totalProducto = int(totalProducto)
            break
        else:
            print("Ingrese un número entero")
    
    for i in range(1, totalProducto+1):
        while True:   #Validar nombre (Se repetirá mientras no haya un break en alguna de las condiciones.)
            nombre = input("Ingresa nombre del producto: ")    # Solicito el nombre al usuario
            if nombre.isdigit() or nombre == "":  # Si el nombre es un dígito o si está vacío
                print("Debe ingresar un nombre válido") # Envía mensaje de error y continúa en el ciclo
            else:
                break  # Si No es dígito ni está vacío, rompa el ciclo.
            
            
        while True:       # Validar precio. (Se repetirá mientras no haya un break en alguna de las condiciones.)
            precio_input = input("Ingrese el precio del producto: ")    # Solicito el precio al usuario
            if precio_input.replace('.', '', 1).isdigit(): # Verifico si el precio es un número válido (acepto decimales), pero debe ser dígito
                precio = float(precio_input) # Convierto precio a float
                if precio <= 0:
                    print("El valor no puede ser 0 o negativo, intente de nuevo.")
                else:
                    break
            else:
                print("Valor inválido, ingrese un número válido.")
        while True:     # Validar cantidad (solo enteros) (Se repetirá mientras no haya un break en alguna de las condiciones.)
            cantidad_input = input("Ingrese la cantidad de productos que lleva el cliente: ") #Solicito la cantidad al usuario
            if cantidad_input.isdigit():   # Valido si la cantidad ingresada es dígito, 
                cantidad = int(cantidad_input) # Si es dígito, convierta el String a entero
                break #Rompa el ciclo
            else:
                print("Valor inválido, ingrese un número entero positivo.")
        producto = {
                    "nombre" : nombre,
                    "precio": precio,
                    "cantidad": cantidad
                   }
        lista.append(producto)
        
    return lista

################## Función Mostrar inventario#######################

def mostrar_inventario(lista):
    if not lista:
        print(f"{lista} está vacío")
    else:
        for producto in lista:
            print(f"producto: {producto["nombre"]} | precio: {producto["precio"]} | Cantidad: {producto["cantidad"]}")
    
        
def calcular_estadisticas(lista):
    if not lista:
        print(f"{lista} está vacío")   
    else:
        cant = 0
        total = 0
        for producto in lista:
            cant += 1
            total += producto["precio"] * producto["cantidad"]
        print("El valor total a pagar por los productos es: ", total )
        print(f"La cantidad total de productos es {cant}")
            
            
   
        
############################## Menú #################################3

inventario = []  
while True:
    print("MENÚ DE OPCIONES")
    print("1. Agregar producto. \n2. Mostrar inventario. \n3. Calcular estadísticas. \n4. Salir")
    opcion = input("Seleccione la opción a realizar: ")
    if opcion not in ("1", "2","3","4"):
        print("Debe ingresar un valor numérico y debe estar dentro de las opciones indicadas")
    elif opcion == "1":
        agregar_producto(inventario)
    elif opcion == "2":
        mostrar_inventario(inventario)
    elif opcion == "3":
        calcular_estadisticas(inventario)
    else:
        print("Hasta luego")
        break        


    
    
    
    
    
    
    
    


  