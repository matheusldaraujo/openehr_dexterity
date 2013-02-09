# -*- coding: utf-8 -*-
__author__ = 'chrispess'

class Interval:

    # inf limite inferior dointervalo
    # sup limite superior do intervalo
    # boolean inf_inclusive true se intervalo fechado en inf, false se intervalo aberto em inf
    # boolean sup_inclusive true se intervalo fechado en sup, false se intervalo aberto em sup



    def __init__(self,inf,sup,inf_inclusive,sup_inclusive):
       # if sup < inf:
       #     lança uma exceção

        self.inf = inf
        self.sup = sup
        self.inf_inclusive = false if self.inf == null else true
        #TODO Matheus: Implementar self.sup_inclusive
        #self.sup_inclusive =   # criar condicional  inf==null ? false : truew

    #TODO Matheus: Código incoerente, verificar intenção
    # def __init__(self):
    # def __Interval__(self, inf, sup):
    #     self.__init__(inf, sup, True, True)


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


    #retorna
    def to_string(self):
        interval_str =[]
        interval_str.append(self.inf)
        interval_str.append(self.inf_inclusive)
        interval_str.append(self.sup)
        interval_str.append(self.sup_inclusive)

        return interval_str


