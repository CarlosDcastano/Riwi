#INVENTARIO


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
        print("Valor inválido, ingrese un número entero positivo.") # Si la cantidad ingresada no es dígito, envía mensaje de error y sigue en el bucle
costo_total = precio * cantidad   # En la variable costo total guardo el resultado de multiplicar precio por cantidad
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")


"""El programa contiene 3 ciclos while, cada uno de ellos para asegurar que el usuario ingresa el tipo de dato correcto para cada dato solicitado.

1/ Dentro del primer ciclo se le pide al usuario por medio de la función input() que ingrese el nombre, para luego validar si lo ingresado
es un dígito o si está vacío, en tal caso, muestra un mensaje de error y se continúa en el ciclo, si no se presenta ninguno de estos casos,
se ingresa al else,lo cual rompe el ciclo

2/En el segundo ciclo, se solicita con input() al usuario que ingrese el precio, una vez ingresado, se crea un condicional que valida por medio de
la función .replace() que el valor ingresado solo tenga un punto decimal y además que sea dígito con .isdigit(), si es así, se ingresa a otro if
que valide si lo ingresado es menor o igual a 0, si lo es, muestra mensaje de advertencia y continúa en el ciclo, si no lo es, rompe el ciclo.
Si por otro lado, no es dígito o tiene más de un punto decimal, muestra valor inválido y continúa en el ciclo.

3/ En el último ciclo while, se solicita de nuevo con input() que se ingrese la cantidad y solo se valida si es dígito, si lo es, se convierte el valor
a entero y se rompe el ciclo, si no es dígito, sino cualquier otro tipo de dato, muestra mensaje de error y continúa en el ciclo.

Finalmente, se crea una variable llamada costo_total, donde se almacena el resultado de multiplicar el precio por la cantidad y se usa un
print() final para mostrar todos los valores"""




