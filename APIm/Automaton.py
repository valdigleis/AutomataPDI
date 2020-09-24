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

    # '''
    # ------------- Para PDI ---------------------------

    def meanDistance(self, dist):
        L = []
        for s in self.__states:
            L.append(s)
        d = 0.0
        k = 0
        for i in range(len(L)-1):
            j = i + 1
            while j < len(L):
                d = d + self.__distance(L[i], L[j], dist)
                k = k + 1
                j = j + 1
        return d/k


    def __merge(self, s, q):
        self.__F[s] = self.__F[s] + self.__F[q]
        Fq = self.__getFather(s)
        self.__delta[Fq] = s
            
        
    def reductionForImage(self, alpha, dist):
        reds = set([self.__s0])
        blues = self.__getBlues(reds)
        while len(blues) > 0:
            print('Tamahos red e blues:', len(reds), len(blues))
            blue = choice(list(blues))
            color = True
            for red in reds:
                if self.__distance(red, blue, dist) < alpha:
                    self.__merge(red, blue)
                    self.__otimize()
                    color = False
                    break
            if color == True:
                reds.add(blue)
            blues = self.__getBlues(reds)

    # '''
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
            F = F + ('d(' + L + ')=' + V) + '\n'
        return S + A + D + F
        
