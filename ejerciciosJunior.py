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
Si llega o supera 100 → mostrar “Meta diaria alcanzada”."""

# litros = 0
# total = 0
# while total < 100:
#     litros = int(input("Ingrese la cantidad de litros para esta venta: "))
#     total += litros
#     if total < 100:
# 	    print(f"{total} litros, sigue vendiendo")
# else:
# 	print(f"{total} litros. Meta diaria alcanzada")

"""17. Panadería “Don Pancho” – Producción diaria
Como panadero, quiero usar un for del 1 al 12.
Si el número es 6, mostrar “Mitad de la producción completada”.
Si es 12, mostrar “¡Día finalizado!”."""

# for i in range(1, 13):
#     if i == 6:
#         print(f"{i} Mitad de la producción completada")
#     elif i == 12:
#         print(f"{i} ¡Día finalizado!")
#     else:
#         print(f"{i}: Producción en curso")

"""18. Academia de inglés – Repetición de palabras
Como estudiante, quiero ingresar una palabra y usar un for para repetirla 5 veces.
Si el contador es impar, mostrar la palabra en minúsculas.
Si es par, mostrarla en mayúsculas."""

# palabra = input("Ingrese una plalabra: ")

# for i in range(1,6):
#     if i % 2 == 0:
#         print(palabra.upper())
#     else:
#         print(palabra.lower())

"""19. Tienda de helados – Registro de clientes atendidos
Como empleado, quiero usar un while que cuente clientes hasta que el número supere 15.
Si el número es múltiplo de 5, mostrar “Pausa para limpieza”.
Al final, mostrar “Turno finalizado”."""

# clientes = 1

# while clientes <=15:
#     if clientes %5 == 0:
#         print(f"Cliente: {clientes}, Pausa para limpieza.")
#     else:
#         print(f"Cliente: {clientes} atendido.")
#     clientes +=1
# else: 
#     print("Turno finalizado")

"""20. Aplicación “Inicio Seguro” – Intentos de inicio de sesión
Como usuario, quiero usar un while con máximo 3 intentos de contraseña.
Si acierto, mostrar “Acceso permitido”.
Si agoto los intentos, mostrar “Acceso denegado”."""

# contraseñaCorrecta = "123"
# contraseñaUsuario = ""
# contador = 0

# while contraseñaUsuario != contraseñaCorrecta or contador <= 3:
#     contraseñaUsuario = input("Ingrese la contraseña")
#     contador +=1
# else:
#     print("Acceso permitido")

# contraseñaCorrecta = "123"
# contraseñaUsuario = ""
# intentos = 0

# while intentos <3:
#     contraseñaUsuario = input("Ingrese la contraseña: ")
#     if contraseñaUsuario == contraseñaCorrecta:
#         print("Acceso permitido")
#         break
#     intentos +=1
# else:
#     print("Acceso denegado")


"""21. Tienda “FuncionaShop” – Mensaje de bienvenida
Como dueño de la tienda, quiero crear una función llamada saludo() que imprima “Bienvenido a FuncionaShop”.
Luego, quiero llamarla desde el programa principal."""

# def saludo():
#     print("Bienvenido a FuncionaShop")

# saludo()

"""22. Gimnasio “StrongFit” – Cálculo de energía
Como entrenador, quiero una función calcularEnergia() que reciba un número de repeticiones y devuelva un mensaje:

Si las repeticiones son menores de 5 → “Necesitas más esfuerzo”.
Si son 5 o más → “¡Buen trabajo!”."""

# def calcularEnergia(a):
#     if a < 5:
#         print("Necesitas más esfuerzo")
#     else:
#         print("Buen trabajo")

# energia = int(input("Ingrese el número de repeticiones realizadas: "))
# calcularEnergia(energia)


"""23. Banco “LoopBank” – Simulación de intereses
Como analista financiero, quiero una función calcularInteres() que reciba un monto y una tasa (porcentaje) 
y retorne el valor final después de aplicar el interés una vez.
El programa principal debe pedir los datos y mostrar el resultado."""

# def calcularInteres(monto, tasa):
#     interes = monto * (tasa / 100)
#     valorFinal = monto + interes
#     return valorFinal

# monto = float(input("Ingrese el monto: "))
# tasa = float(input("Ingrese la tasa de interés (en %): "))
# resultado = calcularInteres(monto, tasa)
# print(f"El valor final después de aplicar el interés es: {resultado}")

"""24. Escuela “Aprende con Funciones” – Promedio de notas
Como profesor, quiero crear una función promedioNotas() que reciba tres notas y calcule el promedio.
Si el promedio es mayor o igual a 3.0, mostrar “Aprobado”; si no, “Reprobado”."""

# def promedioNotas(a,b,c):
#     prom = (a+b+c) / 3  
#     if prom >= 3.0:
#         print("aprobado")
#     else:
#         print("reprobado")

# promedioNotas(-1,2,3)	
# promedioNotas(-5,1,3)

"""25. Restaurante “BuenaFunción” – Verificación de turno
Como gerente, quiero una función verificarTurno(hora) que determine:

Si la hora es menor que 12 → “Turno de mañana”.
Si está entre 12 y 18 → “Turno de tarde”.
Si es mayor → “Turno de noche”.
El programa principal debe pedir la hora e imprimir el resultado."""

# def verificarTurno(hora):
# 	if hora >0 and hora <12:
# 		print("Turno de mañana")
# 	elif hora >=12 and hora <= 18:
# 		print("Turno de tarde")
# 	else:
# 		print("Turno de noche")

# hora = int(input("Ingrese hora: "))
# verificarTurno(hora)