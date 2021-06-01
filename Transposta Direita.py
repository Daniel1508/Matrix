import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def transposta(m):
	largura = len(m[0])
	altura = len(m)
	resposta=[[0 for x in range(largura)] for y in range(altura)]	
	for i in range(altura):

		for j in range(largura):
			resposta[i][j] = m[i][j]
	invertida = resposta[::-1]
	return np.transpose(invertida)

img = cv.imread('img/zeta.png')
img = cv.imread('img/unifafibe.jpg')
b,g,r = cv.split(img)
b1 = transposta(b)
g1 = transposta(g)
r1 = transposta(r)
img2 = cv.merge((b1,g1,r1))
plt.subplot(121),plt.imshow(img, cmap="gray"),plt.title('Original')
plt.subplot(122),plt.imshow(img2, cmap="gray"),plt.title('Processed')
plt.show()