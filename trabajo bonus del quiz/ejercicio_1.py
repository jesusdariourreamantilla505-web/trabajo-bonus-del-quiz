def evaluar_temperatura_incubacion():
    print("***********************************")
    print(" Incubación de tortugas")
    print("***********************************")

total_registrado = 0
cant_bajas = 0
cant_normales = 0
cant_altas = 0

while True:
    entrada = input("\ningrese la temperatura (°C) o escriba 'salir' para acabar ")


    if entrada.lower() == 'salir':
            print("\n--- RESUMEN DE LA JORNADA ---")
            print(f"Total de mediciones realizadas: {total_registros}")
            print(f"Temperaturas T. baja: {cant_bajas}")
            print(f"Temperaturas T. normal: {cant_normales}")
            print(f"Temperaturas T. alta: {cant_altas}")
            print("Saliendo del sistema de monitoreo. ¡Hasta pronto!")
            break
            
    temperatura = float(entrada)
    total_registros += 1
        
    if temperatura < 26.0:
            print("T. baja")
            cant_bajas += 1
    elif 26.0 <= temperatura <= 34.0:
            print("T. normal")
            cant_normales += 1
    else:
            print("T. alta")
            cant_altas += 1

    if __name__ == "_main_":
        evaluar_temperatura_incubacion()


