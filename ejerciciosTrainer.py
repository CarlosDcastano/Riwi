"""1. Cafetería “Buen Café” – Control de tazas servidas
Como barista, quiero usar un bucle for para mostrar cuántas tazas he servido del 1 al 10, 
pero si el número es 5, mostrar el mensaje “¡Mitad del turno completada!"""

# for i in range(1,11):
#     if i == 5:
#         print(5," mitad del turno completado")
#     else:
#         print(f"Llevas {i} tazas")

# #Con while
# tazas = 1

# while tazas <= 10:
#     if tazas == 5:
#         print(f"{tazas} Mitad del turno completado")
#     else:
#         print(f"Llevas {tazas} tazas")
#     tazas += 1

"""2. Cine “La Estrella” – Cuenta regresiva antes de iniciar la función
Como proyeccionista, quiero mostrar una cuenta regresiva del 5 al 1 usando for. 
Si llega al número 1, debe imprimir “¡Que empiece la función!"""

# for i in range(5, 0, -1):
#     if i ==1:
#         print(i,"¡Que empiece la función!")
#     else:
#         print(i)

"""3. Gimnasio “Solo Leveling Fit” – Motivación diaria
Como entrenador, quiero usar un while que repita 5 veces el mensaje “¡Tú puedes lograrlo!”, 
pero en la última repetición muestre “¡Excelente trabajo, terminaste!”."""

# repita = 1
# while repita < 5:    
#     print("¡Tú puedes lograrlo!")
#     repita += 1
# else: 
#     print("¡Excelente trabajo, terminaste!")

"""4. Tienda “Descuento Express” – Clientes atendidos
Como cajero, quiero usar un for que muestre “Atendiendo cliente número X” del 1 al 8. 
Si el cliente es el número 8, mostrar “Último cliente del día”."""

# for i in range (1,9):
#     if i == 8:
#         print(i,"Último cliente del día")
#     else:
#         print(f"Atendiendo cliente número {i}")

"""5. Escuela “Aprende Más” – Registro de tareas entregadas
Como profesor, quiero usar un while que sume tareas hasta 10. 
Si el contador llega a 10, mostrar “¡Todas las tareas recibidas!”. 
Si aún no llega, mostrar cuántas faltan."""

# tarea = 1
# while tarea <10:
#     falta = 10 - tarea  
#     print(f"Tarea {tarea} entregada. Faltan {falta} tareas")
#     tarea += 1
# else: 
#     print("¡Todas las tareas recibidas!")


"""6. Fábrica “LoopTech” – Control de producción
Como supervisor, quiero que un for muestre los productos fabricados del 1 al número que indique el usuario.
Si el número es par, mostrar “Producto verificado”.
Si es impar, mostrar “Producto pendiente”."""

# tope = int(input("Ingrese el tope de productos fabricados: "))

# for i in range(1, tope+1):
#     if i % 2 == 0:
#         print(i, "Producto verificado")
#     else:
#         print(i, "Producto pendiente")

"""7. Restaurante “Buen Sabor” – Revisión de limpieza.
Como jefe de cocina, quiero usar un for para repetir 3 veces el mensaje “Limpia tu estación”.
Si es la última vez, mostrar “¡Revisión completada!”."""

# for i in range (1, 4):
#     if i < 3:
#         print("“Limpia tu estación”")

#     else: 
#         print("¡Revisión completada!")

"""8. Academia de baile – Calentamiento previo
Como instructor, quiero usar un while para contar del 1 al 5.
Si el número es menor que 5, mostrar “Sigue calentando...”, y si llega a 5, mostrar “¡Listo para bailar!”."""

# cont = 1

# while cont < 5:
#     print(cont, "Sigue calentando")
#     cont += 1
# else:
#     print("Listo para bailar")

"""9. Concurso “Adivina el número secreto”
Como participante, quiero que el programa me pida un número entre 1 y 5 usando un while.
Si acierto, mostrar “¡Correcto!”.
Si no, mostrar “Intenta otra vez” y seguir hasta acertar."""

# secreto = 4
# numeroParticipante = int(input("Ingresa tu número: "))

# while numeroParticipante != secreto:
#     numeroParticipante = int(input("Incorrecto, ingresa otro número: "))

# else: 
#     print("Correcto!")

"""10. Taller “Mecánica Pro” – Revisiones del día
Como mecánico, quiero usar un for que muestre “Revisión X”.
Si X es igual a 3, mostrar “Revisión especial de motor”."""


# for x in range(1,4):
#     if x != 3:
#         print("Revision X")
#     else: 
#         print("Revisión especial de motor")
