__author__ = 'chrispess'


#classe ancestral dos identificadores de identification package

class OBJECT_ID():

    value = "" #valor da id do objeto. sempre != vazio


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

    #retorna string do objeto
    def toString(self):
        object_id = []
        object_id.append(self.value)
        return object_id

