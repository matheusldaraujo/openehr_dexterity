__author__ = 'chrispess'

from openehr.rm.datatypes.basic import DATA_VALUE

class DV_BOOLEAN(DATA_VALUE):

    #atributos


    #valor booleano do item
    value = False


    #construtor
    def __init__(self, value):
        self.value = value


    #retorna o valor booleano do item
    def getValue(self):
        return self.value

    #seta um valor booleano
    def __set__(self, value):
        self.value =value



