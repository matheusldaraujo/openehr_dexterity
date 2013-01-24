__author__ = 'chrispess'

class UID:  #essa classe pode ser abstrata em python?


    # cria um UID por valor
    #lança exceção para valor nulo

    def __init__(self, value):
        #criar uma exceção aqui para tratar value == nulo
        self.value = value


    # retorna o valor da id
    def __getvalue__(self):
        return self.value

    #retorna string representativo do valor
    def __str__(self):
        return

    # verifica se dois UID's possuem o mesmo valor
    def __eq__(self, other):
        return

    # retorna o hash code
    def __hash__(self):
        return



