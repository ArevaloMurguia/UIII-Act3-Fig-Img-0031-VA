import numpy as np 
import pandas as pd 
import cv2 
import matplotlib.pyplot as plt

# Arevalo Rafael NC 0031
print("Arevalo Rafael NC 0031")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro VA")
Mi_Imagen = cv2.imread('TheGervontaDavisChamps.jpg')
plt.imshow(Mi_Imagen)
plt.title('Gervonta Davis y Arevalo Rafael 0031')
plt.show() 
print("+-+-+-+- Puntos en la imagen +-+-+-+-")
plt.imshow(Mi_Imagen)
x = [100,100,300,340]
y = [100,400,500,300]
plt.scatter(x,y, s=20,c='red')
plt.show()

import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt

# Arevalo Rafael NC 0031
print("Arevalo Rafael NC 0031")
print("UIII Act3 colocar puntos a una imagen en blanco y negro VA")

# Leer imagen en blanco y negro
Mi_Imagen = cv2.imread('TheGervontaDavisChamps.jpg', 0)

if Mi_Imagen is None:
    print("Error: No se encontro la imagen")
    exit()

# Mostrar imagen
plt.imshow(Mi_Imagen, cmap='gray')
plt.title('Gervonta Davis y Arevalo Rafael 0031')
plt.show()

# Convertir a color para colocar puntos rojos
Imagen_Color = cv2.cvtColor(Mi_Imagen, cv2.COLOR_GRAY2BGR)

print("+-+-+-+- Puntos en la imagen +-+-+-+-")

x = [100, 100, 300, 340]
y = [100, 400, 500, 300]

for i in range(len(x)):
    cv2.circle(Imagen_Color, (x[i], y[i]), 8, (0, 0, 255), -1)

# Dibujar rectangulo
cv2.rectangle(Imagen_Color, (50, 50), (300, 250), (0, 255, 0), 3)

# Dibujar circulo
cv2.circle(Imagen_Color, (350, 350), 60, (255, 0, 0), 3)

# Mostrar resultado
plt.imshow(cv2.cvtColor(Imagen_Color, cv2.COLOR_BGR2RGB))
plt.title('Imagen con puntos, cuadro y circulo')
plt.show()

# Guardar imagen
cv2.imwrite('Resultado_Act3.jpg', Imagen_Color)

print("Imagen guardada correctamente")
