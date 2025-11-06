#INVENTARIO

#Creamos un ciclo while infinito para que se repita este bloque de código hasta que haya un break.
while True:

    nombre = input("Ingrese el nombre del producto: ")

    while True:
        try: 
            precio = float(input("Ingrese el precio del producto: "))
            if precio <= 0:
                print("El valor no puede ser 0 o negativo, intente de nuevo")
            else:
                break

        except ValueError:
            print("Valor inválido, ingrese un valor correcto para continuar")


    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de productos que lleva el cliente: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa, intente de nuevo")
            else:
                break
        except ValueError:
            print("Valor inválido, ingrese un valor correcto para continuar")

    costo_total = precio * cantidad

    print(f"Producto: {nombre}| Precio: {precio}| Cantidad: {cantidad}| Total: {costo_total}")
    
    decision = input("¿Desea continuar? Si:1     No:2 --------->")
    
    if decision == "1":
        continue
    else:
        print("Fin del programa")
        break
    

        

