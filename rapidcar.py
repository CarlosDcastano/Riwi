# 6. Parqueadero “RapidCar” — Tarifa escalonada
while True:
    hora = 2000

    cantHoras = int(input("Ingrese la cantidad de horas: "))
    total = hora * cantHoras
    multa = 5000

    while cantHoras < 0:
        print("No se acepta un valor negativo")
        cantHoras = int(input("Ingrese la cantidad de horas: "))

    if cantHoras >= 0 and cantHoras < 5:
        if cantHoras == 0:
            total = hora
        print(f"Total a pagar: {total}")

    else:
        print(f"Total a pagar: {total + multa}")
    