__author__ = 'chrispess'

class VERSION_TREE_ID:

# formato lexico
# value: trunkVersion ['.' branchNumber '.' branchVersion]

    value = str() #string com a formado identificador


    trunkVersion = str()  #inicia com 1


    branchNumber = str()  #inicia com 1


    branchVersion = str()   #inicia com 1



    #construtor
    def __init__(self, value, trunkVersion, branchNumber, branchVersion):
        self.value =  value
        self.trunkVersion = trunkVersion
        self.branchNumber = branchNumber
        self.branchVersion = branchVersion


    #retorna true se o identificador representa um branch
    def isBranch(self):
        if(self.branchVersion != None):
            return True
        else:return False


    # retorna true se é a primeira cópia numa árvore de versões
    def isFirst(self):
        if(self.trunkVersion == "1"):
            return True
        else:return False

    # retorna branchVersion
    def branchVersion(self):
        return self.branchVersion


    #retorna branchNumber
    def branchNumber(self):
        return self.branchNumber

    #retorna trunkVersion
    def trunkVersion(self):
        return self.trunkVersion

    #retorna value
    def getValue(self):
        return self.value


    #verifica igualdade comparando o objeto com outro passado como parâmetro
    def equal(self, other):
        if(self.value == other.value):
            return True
        else:return False


