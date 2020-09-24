#! -*- utf-8 -*-
#!/usr/bin/python3

from skimage.io import imread
from skimage.io import show
from Auxiliars import createAutomataAndXi as cax

import sys

# URL da imagem
urlImage = sys.argv[1]
alpha = float(sys.argv[2])
distance = sys.argv[3]
# Abrir a imagem
figure = imread(urlImage)
figure = figure/255

M, Xi = cax(figure)
print(len(M))
print(M.meanDistance(distance))