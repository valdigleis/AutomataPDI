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

    def computeValuation(self, word):
        s = self.__s0
        for c in word:
            L = s + ',' + c
            if L in self.__delta:
                s = self.__delta[L]
            else:
                return ZERO
        return self.__F[s]

    def compute(self, word):
        s = self.__s0
        for c in word:
            L = s + ',' + c
            if L in self.__delta:
                s = self.__delta[L]
        return s

    def __getAllPrefixes(self, word):
        n = len(word)
        ctl = 0
        L = []
        while ctl < n + 1:
            L.append(word[:ctl])
            ctl = ctl + 1
        del L[0]
        return L

    def prefixesComputationWithMaxCom(self, word):
        words = self.__getAllPrefixes(word)
        result = ZERO
        for word in words:
            s = self.compute(word)
            result = result + self.__F[s]
        return result

    def prefixesComputationWithMinCom(self, word):
        words = self.__getAllPrefixes(word)
        result = ONE
        for word in words:
            s = self.compute(word)
            result = result * self.__F[s]
        return result
    

    # --------------------------------------------------
    # --------------------------------------------------
            
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
        
