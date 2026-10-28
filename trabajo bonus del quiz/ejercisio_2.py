

numero = int(input("Ingrese un número entero positivo (o uno negativo para salir): "))

while numero >= 0:
    suma_divisores = 0
    
    i = 1
    while i < numero:
        if numero % i == 0:
            suma_divisores = suma_divisores + i
        i = i + 1
        

    if suma_divisores == numero and numero > 0:
        print("El número", numero, "ES perfecto.")
    else:
        print("El número", numero, "NO es perfecto.")
        
    numero = int(input("Ingrese otro número (o uno negativo para salir): "))

print("Fin del programa.")