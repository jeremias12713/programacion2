import tkinter as tk
import random

numero = random.randint(1, 20)
intentos = 6

def reiniciar():
    global numero, intentos
    nuevo_numero = numero
    while nuevo_numero == numero:
        nuevo_numero = random.randint(1, 20)
    numero = nuevo_numero
    intentos = 6
    entrada.delete(0, tk.END)
    mensaje.config(text="¡Felicidades! ¡Clashini viciosini!")

def verificar():
    global intentos, numero
    valor = entrada.get()

    if not valor.isdigit():
        mensaje.config(text="Ingresa un número válido.")
        return

    intento = int(valor)
    intentos -= 1

    if intento == numero:
        mensaje.config(text=f"¡Correcto! Adivinaste en {6 - intentos} intentos.")
        reiniciar()
    elif intentos == 0:
        mensaje.config(text=f"Perdiste. El número era {numero}. Reiniciando...")
        root.after(3000, reiniciar)
    elif intento < numero:
        mensaje.config(text=f"Muy bajo. Intentos restantes: {intentos}")
    else:
        mensaje.config(text=f"Muy alto. Intentos restantes: {intentos}")

root = tk.Tk()
root.geometry("700x750")
root.title("Juego Adivina el Número")
root.config(bg="black")

label = tk.Label(
    root,
    text="Adivina el número entre 1 y 20",
    bg="black",
    fg="white",
    font=("Helvetica", 16, "bold")
)
label.pack(padx=20, pady=20)

entrada = tk.Entry(root, bg="gray20", fg="white", insertbackground="white", font=("Helvetica", 14))
entrada.pack(pady=10)

boton = tk.Button(root, text="Verificar", command=verificar, bg="gray30", fg="white", activebackground="gray50", font=("Helvetica", 14, "bold"))
boton.pack(pady=10)

mensaje = tk.Label(root, text="Nuevo juego: Adivina un número entre 1 y 20", bg="black", fg="white", font=("Helvetica", 14))
mensaje.pack(pady=10)

root.mainloop()
e