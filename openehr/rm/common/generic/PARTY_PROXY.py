__author__ = 'chrispess'

from openehr.rm.support.identification.PARTY_REF import PARTY_REF
from openehr.rm.support.identification.OBJECT_REF import OBJECT_REF
from openehr.BASIC_TYPES import typeStr
class PARTY_PROXY():

    #0..1. referência opcional a maiores detalhes de identificção ou demográficos
    external_ref = PARTY_REF(id = OBJECT_REF(typeStr),namespace = typeStr, type = typeStr)

    #construtor
    def __init__(self, external_ref = PARTY_REF(id = OBJECT_REF(typeStr),namespace = typeStr, type = typeStr)):
        self.external_ref = external_ref