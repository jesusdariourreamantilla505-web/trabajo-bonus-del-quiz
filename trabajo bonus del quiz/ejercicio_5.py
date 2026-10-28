def es_multiplo(a, b):
    if b == 0:
        return False
    
    if a % b == 0:
        return True
    else:
        return False

n1 = int(input("Ingrese el primer entero: "))
n2 = int(input("Ingrese el segundo entero: "))

r1 = es_multiplo(n1, n2)
r2 = es_multiplo(n2, n1)

print(n1, "múltiplo de", n2 + ":", r1)
print(n2, "múltiplo de", n1 + ":", r2)