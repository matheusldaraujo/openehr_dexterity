__author__ = 'chrispess'

from openehr.rm.support.identification import OBJECT_REF
from openehr.rm.support.identification import OBJECT_ID

#referência para um access group num accessGroupRef


class ACCESS_GROUP_REF(OBJECT_REF):

    id = OBJECT_ID()  #id unico de um objeto. != null



#construtor
    def __init__(self, id):
     self.id = id
