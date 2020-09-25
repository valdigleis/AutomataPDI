#! -*- utf-8 -*-
#!/usr/bin/python3


from skimage.io import imread
from skimage.io import show
from skimage.io import imsave
from skimage.io import imshow
from Auxiliars import createAutomataAndXi as cax
from Auxiliars import getListWord as words
from Auxiliars import getEnumPixel as pixels
from THEFE import THFE

import numpy as np
import sys

# URL da imagem
urlImage = sys.argv[1]
# Abrir a imagem
figure = imread(urlImage)
figure = figure/255
(m,n) = figure.shape
# Cria o autômato e a função xi
M, Xi = cax(figure)
# pega as palavras
Words = words('abcd', n)
# pega todos os pixels
Pixels = pixels(m)
# Matriz para a nova imagem
newFigure1 = np.zeros((m,n), float)
newFigure2 = np.zeros((m,n), float)
# O processamento
for i in range(len(Pixels)):
    w = Words[i]
    pixel = Pixels[i]
    x, y = pixel[0], pixel[1]
    v = Xi[M.compute(w)]
    newFigure1[x][y] = v[0][0] * M.prefixesComputationWithMaxCom(w).getSum()
    newFigure2[x][y] = v[0][0] * M.prefixesComputationWithMinCom(w).getSum()
# Salvar as imagem
nImage = sys.argv[1].split('/')
name1 = 'Sup' + nImage[len(nImage)-1]
name2 = 'Inf' + nImage[len(nImage)-1]
imsave(name1, newFigure1)
imsave(name1, newFigure1)