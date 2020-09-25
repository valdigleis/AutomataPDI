#! -*- utf-8 -*-
#!/usr/bin/python3

import string
import itertools
import skimage
import numpy as np

from math import log2
from THEFE import THFE as thfe
from THEFE import ONE
from THEFE import ZERO
from Automaton import Automaton as aut


def getEnumPixel(n):
    L = []
    t = n ** 2
    i = 0
    j = 0
    while len(L) < t:
        T1 = tuple([i, j])
        T2 = tuple([i, j+1])
        T3 = tuple([i+1, j])
        T4 = tuple([i+1, j+1])
        L.append(T1)
        L.append(T2)
        L.append(T3)
        L.append(T4)
        j = j + 2
        if j == n:
            j = 0
            i = i + 2
    return L


def getListWord(alphabet, n):
    L = [''.join(x) for x in itertools.product(alphabet, repeat=int(log2(n)))]
    return L


def diffABS(L1, L2, n):
    x = L1[n]
    y = L2[n]
    return abs(x - y)


def createAutomataAndXi(figure):
    # funcao xi
    xi = dict()
    # variaveis do automato
    states = set()
    alphabet = {'a', 'b', 'c', 'd'}
    delta = dict()
    fStates = dict()
    s0 = 's0'
    states.add(s0)
    # definir o básico
    xi[s0] = figure
    fStates[s0] = ONE
    s = 0
    while True:
        # Imagem de trabalho
        cS = 's' + str(s)
        tmp = xi[cS]
        L, C = tmp.shape
        
        nL = int(L/2)
        nC = int(C/2)

        if nL == 0:
            break

        dim = tuple([nL, nC])

        # Cria as matrizes extras
        mA = np.zeros(dim, dtype=float)
        mB = np.zeros(dim, dtype=float)
        mC = np.zeros(dim, dtype=float)
        mD = np.zeros(dim, dtype=float)

        # Povoando as matriz
        l2 = 0
        for i in range(L):
            c2 = 0
            for j in range(C):
                if i < nL and j < nC:
                    mA[i][j] = tmp[i][j]
                elif i < nL and j >= nC:
                    mB[i][c2] = tmp[i][j]
                    c2 = c2 + 1
                elif (i >= nL and l2 < nL) and j < nC:
                    mC[l2][j] = tmp[i][j]
                else:
                    mD[l2][c2] = tmp[i][j]
                    c2 = c2 + 1
            l2 = l2 + 1
            if l2 == nL:
                l2 = 0

        # atualiza a função xi.
        cA = len(xi)
        cB = len(xi) + 1
        cC = len(xi) + 2
        cD = len(xi) + 3
        sA = 's' + str(cA)
        sB = 's' + str(cB)
        sC = 's' + str(cC)
        sD = 's' + str(cD)
        xi[sA] = mA
        xi[sB] = mB
        xi[sC] = mC
        xi[sD] = mD

        # Adiciona os novos estados
        states.add(sA)
        states.add(sB)
        states.add(sC)
        states.add(sD)

        # Cria as transições
        delta[cS + ',a'] = sA
        delta[cS + ',b'] = sB
        delta[cS + ',c'] = sC
        delta[cS + ',d'] = sD

        # processado as medidas dos quadrantes
        Ltmp = [tmp.min(), tmp.mean(), np.median(tmp), tmp.max()]
        LnA = [mA.min(), mA.mean(), np.median(mA), mA.max()]
        LnB = [mA.min(), mB.mean(), np.median(mB), mB.max()]
        LnC = [mA.min(), mC.mean(), np.median(mC), mC.max()]
        LnD = [mA.min(), mD.mean(), np.median(mD), mD.max()]

        # Diferenca entre as medidas
        rA = [abs(Ltmp[i] - LnA[i]) for i in range(4)]
        rB = [abs(Ltmp[i] - LnB[i]) for i in range(4)]
        rC = [abs(Ltmp[i] - LnC[i]) for i in range(4)]
        rD = [abs(Ltmp[i] - LnD[i]) for i in range(4)]

        # valora os estados finais
        fStates[sA] = thfe(rA)
        fStates[sB] = thfe(rB)
        fStates[sC] = thfe(rC)
        fStates[sD] = thfe(rD)

        # Atualiza o estado de referencia
        s = s + 1

    # Cria o automato
    M = aut(states, alphabet, delta, s0, fStates)
    return M, xi
