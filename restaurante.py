# 7. Restaurante “El Sabor Colombiano” — Menú + bebida opcional + IVA

#Precios
menu = 12000
bebida = 3000
menuConBebida = menu + bebida

#Iva
iva = 0.8
ivaMenu = menu * iva
ivaMenuBebida = menuConBebida * iva

#Totales con iva
totalMenu = menu + ivaMenu
totalMenuBebida = menuConBebida + ivaMenuBebida

print("Bienvenido al 'El Sabor Colombiano'")
print("Menú del día por valor de $12.000")
decision = int(input("""Desea adicionar bebida por un valor adicional de $3.000?
                     1. Si
                     2. No
                     ---> """))

if decision == 1:
    print(f"Gracias por su compra, total a pagar: {totalMenuBebida}")
    
elif decision == 2:
    print(f"Gracias por su compra, total a pagar: {totalMenu}")
    
else:
    print("Valor no válido")