
def cupos_libres(capacidad, ocupacion):
    libres = capacidad - ocupacion
    if libres < 0:
        return 0
    return libres

def eleccion(cap1, ocu1, cap2, ocu2, grupo):
    libres1 = cupos_libres(cap1, ocu1)
    libres2 = cupos_libres(cap2, ocu2)
    
    cabe1 = libres1 >= grupo
    cabe2 = libres2 >= grupo
    
    if not cabe1 and not cabe2:
        return 0
    elif cabe1 and not cabe2:
        return 1
    elif not cabe1 and cabe2:
        return 2
    else:

        sobrante1 = libres1 - grupo
        sobrante2 = libres2 - grupo
        
        if sobrante1 <= sobrante2:
            return 1
        else:
            return 2

print("Evaluando Sala 1 y Sala 2:")
c1 = int(input("Capacidad Sala 1: "))
o1 = int(input("Ocupación Sala 1: "))
c2 = int(input("Capacidad Sala 2: "))
o2 = int(input("Ocupación Sala 2: "))
g = int(input("Tamaño del grupo: "))

resultado = eleccion(c1, o1, c2, o2, g)

if resultado == 0:
    print("Retorno: 0, sin sala")
else:
    print("Sala elegida:", resultado)

    