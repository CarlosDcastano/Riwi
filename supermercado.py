# Supermercado “AhorroMax” — Descuentos y envío

producto = 2000
envio = 5000

#Descuentos. >10= desc1   >30 = desc2
desc1 = 0.05
desc2 = 0.15


cantidad = int(input("Ingrese la cantidad de productos a llevar: "))

while cantidad <=0:
    print("Error, debe ingresar valores positivos")
    cantidad = int(input("Ingrese la cantidad de productos a llevar: "))


    
if cantidad < 10:
    total = cantidad * producto

elif cantidad < 30:
    total = cantidad * (producto-(desc1 * producto))
    

else:
    total = cantidad * (producto-(desc2 * producto))

if total < 50000:
    total += envio

print(total)  

    
    



