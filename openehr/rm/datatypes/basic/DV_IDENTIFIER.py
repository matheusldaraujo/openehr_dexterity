__author__ = 'chrispess'

from openehr.rm.datatypes.basic import DATA_VALUE

# classe para criaão deumidentificador

#atributos

issuer = ""

assigner = ""

id = ""

type = ""



class DV_IDENTIFIER(DATA_VALUE):

    #construtor

    def __init__(self, issuer, assigner, id, type):

        self.issuer = issuer
        self.assigner = assigner
        self.id = id
        self.type = type

    # metodos get
    def getIssuer(self):
        return self.issuer

    def getAssigner(self):
        return self.assigner

    def getId(self):
        return self.id

    def getType(self):
        return self.type


    # metodos set

    def setIssuer(self, issuer):
         self.issuer = issuer

    def setAssigner(self, assigner):
        self.assigner = assigner

    def setId(self, id):
        self.id = id

    def setType(self, type):
        self.type = type
