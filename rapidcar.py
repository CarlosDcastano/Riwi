# 6. Parqueadero “RapidCar” — Tarifa escalonada

hora = 2000

cantHoras = int(input("Ingrese la cantidad de horas: "))
total = hora * cantHoras
multa = 5000

if cantHoras < 0:
    print("No se acepta un valor negativo")

elif cantHoras < 5:
    print(f"Total a pagar: {total}")

else:
    print(f"Total a pagar: {total + multa}")
    