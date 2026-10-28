

def es_perfecto(n):
    if n <= 1:
        return False
    
    suma = 0
    i = 1
    while i < n:
        if n % i == 0:
            suma = suma + i
        i = i + 1
        
    if suma == n:
        return True
    else:
        return False

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

r1 = es_perfecto(num1)
r2 = es_perfecto(num2)

# SALIDA
print("Perfectos:", r1, ";", r2)