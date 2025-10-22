import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread


img = imread('descarga.jpg')  


if img.ndim == 3:
    img = img @ [0.2989, 0.5870, 0.1140]  


if img.max() > 1:
    img = img / 255.0


kernel = (1/16) * np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
])


filtered_img = img.copy()
rows, cols = img.shape


for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        region = img[i-1:i+2, j-1:j+2]
        value = np.sum(region * kernel)
        filtered_img[i, j] = value


plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Imagen Original")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Imagen con Desenfoque Gaussiano")
plt.imshow(filtered_img, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

