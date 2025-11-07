pruebaTecnica = float(input("Ingrese la nota de la prueba técnica: "))

while (pruebaTecnica <0 or pruebaTecnica >5):
    print("Error, los valores a ingresar deben estar entre 0 y 5, intenta de nuevo")
    pruebaTecnica = float(input("Ingrese la nota de la prueba técnica: "))
    
    
pruebaLogica = float(input("Ingrese la nota de la prueba lógica: "))

while (pruebaLogica <0 or pruebaLogica >5):
    print("Error, los valores a ingresar deben estar entre 0 y 5, intenta de nuevo")
    pruebaLogica = float(input("Ingrese la nota de la prueba lógica: "))
    
notaFinal = (pruebaTecnica * 0.7) + (pruebaLogica * 0.3)

if notaFinal >= 3:
    print("Aprobado ", notaFinal)
elif notaFinal >=2 and notaFinal <3:
    print("Revision ", notaFinal)
else:
    print("Reprobado ", notaFinal)
    

    



    