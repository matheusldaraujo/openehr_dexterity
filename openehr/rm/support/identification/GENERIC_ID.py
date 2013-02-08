__author__ = 'chrispess'

from openehr.rm.support.identification import OBJECT_ID

class GENERIC_ID(OBJECT_ID):


    value = str()

    scheme = str()


    #construtor
    def __init__(self, value, scheme):
        self.value = value
        self.scheme = scheme


    #retorna scheme
    def Scheme(self):
        return self.scheme


    #verifica se GENERIC_ID é igual
    def equals(self, other):
        if(self == other):
            return True
        else:return False
