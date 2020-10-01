from skimage.io import imread
from skimage.transform import rescale

from Core import defineAutXi
from Core import getListWords

import numpy as np

import sys

# URL da imagem
urlImage = sys.argv[1]
# Abrir a imagem
image = imread(urlImage)
# image = np.random.randint(5, size=(4, 4))
image = rescale(image, 0.5, anti_aliasing=False)
image = image/255
# pegas as informações
(m,n) = image.shape
# Gera as palavras
words = getListWords(m)
# Pega a funcao xi e o automato
A, xi = defineAutXi(image)
# Gera as novas imagens
newImagen = np.zeros((m,n), dtype=float)
# loop de processamento
for word in words:
    w = str(word)
    s = A.compute(w)
    P = xi[s]
    i, j = P[0]
    newImagen[i][j] = image[i][j] 
# teste
print((image == newImagen).all())
