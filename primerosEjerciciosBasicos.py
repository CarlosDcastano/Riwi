
"""Librería El Saber"""

# print("Bienvenido a su librería 'el saber'")

# #Precio libro
# libro = 25000

# #Descuento de estudiantes
# descEst = 0.15

# #Descuento con cupon
# cupon = "LIBRO10"
# descCup = 0.10

# esEstudiante = input("¿Es un estudiante? 1. Si   2. No      ")

# while esEstudiante not in ("1","2"):
#     esEstudiante = input("Opción no válida, debe ingresar 1 o 2 ----> ")


# cantidadLibros = int(input("Ingrese la cantidad de libros a comprar: "))
# while cantidadLibros <=0:
#     cantidadLibros = int(input("Opción no válida, debe ingresar 1 o 2 ----> "))

# total = libro * cantidadLibros

# if esEstudiante == 1:
#     total = total - (total * descEst)
#     tieneCupon = input("¿Tiene un cupon para redimir? 1. Si    2. No   ")
#     if tieneCupon == "1":
#         cuponEst = input("Ingrese su cupon: ")
#         if cuponEst == cupon:
#             total = total -(total * descCup)
#         else:
#             print(f"Cupon ingresado '{cuponEst}' no válido,")
            
# print("Total a pagar: ", total)

"""Moda todal"""

# "Bienvenido a prenda total"

# prendas = {"camisa" : 20000,
#          "pantalon" : 34000,
#          "sudadera" : 18000,
#          "pantaloneta" : 17000,
#          "camisilla" : 12000,
#          "boxers" : 10000,
#          "brasier" : 18000         
#          }

# total = 0
# cont = "1"

# while cont == "1":   
#         prenda = input("ingrese la prenda a registrar para la venta: ").lower()
#         while prenda not in prendas:
#             prenda = input(f"Producto no encontrado. Ingrese un producto disponible en la lista {prendas}").lower()
#         total += prendas[prenda]
#         print("Total actual: $", total)
#         cont = (input("Desea ingresar más productos? \nSi: 1 \n No: 'Cualquier otra tecla' \n ---->"))
        
        
# print(total)


"""6. Parqueadero “RapidCar” — Tarifa escalonada """
# while True:
#     hora = 2000

#     cantHoras = int(input("Ingrese la cantidad de horas: "))
#     total = hora * cantHoras
#     multa = 5000

#     while cantHoras < 0:
#         print("No se acepta un valor negativo")
#         cantHoras = int(input("Ingrese la cantidad de horas: "))

#     if cantHoras in range(5):
#         if cantHoras == 0:
#             total = hora
#         print(f"Total a pagar: {total}")

#     else:
#         print(f"Total a pagar: {total + multa}")
#         break


"""7. Restaurante “El Sabor Colombiano” — Menú + bebida opcional + IVA"""

# #Precios
# menu = 12000
# bebida = 3000
# menuConBebida = menu + bebida

# #Iva
# iva = 0.08
# ivaMenu = menu * iva
# ivaMenuBebida = menuConBebida * iva

# #Totales con iva
# totalMenu = menu + ivaMenu
# totalMenuBebida = menuConBebida + ivaMenuBebida

# print("Bienvenido al 'El Sabor Colombiano'")
# print("Menú del día por valor de $12.000")
# decision = int(input("""Desea adicionar bebida por un valor adicional de $3.000?
#                      1. Si
#                      2. No
#                      ---> """))

# if decision == 1:
#     print(f"Gracias por su compra, total a pagar: {totalMenuBebida}")
    
# elif decision == 2:
#     print(f"Gracias por su compra, total a pagar: {totalMenu}")
    
# else:
#     print("Valor no válido")


"""Supermercado “AhorroMax” — Descuentos y envío"""

# producto = 2000
# envio = 5000

# #Descuentos. >10= desc1   >30 = desc2
# desc1 = 0.05
# desc2 = 0.15


# cantidad = int(input("Ingrese la cantidad de productos a llevar: "))

# while cantidad <=0:
#     print("Error, debe ingresar valores positivos")
#     cantidad = int(input("Ingrese la cantidad de productos a llevar: "))


    
# if cantidad < 10:
#     total = cantidad * producto

# elif cantidad < 30:
#     total = cantidad * (producto-(desc1 * producto))
    

# else:
#     total = cantidad * (producto-(desc2 * producto))

# if total < 50000:
#     total += envio

# print(total)  


"""TecnoPlus"""

# pruebaTecnica = float(input("Ingrese la nota de la prueba técnica: "))

# while (pruebaTecnica <0 or pruebaTecnica >5):
#     print("Error, los valores a ingresar deben estar entre 0 y 5, intenta de nuevo")
#     pruebaTecnica = float(input("Ingrese la nota de la prueba técnica: "))
    
    
# pruebaLogica = float(input("Ingrese la nota de la prueba lógica: "))

# while (pruebaLogica <0 or pruebaLogica >5):
#     print("Error, los valores a ingresar deben estar entre 0 y 5, intenta de nuevo")
#     pruebaLogica = float(input("Ingrese la nota de la prueba lógica: "))
    
# notaFinal = (pruebaTecnica * 0.7) + (pruebaLogica * 0.3)

# if notaFinal >= 3:
#     print("Aprobado ", notaFinal)
# elif notaFinal >=2 and notaFinal <3:
#     print("Revision ", notaFinal)
# else:
#     print("Reprobado ", notaFinal)


""" Sabores y precios:

chocolate → $4.000
vainilla → $3.500

Opcional: topping cuesta $1.000.

Si el usuario ingresa un sabor que no existe, mostrar "Sabor no disponible".
Si el sabor es válido, preguntar si quiere topping y calcular total."""

# while True:    
#     sabores = {"chocolate" : 4000,
#                "fresa": 2500,
#                "mandarina": 3800,
#                "limon": 5200}

#     topping = 1000

#     sabor = input(f"Por favor ingrese el sabor a elegir, tenemos: {sabores} ----> ").lower()

#     while sabor not in sabores:
#         sabor = input(f"Sabor no disponible, tenemos: {sabores} Por favor escriba solo uno de los sabores disponibles: ----> ").lower()
    
#     add = input(f"Quiere añadir topping vor valor de {topping}? \n Escriba Si o No \n ----> ").lower()
#     while add not in ("si", "no"):
#         add = input(f"{add} No es una respuesta aceptable. Escriba Si o No \n ----> ").lower()

#     total = sabores[sabor]

#     if add == "no":

#         print(f"Total a pagar: {total}")

#     else:
#         total += topping
#         print(f"Gracias por su compra, total a pagar {total}")

"""Club Noche Estelar"""

# while True:
#     try:
#         edad = int(input("Ingrese su edad: "))
#         if edad < 0:
#             print("Debe ingresar un número entero positivo")
#         else:
#             break
        
#     except ValueError:
#         print("Ingrese un tipo de dato correcto, número entero posivito")

# if edad < 18:
#     print("No puede ingresar")

# else:
#     while True:
#         try:
#             doc = input("¿Tiene documento de identificación? \nSi \nNo \nEscriba su respuesta ---> ").lower()
#             if doc not in ("si", "no"):
#                 print("Debe ingresar si o no, no se aceptan otras respuestas")
#             else:
#                 break
#         except ValueError:
#             print("Debe ingresar si o no, no se aceptan otras respuestas")
        
# if doc == "no":
#         print("No puede ingresar")
# else:
#         print("Puede ingresar")
    