from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 1. Cargar la imagen y convertirla a escala de grises
imagen = Image.open('kitler.jpg').convert('L')

# 2. Convertir la imagen a una matriz numpy
matriz = np.array(imagen)

# Mostrar imagen original
plt.imshow(matriz, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')
plt.show()

# 3. Voltear horizontalmente manualmente (invirtiendo cada fila)
filas, columnas = matriz.shape
matriz_volteada = np.zeros_like(matriz)

for i in range(filas):
    for j in range(columnas):
        matriz_volteada[i][j] = matriz[i][columnas - 1 - j]  # Copiar valores de derecha a izquierda

# 4. Mostrar imagen volteada
plt.imshow(matriz_volteada, cmap='gray')
plt.title('Imagen Volteada Horizontalmente (manual)')
plt.axis('off')
plt.show()


