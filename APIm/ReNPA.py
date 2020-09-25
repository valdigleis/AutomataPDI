#! -*- utf-8 -*-
#!/usr/bin/python3


from skimage.io import imread
from skimage.io import show
from Auxiliars import createAutomataAndXi as cax
from Auxiliars import getListWord as words
from Auxiliars import getEnumPixel as pixels
from THEFE import THFE
from math import log2

import numpy as np
import sys

# URL da imagem
urlImage = sys.argv[1]
# Abrir a imagem
#figure = imread(urlImage)
#figure = figure/255
figure = np.random.rand(4,4)
(m,n) = figure.shape
# Cria o autômato e a função xi
M, Xi = cax(figure)
# pega as palavras
W = words('abcd', n)
# pega todos os pixels
P = pixels(m)
# Matriz para a nova imagem
newFigure = np.zeros((m,n), float)
# O processamento
print(len(W) == len(P))
