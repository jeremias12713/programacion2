def repartir_caramelos():
    caramelos = int(input("¿Cuántos caramelos hay? "))
    estudiantes = int(input("¿Cuántos estudiantes hay? "))

    if estudiantes <= 0:
        print("Debe haber al menos un estudiante.")
        return

    caramelos_por_estudiante = caramelos // estudiantes
    sobrantes = caramelos % estudiantes

    print("\n--- Reparto de caramelos ---")
    print(f"A cada estudiante le tocan {caramelos_por_estudiante} caramelos.")
    print(f"Caramelos que sobran en la bolsa: {sobrantes}")


repartir_caramelos()
