#! -*- utf-8 -*-
#!/usr/bin/python3

from random import choice
from THEFE import ZERO

class Automaton(object):

    def __init__(self, states, alphabet, delta, s0, F, label="Machine"):
        self.__states = states
        self.__alphabelt = alphabet
        self.__delta = delta
        self.__s0 = s0
        self.__F = F

    def compute(self, word):
        s = self.__s0
        for c in word:
            L = s + ',' + c
            if L in self.__delta:
                s = self.__delta[L]
        return s

    def valuedCompute(self, word):
        s = self.__s0
        for c in word:
            L = s + ',' + c
            if L in self.__delta:
                s = self.__delta[L]
            else:
                return ZERO
        return self.__F[s]

    def __getFather(self, q):
        for K, V in self.__delta.items():
            if V == q:
                return K
        return None
    
    def __getBlues(self, reds):
        blues = set()
        for red in reds:
            for a in self.__alphabelt:
                L = red + ',' + a
                if L in self.__delta:
                    if self.__delta[L] not in reds:
                        blues.add(self.__delta[L])
        return blues

    
    def __distance(self, s, q, dist):
        if dist == 'Jaccard':
            return self.__F[s] ** self.__F[q]
        elif dist == 'std':
            return self.__F[s] // self.__F[q]
        else:
            return self.__F[s] ** self.__F[q]

    def __getAllAcessibles(self):
        Accs = set([self.__s0])
        sUse = set([self.__s0])
        while len(sUse) > 0:
            nextS = self.__getBlues(sUse)
            Accs = Accs.union(nextS)
            sUse = nextS
        return Accs

    def __otimize(self):
        temp = self.__states - self.__getAllAcessibles()
        self.__states = self.__states - temp
        for s in temp:
            del self.__F[s]
        toErase = set()
        for L, r in self.__delta.items():
            s = L.split(',')
            if s[0] in temp or r in temp:
                toErase.add(L)
        for L in toErase:
            if L in self.__delta:
                del self.__delta[L]
        temp = None
        toErase = None
    

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
            F = F + ('d(' + L + ')=' + str(V)) + '\n'
        return S + A + D + F
        
