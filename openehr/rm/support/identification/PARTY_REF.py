# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.support.identification.OBJECT_REF import OBJECT_REF

from openehr.rm.support.identification.OBJECT_ID import OBJECT_ID
from openehr.BASIC_TYPES import typeStr


class PARTY_REF(OBJECT_REF):

 #id referenciando participante de um serviço identificado
 id = OBJECT_ID(typeStr)

 #namespace
 namespace = typeStr

 #tipo
 type = typeStr

 #construtor
 def __init__(self, id = OBJECT_REF(typeStr),namespace = typeStr, type = typeStr):
     #chama o superconstrutor
     super(PARTY_REF,self).__init__()
     self.id = id
     self.namespace = namespace
     self.type = type








