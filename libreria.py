print("Bienvenido a su librería 'el saber'")

#Precio libro
libro = 25000

#Descuento de estudiantes
descEst = 0.15

#Descuento con cupon
cupon = "LIBRO10"
descCup = 0.10

esEstudiante = input("¿Es un estudiante? 1. Si   2. No      ")

while esEstudiante not in ("1","2"):
    esEstudiante = input("Opción no válida, debe ingresar 1 o 2 ----> ")


cantidadLibros = int(input("Ingrese la cantidad de libros a comprar: "))
while cantidadLibros <=0:
    cantidadLibros = int(input("Opción no válida, debe ingresar 1 o 2 ----> "))

total = libro * cantidadLibros

if esEstudiante == 1:
    total = total - (total * descEst)
    tieneCupon = input("¿Tiene un cupon para redimir? 1. Si    2. No   ")
    if tieneCupon == "1":
        cuponEst = input("Ingrese su cupon: ")
        if cuponEst == cupon:
            total = total -(total * descCup)
        else:
            print(f"Cupon ingresado '{cuponEst}' no válido,")
            
print("Total a pagar: ", total)