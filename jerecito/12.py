def cifrar_cesar(texto, desp, modo):
    if any(c.isdigit() for c in texto):
        raise ValueError("El texto no debe contener números.")

    if not isinstance(desp, int):
        raise ValueError("El desplazamiento debe ser un número entero.")

    if modo == "descifrar":
        desp = -desp

    resultado = ""
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultado += chr((ord(c) - base + desp) % 26 + base)
        else:
            resultado += c

    return resultado


def main():
    print("CIFRADO CÉSAR")
    texto = input("Ingrese el mensaje: ")

    if any(c.isdigit() for c in texto):
        print("Error: No se permiten números.")
        return

    try:
        desp = int(input("Ingrese el desplazamiento: "))
    except ValueError:
        print("Error: El desplazamiento debe ser un número.")
        return

    modo = input("¿Desea cifrar o descifrar? (cifrar/descifrar): ").lower()
    if modo not in ["cifrar", "descifrar"]:
        print("Error: Modo inválido.")
        return

    try:
        resultado = cifrar_cesar(texto, desp, modo)
        print("Resultado:", resultado)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
