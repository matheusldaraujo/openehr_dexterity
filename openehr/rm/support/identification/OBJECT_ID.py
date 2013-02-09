# -*- coding: utf-8 -*-
__author__ = 'chrispess'


#classe ancestral dos identificadores de identification package

class OBJECT_ID():

    value = str() #valor da id do objeto. sempre != vazio


    #consrutor. recebe value como argumento
    def __init__(self, value):

        self.value = value

    #seta um valor
    def setObjectID(self, value):
        self.value = value


     #retorna value
    def getObjectID(self):
        return  self.value


    #verifica igualdade comparando o objeto com outro passado como parâmetro
    def equal(self, other):
        if(self.value == other):
            return True
        else:return False



