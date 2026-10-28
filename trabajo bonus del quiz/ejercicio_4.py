
inicio = int(input("Ingrese el rango inicial: "))
fin = int(input("Ingrese el rango final: "))

print("Los números abundantes entre", inicio, "y", fin, "son:")

actual = inicio
while actual <= fin:
    suma_divisores = 0
    
    i = 1
    while i < actual:
        if actual % i == 0:
            suma_divisores = suma_divisores + i
        i = i + 1
        
    if suma_divisores > actual:
        print(actual)
        
    actual = actual + 1

print("Fin del programa.")