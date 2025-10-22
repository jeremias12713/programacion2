from PIL import Image
import numpy as np
import matplotlib.pyplot as plt



def cargar_imagen(ruta):
    imagen = Image.open(mclovin.jpg)
    imagen_matriz = np.array(imagen)
    return imagen, imagen_matriz


def rotar_90_derecha(imagen_matriz):
    return np.rot90(imagen_matriz, -1)


def rotar_180(imagen_matriz):
    return np.rot90(imagen_matriz, 2)


def mostrar_matriz(imagen_matriz):
    for fila in imagen_matriz:
        print(fila)


def main():
   
    imagen, imagen_matriz = cargar_imagen(ruta_imagen)
    
    
    print("mclovin:")
    mostrar_matriz(imagen_matriz)
    
    
    rotacion = input("\n¿Quieres rotar la imagen? (90° a la derecha / 180°): ")
    
    if rotacion == '90':
        imagen_rotada = rotar_90_derecha(imagen_matriz)
        print("\nImagen Rotada 90° hacia la derecha:")
        mostrar_matriz(imagen_rotada)
        imagen_rotada_pillow = Image.fromarray(imagen_rotada)
        imagen_rotada_pillow.show()
    elif rotacion == '180':
        imagen_rotada = rotar_180(imagen_matriz)
        print("\nImagen Rotada 180°:")
        mostrar_matriz(imagen_rotada)
        imagen_rotada_pillow = Image.fromarray(imagen_rotada)
        imagen_rotada_pillow.show()
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
