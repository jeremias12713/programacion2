def crecimiento_debacteria():
    horas = int(input("¿Cuántas horas han pasado? "))

    if horas < 0:
        print("El número de horas no puede ser negativo.")
        return

    bacterias = 2 ** horas

    print(f"\nDespués de {horas} horas habrá {bacterias} bacterias.")


crecimiento_debacteria()
