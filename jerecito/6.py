
def cajero_automatico():
    monto = int(input("Ingrese la cantidad que desea retirar (solo números enteros positivos): "))

    if monto <= 0:
        print("La cantidad debe ser mayor que 0.")
        return


    billetes_1000 = monto // 1000
    restante = monto % 1000

    
    billetes_200 = restante // 200
    restante = restante % 200

    
    print("\n--- Detalle de entrega ---")
    print(f"Billetes de $1000: {billetes_1000}")
    print(f"Billetes de $200: {billetes_200}")
    print(f"Saldo no entregado: ${restante}")


cajero_automatico()
