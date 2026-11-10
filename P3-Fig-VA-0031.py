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