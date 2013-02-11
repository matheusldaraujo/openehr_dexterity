# -*- coding: utf-8 -*-
__author__ = 'chrispess'


from openehr.BASIC_TYPES import typeFloat
from openehr.BASIC_TYPES import typeBool

class Interval:

    # inf limite inferior do intervalo
    inf = typeFloat()

    # sup limite superior do intervalo
    sup = typeFloat()

    # boolean inf_inclusive true se intervalo fechado en inf, false se intervalo aberto em inf
    inf_inclusive = typeBool()

    # boolean sup_inclusive true se intervalo fechado en sup, false se intervalo aberto em sup
    sup_inclusive =typeBool()

    #construtor
    def __init__(self,inf,sup,inf_inclusive,sup_inclusive):

        self.inf = inf
        self.sup = sup
        self.inf_inclusive = False if self.inf == None else True
        self.sup_inclusive = False if self.sup == None else True


    #construtor. extremos inclusos por default
    def __init__(self,inf,sup,inf_inclusive,sup_inclusive):

        self.inf = inf
        self.sup = sup
        self.inf_inclusive = True
        self.sup_inclusive = True

    #retorna o limite inferior do intervalo
    def get_inf(self):
         return self.inf

    #retorna o limite superior do intervalo
    def get_sup(self):
         return self.sup


    #define o limite inferior do intervalo
    def set_inf(self, inf):
        self.inf = inf


    #define o limite superior do intervalo
    def set_sup(self, sup):
        self.sup = sup


    #define se o intervalo é fechado à esquerda
    def set_inf_inclusive(self, inf_inclusive):
        self.inf_inclusive = inf_inclusive


    #define se o intervalo é fechado à direita
    def set_sup_inclusive(self, sup_inclusive):
        self.sup_inclusive = sup_inclusive


    #retorna string relativo ao intervalo
    def to_string(self):
        interval_str =[]
        interval_str.append(self.inf)
        interval_str.append(self.inf_inclusive)
        interval_str.append(self.sup)
        interval_str.append(self.sup_inclusive)

        return interval_str


    #retorna true se o limite inferior do intervalo é inclusivo
    def isInfIncluded(self):
        return self.inf_inclusive


    #retorna true se o limite superior do intervalo é inclusivo
    def isSupIncluded(self):
        return self.sup_inclusive


    #retorna true se o valor do argumento se encontra no intervalo
    def has(self, value):
        if(self.inf_inclusive==True):
            if(self.sup_inclusive==True):
                if(value >= self.inf and value <= self.sup):
                   return True

            elif(self.sup_inclusive==False):
                if(value >= self.inf and value < self.sup):
                    return True


        elif(self.sup_inclusive==True):
            if(self.inf_inclusive==True):
                if(value >= self.inf and value <= self.sup):
                    return True

            elif(self.inf_inclusive==False):
                if(value > self.inf and value <= self.sup):
                    return True


        else:return False