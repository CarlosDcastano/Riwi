"""1) Restaurante “Menú Dinámico” — Agregar plato del día
Como chef, quiero una función agregar_plato(menu, plato) que valide que plato no esté vacío y lo agregue a la lista menu.

Si el plato ya existe, mostrar “plato duplicado”.
Recorre el menú al final para imprimirlo numerado.
Sugerencia: usa list.append()."""      

# def agregar_plato(menu, plato):
    
#     if not plato:
#         "El plato está vacío"
#     elif plato.isdigit():
#         "Debe agregar un valor válido"
#     else:
#         if plato in menu:
#             print("Plato duplicado")
#         else:
#             menu.append(plato)
#         i = 0   
#         for plato in menu:
#             print(f"Plato número {i+1}: {plato}")
#             i += 1
    
        
        
# menu = []       
# while True:
    
#     plato = input("Ingrese el nombre del plato")
#     agregar_plato(menu, plato)
    
"""2) Teatro “Butacas VIP” — Insertar reserva en posición
Como encargado de reservas, quiero una función insertar_reserva(butacas, nombre, posicion) que valide
que posicion esté en rango y ubique la reserva en esa posición.

Si la posición no es válida, no inserta y muestra error.
Luego, recorre la lista para confirmar el orden.
Sugerencia: usa list.insert()."""