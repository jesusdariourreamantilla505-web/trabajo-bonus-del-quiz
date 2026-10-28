

def cobertura(peso, zona):
    if peso > 0 and peso <= 20 and (zona == 1 or zona == 2):
        return True
    else:
        return False

def costo_inicial(peso, zona):
    if zona == 1:
        base = 5000
    else:
        base = 8000
    
    exceso = peso - 1
    if exceso < 0:
        exceso = 0
        
    recargo = 2000 * exceso
    return base + recargo

def costo_final(peso, zona, compra):
    if not cobertura(peso, zona):
        return -1
    
    inicial = costo_inicial(peso, zona)
    
    if compra >= 100000:
        final = inicial * 0.50
    else:
        final = inicial
        
    return final

print("Prueba de envío:")
p = float(input("Peso (kg): "))
z = int(input("Zona (1 o 2): "))
c = float(input("Valor de la compra: "))

resultado = costo_final(p, z, c)

if resultado == -1:
    print("Retorno: -1; sin cobertura")
else:
    print("Costo:", resultado, "pesos")