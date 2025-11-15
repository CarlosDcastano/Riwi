"""1. Restaurante “Buen Sabor” – Cálculo de propina
Como mesero, quiero una función calcular_propina(total_cuenta) 
que reciba el valor total de la cuenta y calcule la propina del 10%.
Si el total es mayor de $100.000, aplicar el 15%.
El programa debe mostrar el total final a pagar."""

# def calcular_propina(total_cuenta):
#     prop = 0.90
#     desc = 0.85
#     total_cuenta *= prop 
#     if total_cuenta > 100000:
#         total_cuenta *= desc
#         return total_cuenta
#     else:
#         return total_cuenta
    
# total = int(input("Ingrese el total: "))

# print(calcular_propina(total))

"""2. Gimnasio “Level Up” – Control de repeticiones
Como entrenador, quiero una función repeticiones(n) 
que use un bucle for para mostrar las repeticiones del 1 al número indicado.
Si el número actual es par, mostrar “Excelente forma”, 
si no, “Mantén el ritmo”."""

# def repeticiones(n):
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             print("Excelente forma")
#         print("Mantén el ritmo")

# n = int(input("Ingrese el número de repeticiones deseadas: "))

# repeticiones(n)


"""3. Tienda “LoopShop” – Descuentos acumulados
Como vendedor, quiero una función aplicar_descuentos() que pida varios 
precios hasta que el usuario escriba 0.
Si el precio supera 50.000, aplicar 10% de descuento.
Al final, mostrar la suma total de las compras con descuento."""


# def aplicar_descuento():
#     precio = 1
#     total = 0
#     desc = 0.90
#     while precio != 0:
#         precio = int(input("Ingrese el precio: "))
#         if precio > 50000:
#             precio *= desc
#         total +=precio
#         print(f"Hasta ahora van {total}")
#     else:
#         print(f"Su total es {total}")
        
# aplicar_descuento()

"""4. Banco “PythonBank” – Evaluador de crédito
Como asesor financiero, quiero una función evaluar_credito(ingresos, edad) que:

Apruebe el crédito si los ingresos son mayores de 2 millones
y la edad está entre 25 y 60.
Si no cumple, mostrar “Crédito rechazado”.
Usar condicionales dentro de la función.
"""

# def evaluar_credito(ingresos, edad):
#     if ingresos < 2000000 or edad not in range(25, 61):
#         print("Crédito rechazado")
#     else:
#         print("Crédito aprobado")

# ingresos = int(input("Ingrese los ingresos mensuales: "))
# edad = int(input("Ingrese la edad: "))
# evaluar_credito(ingresos, edad)

"""5. Escuela “Aprende Más” – Promedio de notas
Como profesor, quiero una función promedio_notas() 
que reciba tres notas y calcule el promedio.
Si el promedio es mayor o igual a 3.0 → mostrar “Aprobado”, 
de lo contrario “Reprobado”.
Debe repetirse para varios estudiantes usando un while."""



# def promedio_notas(a,b,c):
#         prom = (a+b+c) / 3
#         if prom >= 3.0:
#             return "Aprobado"
#         else:
#             return "Reprobado"


# estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
# i = 1

# while i <= estudiantes:
#     nota1 = int(input(f"Ingrese la nota 1 para el estudiante {i}: "))
#     nota2 = int(input(f"Ingrese la nota 2 para el estudiante {i}: "))
#     nota3 = int(input(f"Ingrese la nota 3 para el estudiante {i}: "))
#     print(promedio_notas(nota1,nota2,nota3))
#     i +=1

"""6. Estación “LoopBus” – Simulador de pasajeros
Como conductor, quiero una función simular_viaje(pasajeros) 
que recorra con un for cada pasajero y muestre “Pasajero X a bordo”.
Si llega a 10 pasajeros, mostrar “Bus lleno” y detener el bucle."""

# def simular_viaje(pasajeros):
#     for i in range (1, pasajeros):
#         if i >= 10:
#             print("Bus lleno")
#             break
#         else:
#             print(f"Pasajero {i} a bordo")
        
        
# pasajeros = int(input("Ingrese la cantidad de pasajeros: "))

# simular_viaje(pasajeros)
            
            
"""7. Panadería “Don Pancho” – Control de producción diaria
Como panadero, quiero una función hornear_pan(lotes) que use un for 
para indicar qué lote se está horneando.
Si el lote es divisible por 3, mostrar “Verificación de calidad”.
Al final, mostrar “Producción terminada”.""" 
    
# def hornear_pan(lotes):
#     for lote in range(1, lotes+1):
#         if lote % 3 == 0:
#             print(f"lote {lote} Verificación de calidad")
#         else:
#             print(f"Se está horneando el lote {lote}")
#     print("Producción terminada")
    
    
# lotes = int(input("Ingrese la cantidad de lotes: "))

# hornear_pan(lotes)

"""Como cajero, quiero una función calcular_entradas() que pida 
edades de los clientes hasta que se ingrese 0.
Aplicar precio:

    Menores de 12 → $5.000
    De 12 a 59 → $8.000
    Mayores de 60 → $4.000
    Usar un while y condiciones.
"""

# def calcular_entradas():
#     edad = int(input("Ingrese la edad, o ingrese 0 para salir: "))
#     while edad != 0:
        
#         if edad < 0:
#             print("Edad no válida")
#         elif edad < 12:
#             print("$5.000")
#         elif edad < 60:
#             print("$8.000")
#         else:
#             print("$4.000")
#         edad = int(input("Ingrese la edad, o ingrese 0 para salir: "))

# calcular_entradas()

"""9. Tienda “EnergyStore” – Simulador de puntos
Como cliente, quiero una función calcular_puntos(compras) que use un for 
para recorrer la cantidad de compras (ingresada por el usuario).
Si el número de compra es múltiplo de 3, agregar 10 puntos; en caso 
contrario, agregar 5.
Al final, mostrar los puntos totales."""

# def calcular_puntos(compras):
#     puntos = 0
#     for i in range(1, compras):
#         if i %3 == 0:
#             puntos += 10
            
#         else:
#             puntos += 5
            
#     return puntos
        
# compras = int(input("Ingrese la cantidad de compras: "))

# print(calcular_puntos(compras))
            

"""10. Academia “CodeStart” – Tabla de multiplicar personalizada
Como estudiante, quiero una función tabla_multiplicar(numero) que use un for para mostrar la tabla del número dado hasta el 10.
Si el resultado es mayor de 50, mostrar también “Resultado alto”."""

# def tabla_multiplicar(numero):
#     for i in range(1, 11):
#         total = i * numero
#         if total > 50:
#             print(f"{numero} X {i} = {total} Resultado alto")
#         else:
#             print(f"{numero} X {i} = {total}")

# numero = int(input("Ingrese un número para hacer la tabla de dicho número hasta el 10: "))

# tabla_multiplicar(numero)

"""11. Aerolínea “FlyLoop” – Cálculo de millas acumuladas
Como viajero frecuente, quiero una función calcular_millas(viajes) que reciba
el número de viajes realizados y sume millas según la distancia:

Viaje corto (< 1000 km): 500 millas
Medio (1000–3000 km): 1000 millas
Largo (> 3000 km): 2000 millas
Debe repetirse hasta que el usuario escriba “fin” y mostrar el total acumulado."""

def calcular_millas(viajes):
    #Millas
    corto = 500
    medio = 1000
    largo = 2000
    #Input
    
    
    #Contador
    cont = 0
    i = 1
    while i <= viajes:
        millas = input("Ingrese la cantidad de km recorridos (O escriba fin para terminar)")
        
        if millas.lower() == "fin":
            print(f"Por {i} viajes, total millas acumuladas: {cont}")
            break
        
        else:
            millas = int(millas)
            if millas in range (0,1001):
                print(f"Ganaste {corto} millas")
                cont += corto
            elif millas in range(1000, 3001):
                print(f"Ganaste {medio} millas")
                cont += medio
            elif millas > 3000:
                print(f"Ganaste {largo} millas")
                cont += largo
    else: 
        print(f"Por {viajes} viajes, total millas acumuladas: {cont}")
        
# viajes = int(input("Ingrese la cantidad de viajes realizados"))

# calcular_millas(viajes)


"""12. Hospital “Salud Total” – Evaluador de signos vitales
Como médico, quiero una función evaluar_paciente() que reciba frecuencia cardiaca y temperatura corporal.
Si ambos valores están fuera del rango normal (FC > 100 o Temp > 38), mostrar “Paciente en observación”.
Repetir el proceso con varios pacientes en un bucle while."""

# def evaluar_paciente(fC, tC):
#     if fC > 100 or tC > 38:
#         print("Paciente en observación")
#     else:
#         print("Ta bien")

# cantidad_pacientes = int(input("Ingrese la cantidad de pacientes a evaluar"))

# i = 1
# while i <= cantidad_pacientes:
#     print(f"paciente {i}")
#     fC = int(input("Ingrese la frecuencia cardiaca"))
#     tC = int(input("Ingrese la temperatura corporal"))
#     evaluar_paciente(fC, tC)
#     i +=1
    
"""13. Tienda Online “ShopMaster” – Carrito de compras con validaciones
Como comprador, quiero una función carrito() que permita ingresar precios de productos y valide:

Si el precio es negativo, mostrar error y pedir otro valor.
Si el precio es mayor a 100.000, aplicar un 20% de descuento.
Usar while y if dentro de la función hasta ingresar 0 para finalizar."""

# def carrito():
#     desc = 0.20
#     while True:
#         precio = input("Ingrese el precio del producto")
#         if not precio.replace('.', '', 1).isdigit():
#             print(f"{precio} No es un valor aceptado, debe ingresar solo números")
#         else:
#             if precio == "0":
#                 print("Adios")
#                 break
#             else:
#                 precio = float(precio)
#                 if precio > 100000:
#                     precio -= precio * desc
#                 print("Total a pagar", precio)
                    
                
# carrito()

"""14. Academia “DevLoop” – Calculadora de factoriales
Como estudiante de programación, quiero una función calcular_factorial(numero) que use un bucle for para calcular el factorial del número.
Si el número ingresado es negativo, mostrar “Número inválido”.
De lo contrario, mostrar el resultado."""

# def calcular_factorial(numero):
#     numero = str(numero)
#     if not numero.isdigit():
#         print("Número inválido")
#     else:
#         numero = int(numero)
#         factorial = 1
#         for i in range(1, numero +1):
#             factorial *=i
#         print(factorial)
        
# numero = input("Ingrese un número para hallar su factorial: --->")       
# calcular_factorial(numero)
    

"""
15. Empresa “TechManager” – Simulador de rendimiento laboral
Como jefe de equipo, quiero una función evaluar_empleado(nombre, horas) que:

Use un bucle for para simular las horas trabajadas (de 1 hasta horas).
Si la hora es mayor de 8, contar como hora extra.
Al final, calcular el total de horas normales y extras.
Mostrar un resumen del empleado.    """   

# def evaluar_empleado(nombre, horas):
#     extras = 0
#     normales = 0
#     for hora in range(1, horas):
#         if hora <=8:
#             normales += 1
#         else:
#             extras +=1
#     print(f"Para {nombre}: \nTotal de horas normales {normales} \ntotal horas extras: {extras}")


       
# nombre = input("Ingrese su nombre: --->")

# while True:
#     horas = input("Ingrese la cantidad de horas laboradas: --->")
#     if horas.isdigit():
#         horas = int(horas)
#         break
#     else:
#         print("Debe ingresar un valor válido, solo números enteros")

# evaluar_empleado(nombre, horas)


             

    

    
        
        
        
        
    

