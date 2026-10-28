

def necesidad(existencias, minimo):
    if existencias < minimo:
        return True
    else:
        return False

def lotes_necesarios(faltante, lote):
    cociente = faltante // lote
    residuo = faltante % lote
    
    if residuo > 0:
        return cociente + 1
    else:
        return cociente

def pedido(existencias, minimo, capacidad, lote):
    if not necesidad(existencias, minimo):
        return 0
    
    faltante = minimo - existencias
    lotes = lotes_necesarios(faltante, lote)
    cant_pedido = lotes * lote
    
    if existencias + cant_pedido > capacidad:
        return -1
        
    return cant_pedido

print("Prueba de reposición:")
ex = int(input("Existencias: "))
min_val = int(input("Mínimo: "))
cap = int(input("Capacidad: "))
lot = int(input("Lote: "))

nec = necesidad(ex, min_val)
ped = pedido(ex, min_val, cap, lot)

print("Necesita:", nec)
if ped == -1:
    print("Retorno: -1; no cabe el pedido")
else:
    print("Pedido:", ped)