import tkinter as tk
from tkinter import messagebox

def cifrar_cesar():
    texto = entrada.get()
    if any(c.isdigit() for c in texto):
        messagebox.showerror("Error", "No se permiten números.")
        return

    try:
        desp = int(desplazamiento.get())
    except ValueError:
        messagebox.showerror("Error", "El desplazamiento debe ser un número.")
        return

    if modo.get() == "descifrar":
        desp = -desp

    resultado = ""
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultado += chr((ord(c) - base + desp) % 26 + base)
        else:
            resultado += c

    salida.config(text="Resultado: " + resultado)


ventana = tk.Tk()
ventana.title("Cifrado César")
ventana.geometry("400x300")  
ventana.configure(bg="Green")  

fuente_titulo = ("Helvetica", 12, "bold")
fuente_normal = ("Helvetica", 10)


tk.Label(ventana, text="Mensaje:", bg="White", font=fuente_titulo).pack(pady=5)
entrada = tk.Entry(ventana, width=40, font=fuente_normal)
entrada.pack()

tk.Label(ventana, text="Desplazamiento:", bg="Red", font=fuente_titulo).pack(pady=5)
desplazamiento = tk.Entry(ventana, width=10, font=fuente_normal)
desplazamiento.pack()

modo = tk.StringVar(value="cifrar")
tk.Radiobutton(ventana, text="Cifrar", variable=modo, value="cifrar", bg="Yellow", font=fuente_normal).pack()
tk.Radiobutton(ventana, text="Descifrar", variable=modo, value="descifrar", bg="Red", font=fuente_normal).pack()

tk.Button(ventana, text="Procesar", command=cifrar_cesar, bg="Red", fg="white", font=fuente_normal).pack(pady=10)
salida = tk.Label(ventana, text="Resultado: ", bg="Black", font=fuente_normal)
salida.pack(pady=5)

ventana.mainloop()

