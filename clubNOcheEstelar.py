while True:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad < 0:
            print("Debe ingresar un número entero positivo")
        else:
            break
        
    except ValueError:
        print("Ingrese un tipo de dato correcto, número entero posivito")

if edad < 18:
    print("No puede ingresar")

else:
    while True:
        try:
            doc = input("¿Tiene documento de identificación? \nSi \nNo \nEscriba su respuesta ---> ").lower()
            if doc not in ("si", "no"):
                print("Debe ingresar si o no, no se aceptan otras respuestas")
            else:
                break
        except ValueError:
            print("Debe ingresar si o no, no se aceptan otras respuestas")
        
if doc == "no":
        print("No puede ingresar")
else:
        print("Puede ingresar")