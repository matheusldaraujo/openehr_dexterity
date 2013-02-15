# -*- coding: utf-8 -*-
__author__ = 'chrispess'
from openehr.BASIC_TYPES import typeStr
class VERSION_TREE_ID:

# formato lexico
# value: trunkVersion ['.' branchNumber '.' branchVersion]

    value = str #string com a formado identificador


    trunkVersion = typeStr  #inicia com 1


    branchNumber = typeStr  #inicia com 1


    branchVersion = typeStr  #inicia com 1



    #construtor
    def __init__(self, value, trunkVersion, branchNumber, branchVersion):
        self.value =  value
        self.trunkVersion = trunkVersion
        self.branchNumber = branchNumber
        self.branchVersion = branchVersion


    #retorna true se o identificador representa um branch
    def is_branch(self):
        if(self.branchVersion != None):
            return True
        else:return False


    # retorna true se é a primeira cópia numa árvore de versões
    def is_first(self):
        if(self.trunkVersion == "1"):
            return True
        else:return False

    # retorna branchVersion
    def branch_version(self):
        return self.branchVersion


    #retorna branchNumber
    def branch_number(self):
        return self.branchNumber

    #retorna trunkVersion
    def trunk_version(self):
        return self.trunkVersion

    #retorna value
    def getValue(self):
        return self.value


    #verifica igualdade comparando o objeto com outro passado como parâmetro
    def equal(self, other):
        if(self.value == other.value):
            return True
        else:return False


