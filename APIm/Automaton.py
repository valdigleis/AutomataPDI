#! -*- utf-8 -*-
#!/usr/bin/python3

from random import choice
from THEFE import THFE
from THEFE import ZERO
from THEFE import ONE

class Automaton(object):

    def __init__(self, states, alphabet, delta, s0, F, label="Machine"):
        self.__states = states
        self.__alphabelt = alphabet
        self.__delta = delta
        self.__s0 = s0
        self.__F = F

    # --------------------------------------------------
    # Métodos de computação
    # --------------------------------------------------

    def computeValuationByMax(self, words):
        X = ZERO
        for word in words:
            X = X + self.computeValuation(word)
        return X
    
    def computeValuationByMin(self, words):
        X = ONE
        for word in words:
            X = X * self.computeValuation(word)
        return X

    def computeValuation(self, word):
        return self.__F[self.compute(word)]

    def compute(self, word):
        s = self.__s0
        for c in word:
            L = s + ',' + c
            if L in self.__delta:
                s = self.__delta[L]
        return s

    
    # --------------------------------------------------
    # Return infos
    # --------------------------------------------------
    def getF(self):
        F = ''
        for L, V in self.__F.items():
            F = F + ('F(' + L + ')=' + str(V)) + '\n'
        return F
            
    def __len__(self):
        return len(self.__states)

    def __str__(self):
        S = str(self.__states) + '\n'
        A = str(self.__alphabelt) + '\n' + self.__s0 + '\n'
        D = ''
        for L, V in self.__delta.items():
            D = D + ('d(' + L + ')=' + V) + '\n'
        F = ''
        for L, V in self.__F.items():
            F = F + ('F(' + L + ')=' + str(V)) + '\n'
        return S + A + D + F
        
