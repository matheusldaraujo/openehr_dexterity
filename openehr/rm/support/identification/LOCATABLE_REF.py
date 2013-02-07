__author__ = 'chrispess'


from openehr.rm.support.identification import OBJECT_REF
from openehr.rm.support.identification import OBJECT_VERSION_ID

class LOCATABLE_REF(OBJECT_REF):


    id = OBJECT_VERSION_ID #identificador da versão

    path = str()

    as_uri =[] # uri criada pela concatenação de "ehr://" + id.value + "/" + path

    type = str()

    namespace = str()

    #construtor full
    def __init__(self, id, namespace, type, path):
        self.id = id
        self.namespace = namespace
        self.type = type
        self.path = path


    #constrói e retorna as_uri
    def asURI(self):
        self.as_uri.append("ehr://")
        self.as_uri.append(self.id.getValue())
        self.as_uri.append("/")
        self.as_uri.append(self.path)

    #retorna path
    def getPath(self):
        return self.path


    #seta o path
    def setPath(self, path):
        self.path = path


