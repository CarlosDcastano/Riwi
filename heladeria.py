# Sabores y precios:

#     chocolate → $4.000
#     vainilla → $3.500

# Opcional: topping cuesta $1.000.

# Si el usuario ingresa un sabor que no existe, mostrar "Sabor no disponible".
# Si el sabor es válido, preguntar si quiere topping y calcular total.
while True:    
    sabores = {"chocolate" : 4000,
               "fresa": 2500,
               "mandarina": 3800,
               "limon": 5200}

    topping = 1000

    sabor = input(f"Por favor ingrese el sabor a elegir, tenemos: {sabores} ----> ").lower()

    while sabor not in sabores:
        sabor = input(f"Sabor no disponible, tenemos: {sabores} Por favor escriba solo uno de los sabores disponibles: ----> ").lower()
    
    add = input(f"Quiere añadir topping vor valor de {topping}? \n Escriba Si o No \n ----> ").lower()
    while add not in ("si", "no"):
        add = input(f"{add} No es una respuesta aceptable. Escriba Si o No \n ----> ").lower()

    total = sabores[sabor]

    if add == "no":

        print(f"Total a pagar: {total}")

    else:
        total += topping
        print(f"Gracias por su compra, total a pagar {total}")

