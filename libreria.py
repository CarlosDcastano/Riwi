print("Bienvenido a su librería 'el saber'")

esEstudiante = input("¿Es un estudiante? 1. Si   2. No      ")

libro = 25000
cantidadLibros = int(input("Ingrese la cantidad de libros a comprar: "))
total = libro * cantidadLibros

#Descuento de estudiantes
descEst = 0.15

#Descuento con cupon
cupon = "LIBRO10"
descCup = 0.10

if esEstudiante == "2":
    total = total

elif esEstudiante == "1":
    total = total - (total * descEst)
    tieneCupon = input("¿Tiene un cupon para redimir? 1. Si    2. No   ")
    if tieneCupon == "1":
        cuponEst = input("Ingrese su cupon: ")
        if cuponEst == cupon:
            total = total -(total * descCup)
        else:
            print(f"Cupon ingresado '{cuponEst}' no válido,")

else:
    print("Opción no válida")

print(total)