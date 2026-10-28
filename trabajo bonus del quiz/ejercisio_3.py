

numero = int(input("Ingrese un número entero positivo (0 o negativo para salir): "))

while numero > 0:
    texto = str(numero)
    cantidad = len(texto)
    suma = 0
    
    i = 0
    while i < cantidad:
        digito = int(texto[i])
        suma = suma + (digito ** cantidad)
        i = i + 1
        
    if suma == numero:
        print("El número", numero, "ES narcisista.")
    else:
        print("El número", numero, "NO es narcisista.")
        
    numero = int(input("Ingrese otro número (0 o negativo para salir): "))

print("Fin del programa.")