__author__ = 'chrispess'

class UID:  #essa classe pode ser abstrata em python?

    value = ""

    # cria um UID por valor
    #lança exceção para valor nulo

    def __init__(self, value):
        #criar uma exceção aqui para tratar value == nulo
        self.value = value


    # retorna o valor da id
    def getValue(self):
        return self.value

    #retorna string representativo do valor
    def toString(self):
        uid = []
        uid.append(self.value)
        return uid

    # verifica se dois UID's possuem o mesmo valor
    def equals(self, other):
        if(self == other):
            return True
        else:return False






