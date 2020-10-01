#! -*- utf-8 -*-
#!/usr/bin/python3

import numpy as np


def getPixelRegion(i, j, image, tam=1):
    pixels = []
    m, n = imagem.shape
    target = int((tam + 1)/2)
    # Pega o central
    pixels.append(imagem(i,j))
    # Pegar os demais pixels
    for k1 in range(tam):
        for k2 in range(tam):
            L = i + (k2 - target)
            C = j + (k1 - target)
            if L > 0 and L < m and C > 0 and C < n:
                pixels.append(image[L][C])
    return pixels


def Hmedian(values):
    M = np.median(values)
    W = []
    ref = 0.0
    for x in values:
        ref = ref + abs(x - M)
    t = len(values)
    k = 1/(t-1)
    for x in values:
        if ref > 0:
            p = k * (1 - (abs(x - M)/ref))
            W.append(p)
        else:
            W.append(1/t)
    ref = 0.0
    for i in range(t):
        ref = ref + (values[i] * W[i])
    return ref

def Hmean(values):
    M = np.mean(values)
    W = []
    ref = 0.0
    for x in values:
        ref = ref + abs(x - M)
    t = len(values)
    k = 1/(t-1)
    for x in values:
        if ref > 0:
            p = k * (1 - (abs(x - M)/ref))
            W.append(p)
        else:
            W.append(1/t)
    ref = 0.0
    for i in range(t):
        ref = ref + (values[i] * W[i])
    return ref

def Hmax(values):
    M = np.max(values)
    W = []
    ref = 0.0
    for x in values:
        ref = ref + abs(x - M)
    t = len(values)
    k = 1/(t-1)
    for x in values:
        if ref > 0:
            p = k * (1 - (abs(x - M)/ref))
            W.append(p)
        else:
            W.append(1/t)
    ref = 0.0
    for i in range(t):
        ref = ref + (values[i] * W[i])
    return ref

def Hmin(values):
    M = np.min(values)
    W = []
    ref = 0.0
    for x in values:
        ref = ref + abs(x - M)
    t = len(values)
    k = 1/(t-1)
    for x in values:
        if ref > 0:
            p = k * (1 - (abs(x - M)/ref))
            W.append(p)
        else:
            W.append(1/t)
    ref = 0.0
    for i in range(t):
        ref = ref + (values[i] * W[i])
    return ref


def computeMixtureMedianImage(image, tam=1):
    # Pega as informações da imagem
    m, n = image.shape
    # define uma nova imagem
    newImage = np.zeros((m,n), dtype=float)
    # Loop e processamento
    for i in range(m):
        for j in range(n):
            L = getPixelRegion(i, j, image, tam)
            newImage = Hmedian(L)
    # retorna o resultado
    return newImage


def computeMixtureMeanImage(image, tam=1):
    # Pega as informações da imagem
    m, n = image.shape
    # define uma nova imagem
    newImage = np.zeros((m,n), dtype=float)
    # Loop e processamento
    for i in range(m):
        for j in range(n):
            L = getPixelRegion(i, j, image, tam)
            newImage = Hmean(L)
    # retorna o resultado
    return newImage

def computeMixtureMaxImage(image, tam=1):
    # Pega as informações da imagem
    m, n = image.shape
    # define uma nova imagem
    newImage = np.zeros((m,n), dtype=float)
    # Loop e processamento
    for i in range(m):
        for j in range(n):
            L = getPixelRegion(i, j, image, tam)
            newImage = Hmax(L)
    # retorna o resultado
    return newImage

def computeMixtureMinImage(image, tam=1):
    # Pega as informações da imagem
    m, n = image.shape
    # define uma nova imagem
    newImage = np.zeros((m,n), dtype=float)
    # Loop e processamento
    for i in range(m):
        for j in range(n):
            L = getPixelRegion(i, j, image, tam)
            newImage = Hmin(L)
    # retorna o resultado
    return newImage