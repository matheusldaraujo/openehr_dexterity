__author__ = 'chrispess'

from openehr.rm.datatypes.basic import DATA_VALUE
from openehr.rm.support.identification import TERMINOLOGY_ID

#classe que constroi uma codephrase utilizando umaterminologyID e ums codeString

#léxico: terminology_id = snomed-ct
#        code_string = nnnnnnnnn

class CODE_PHRASE(DATA_VALUE):

    #identificador da terminologia de onde o code_string foi extraido
    terminologyID = TERMINOLOGY_ID()


    #chave utilizada pelo serviço de terminologia para identificar um conceito
    codeString = str()


    #construtor
    def __init__(self, teminology_id, code_string):
        self.terminologyID = teminology_id
        self.codeString = code_string

    # retorna o string associado à codephrase
    def toString(self):
        return self.terminologyID + "," + self.codeString


    # retorna terminologyID
    def getTerminologyID(self):
        return self.terminologyID

    #retorna codeString
    def getCodeString(self):
        return self.codeString


    #seta terminologyID
    def setTerminologyID(self, terminology_id):
        self.terminologyID = terminology_id


    #seta codeString
    def setCodeString(self, code_string):
        self.codeString = code_string



