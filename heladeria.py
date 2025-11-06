# Sabores y precios:

#     chocolate → $4.000
#     vainilla → $3.500

# Opcional: topping cuesta $1.000.

# Si el usuario ingresa un sabor que no existe, mostrar "Sabor no disponible".
# Si el sabor es válido, preguntar si quiere topping y calcular total.

while True:
    
    print("Heladería “Frosty” — Sabor y topping")

    print("1. Chocolate")
    print("2. Vainilla")

    opcion = (input("Ingrese el número correspondiente al sabor que desea comprar: "))



    valorCho = 4000
    valorVa = 3500
    valorTop = 1000
    
    print(f"Desea incluir topping por valor de ${valorTop}?")
    print("1. Si")
    print("2. no")
    add = input("Ingrese su respuesta")

    if opcion == "1":
        if add == "1":
            print(f"Disfruta tu helado de chocolate con topping, total a pagar {valorCho + valorTop}")
        else:
            print(f"Disfruta tu helado de chocolate por valor de {valorCho}")


    elif opcion == "2":
        if add == "1":
            print(f"Disfruta tu helado de vainilla con topping, total a pagar {valorVa + valorTop}")
        else:
            print(f"Disfruta tu helado de vainilla por valor de {valorVa}")

    else:
        print("No hay sabores diferentes a chocolate o vainilla")