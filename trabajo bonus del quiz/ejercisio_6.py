

def es_bisiesto(anio):
    if anio % 400 == 0:
        return True
    elif anio % 4 == 0 and anio % 100 != 0:
        return True
    else:
        return False

anio1 = int(input("Ingrese el primer año (entre 1 y 9999): "))
anio2 = int(input("Ingrese el segundo año (entre 1 y 9999): "))

b1 = es_bisiesto(anio1)
b2 = es_bisiesto(anio2)

print("Bisiestos:", b1, "; verdadero si misma condición:", b1 == b2)