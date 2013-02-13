# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.support.identification.UID_BASED_ID import UID_BASED_ID
from openehr.rm.support.identification.UID import UID
from openehr.rm.support.identification.VERSION_TREE_ID import VERSION_TREE_ID

# classe para gerar um identificador unico para uma versão deum objeto versionado

# a forma da string de um OBJECT_VERSION_ID associada ao atributo value consiste
# em três segmentos separados por duplo dois pontos (::)
# value = objectID + '::'+ creatingSystemID + '::' + versionTreeID
# Exemplo: F7C5C7B7-75DB-4b39-9A1E-C0BA9BFDBDEC::87284370-2D4B-4e3d-A3F3-F303D2F4F34B::2

from openehr.BASIC_TYPES import typeStr

class OBJECT_VERSION_ID(UID_BASED_ID):

    #TODO Matheus: Passando valor dumie
    objectID =UID(5)
    #TODO Matheus: Passando valor dumie
    creatingSystemID = UID(5)
    #TODO Matheus: Passando valor dumie
    versionTreeID = VERSION_TREE_ID(5,5,5,5)

    value = typeStr[]


    #construtor

    def __init__(self, objectID, creatingSystemID, versionTreeID):
        self.objectID = objectID
        self.creatingSystemID = creatingSystemID
        self.versionTreeID = versionTreeID


        self.value.append(self,objectID.toString()) #verificar se chamada de método
        self.value.append(self,"::")                #está correta
        self.value.append(self,creatingSystemID.toString())
        self.value.append(self,"::")
        self.value.append(self,versionTreeID.toString())


    def __init__(self, objectID = str(), creatingSystemID = str(), versionTreeID = str()):

        self.value.append(self,objectID) #verificar se chamada de método
        self.value.append(self,"::")                #está correta
        self.value.append(self,creatingSystemID)
        self.value.append(self,"::")
        self.value.append(self,versionTreeID)


    #retorna objectID
    def ObjectID(self):
        return self.objectID

    #retorna creatingSystemID
    def  CreatingSystemID(self):
        return self.creatingSystemID

    #retorna VersionTreeID
    def VersionTreeID(self):
        return self.versionTreeID


    #retorna value
    def getValue(self):
        return self.value

    #seta o valor da string value
    def setValue(self, value):
        self.value = value


