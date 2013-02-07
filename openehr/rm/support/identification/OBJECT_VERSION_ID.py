__author__ = 'chrispess'

from openehr.rm.support.identification import UID_BASED_ID
from openehr.rm.support.identification import UID
from openehr.rm.support.identification import VERSION_TREE_ID

# classe para gerar um identificador unico para uma versão deum objeto versionado

# a forma da string de um OBJECT_VERSION_ID associada ao atributo value consiste
# em três segmentos separados por duplo dois pontos (::)
# value = objectID + '::'+ creatingSystemID + '::' + versionTreeID
# Exemplo: F7C5C7B7-75DB-4b39-9A1E-C0BA9BFDBDEC::87284370-2D4B-4e3d-A3F3-F303D2F4F34B::2

class OBJECT_VERSION_ID(UID_BASED_ID):

    objectID =UID()

    creatingSystemID = UID()

    versionTreeID = VERSION_TREE_ID()

    value = str()


    #construtor

    def __init__(self, objectID, creatingSystemID, versionTreeID):
        self.objectID = objectID
        self.creatingSystemID = creatingSystemID
        self.versionTreeID = versionTreeID

        self.value=[]
        self.value.append(self,objectID.toString()) #verificar se chamada de método
        self.value.append(self,"::")                #está correta
        self.value.append(self,creatingSystemID.toString())
        self.value.append(self,"::")
        self.value.append(self,versionTreeID.toString())


    def __init__(self, objectID, creatingSystemID, versionTreeID):
        self.value=[]
        self.value.append(self,objectID) #verificar se chamada de método
        self.value.append(self,"::")                #está correta
        self.value.append(self,creatingSystemID)
        self.value.append(self,"::")
        self.value.append(self,versionTreeID)


    #retorna objectID
    def getObjectID(self):
        return self.objectID

    #retorna creatingSystemID
    def  getCreatingSystemID(self):
        return self.creatingSystemID

    #retorna VersionTreeID
    def getVersionTreeID(self):
        return self.versionTreeID


    #seta o valor da string value
    def setValue(self, value):
        self.value = value


