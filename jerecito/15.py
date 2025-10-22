from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


imagen_color = Image.open('mclovin.jpg').convert('RGB')


plt.imshow(imagen_color)
plt.title('Imagen a Color')
plt.axis('off')
plt.show()


matriz_color = np.array(imagen_color)


def convertir_a_grises_manual(matriz_rgb):
    filas, columnas, _ = matriz_rgb.shape
    matriz_gris = np.zeros((filas, columnas), dtype=np.uint8)

    for i in range(filas):
        for j in range(columnas):
            R = matriz_rgb[i][j][0]
            G = matriz_rgb[i][j][1]
            B = matriz_rgb[i][j][2]
            gris = int(R * 0.2989 + G * 0.5870 + B * 0.1144)
            matriz_gris[i][j] = gris
    
    return matriz_gris


matriz_grises = convertir_a_grises_manual(matriz_color)


plt.imshow(matriz_grises, cmap='gray')
plt.title('Imagen en Escala de Grises (manual)')
plt.axis('off')
plt.show()
