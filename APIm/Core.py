import itertools

import numpy as np

from math import log2

from THEFE import THFE
from THEFE import ONE
from THEFE import ZERO

from Automaton import Automaton as aut


def defineAutXi(image):
    # Pega as informações básicas da imagem
    (m, n) = image.shape
    if m != n:
        return None
    # Aloca a ED para a funcao xi
    xi = dict()
    # Aloca as variaveis usadas para definir o automato
    states = set()
    alphabet = {1, 2, 3, 4}
    delta = dict()
    fStates = dict()
    s0 = 's0'
    states.add(s0)
    # Definir o básico
    xi[s0] = [(0,0), m]
    fStates[s0] = ONE
    s = 0
    while True:
        # Imagem de trabalho
        S = 's' + str(s)
        # Pontos extremos da imagem de trabalho
        pS, d = xi[S]
        # Testar se precisa fazer o processamento
        D = int(d/2)
        if D == 0:
            break
        # Medidas da imagem de trabalho
        Ls = getMeasures(pS, d, image)
        # Define os proximos estados
        s1 = 's' + str(len(xi))
        s2 = 's' + str(len(xi) + 1)
        s3 = 's' + str(len(xi) + 2)
        s4 = 's' + str(len(xi) + 3)
        # Pegar os pontos esquerdos superiores dos quadrantes
        pS1 = pS
        pS2 = (pS[0], pS[1] + D)
        pS3 = (pS[0] + D, pS[1])
        pS4 = (pS[0] + D, pS[1] + D)
        # Define o xi
        xi[s1] = [pS1, D]
        xi[s2] = [pS2, D]
        xi[s3] = [pS3, D]
        xi[s4] = [pS4, D]
        # Pegas as medidas dos quadrantes
        Ls1 = getMeasures(pS1, D, image)
        Ls2 = getMeasures(pS2, D, image)
        Ls3 = getMeasures(pS3, D, image)
        Ls4 = getMeasures(pS4, D, image)
        # Cria as transições
        delta[S + ',1'] = s1
        delta[S + ',2'] = s2
        delta[S + ',3'] = s3
        delta[S + ',4'] = s4
        # Peparação para valorar
        L1 = [(1.0 - abs(Ls[i] - Ls1[i])) for i in range(4)]
        L2 = [(1.0 - abs(Ls[i] - Ls2[i])) for i in range(4)]
        L3 = [(1.0 - abs(Ls[i] - Ls3[i])) for i in range(4)]
        L4 = [(1.0 - abs(Ls[i] - Ls4[i])) for i in range(4)]
        # valora os estados
        fStates[s1] = THFE(L1)
        fStates[s2] = THFE(L2)
        fStates[s3] = THFE(L3)
        fStates[s4] = THFE(L4)
        # Atualiza o estado
        s = s + 1
    # Cria o automato
    M = aut(states, alphabet, delta, s0, fStates)
    return M, xi
        
def getMeasures(p, d, image):
    ki, kj = p[0], p[1]
    M = np.zeros((d,d), dtype=float)
    for i in range(d):
        for j in range(d):
            M[i][j] = image[ki + i][kj + j]
    m1 = M.min()
    m2 = M.mean()
    m3 = np.median(M)
    m4 = M.max()
    return [m1, m2, m3, m4]

def getListWords(n):
    N = [''.join(x) for x in itertools.product('1234', repeat=int(log2(n)))]
    L = []
    for x in N:
        L.append(int(x))
    return L

def getAllPrefixes(word):
    n = len(word)
    ctl = 0
    L = []
    while ctl < n + 1:
        L.append(word[:ctl])
        ctl = ctl + 1
    del L[0]
    return L

def getPrefixes(word, n):
    P = getAllPrefixes(word)
    prefixes = P[len(word)-n: len(word)]
    return prefixes
