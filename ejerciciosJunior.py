"""11. Banco “PythonBank” – Simulación de ahorro mensual
Como cliente, quiero usar un for que sume mi ahorro mensual durante 6 meses.
Si en algún mes el total supera $1,000,000, mostrar “¡Meta alcanzada!”.
Al final, mostrar el total acumulado."""

# ahorro = 0


# for i in range(1, 7):
#     ahorroCliente = int(input(f"Mes {i} Ingrese valor: "))
#     if ahorroCliente > 1000000:
#         print("Meta mensual alcanzada")
#     ahorro += ahorroCliente

# print("Su total ahorrado es de: $",ahorro)


"""12. Gimnasio “Level Up” – Control de repeticiones
Como deportista, quiero ingresar un número de repeticiones y usar un for para imprimir “Repetición X completada”.
Si X es divisible por 3, mostrar además “¡Excelente ritmo!”."""


# repeticiones = int(input("Ingrese el número de repeticiones: "))

# for i in range(1, repeticiones +1):
#     if i % 3 == 0:
#         print(f"Repetición {i} completada ¡Excelente ritmo!")
#     else:
#         print(f"Repetición {i} completada")


"""13. Parqueadero “AutoLoop” – Control de vehículos
Como vigilante, quiero usar un while que cuente vehículos hasta llegar a 20.
Si entra un número par, mostrar “Vehículo par registrado”.
Si el total llega a 20, mostrar “Capacidad completa”."""

# vehiculo = 1

# while vehiculo <= 20:
#     if vehiculo % 2 == 0:
#         print(vehiculo, "Vehículo par registrado")
#     else:
#         print(vehiculo)
#     vehiculo +=1
# else: 
#     print("Capacidad completa")

"""14. Tienda “Ahorra Más” – Caja registradora básica
Como cajero, quiero pedir montos de venta hasta que el usuario escriba 0.
Si la venta supera $100,000, mostrar “Venta destacada”.
Al final, mostrar el total vendido."""

# venta = 1
# total = 0

# while venta != 0:
#     venta = int(input("Ingrese el valor de la venta: "))
#     if venta > 100000:
#         print("Venta destacada")
#     total += venta
# else:
#     print(total)


"""15. Academia “CodeStart” – Contador de ejercicios completados
Como estudiante, quiero usar un for del 1 al número que indique.
Si el número es múltiplo de 5, mostrar “¡Gran avance!”.
Si no, solo mostrar “Ejercicio X completado”."""

# ejCompletos = int(input("Ingrese el número de ejercicios: "))

# for i in range(1, ejCompletos + 1):
#     if i % 5 == 0:
#         print(f"{i} Gran avance")
#     else:
#         print(f"Ejercicio {i} completado")

"""16. Gasolinera “LoopFuel” – Control de litros vendidos
Como operador, quiero usar un while que sume litros hasta superar 100.
Cada vez que se venda una cantidad, verificar:

    Si el total aún es menor que 100 → mostrar “Sigue vendiendo”.
    Si llega o supera 100 → mostrar “Meta diaria alcanzada”.

"""

# litros = 0

# while litros < 100:
#     litros = int(input("Ingrese la cantidad de litros"))
    
    
lista = []

while True:
    nombre = input("Ingrese su nombre")
    lista.append(nombre)
    print(lista)
    
