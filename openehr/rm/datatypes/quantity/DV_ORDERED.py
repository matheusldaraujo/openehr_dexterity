 # -*- coding: utf-8 -*-
__author__ = 'chrispess'


#classe criada para definir o conceito de valores ordenados

from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.rm.datatypes.quantity.DV_INTERVAL import DV_INTERVAL
#TODO: Matheus, Importando REFERENCE_RANGE uma classe que
# from openehr.rm.datatypes.quantity.REFERENCE_RANGE import REFERENCE_RANGE
from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE
from openehr.rm.support.identification.TERMINOLOGY_ID import TERMINOLOGY_ID
from openehr.BASIC_TYPES import typeStr
from openehr.BASIC_TYPES import typeFloat


#classe abstrata que define o conceito de valores ordenados
class DV_ORDERED(DATA_VALUE):
  pass
  # #valor opcional para um range normal
  # normal_range = DV_INTERVAL(typeFloat,typeFloat)

  # #lista de ranges opcionais para este valor neste contexto, em particular
  # otherReferenceRanges = REFERENCE_RANGE()

  # #opcional. indicador normal de status do valorcom respeito ao range normal
  # # ver OpenEHR terminology group "normal status"
  # normal_status = CODE_PHRASE(teminology_id = TERMINOLOGY_ID(), code_string = typeStr())


  # #TODO: Matheus python nao suporta overload de funcoes
  # #construtor
  # def __init__(self, normal_range, otherReferenceRanges, normal_status):
  #     self.normal_range = normal_range
  #     self.otherReferenceRanges = otherReferenceRanges
  #     self.normal_status = normal_status

  # # #construtor vazio
  # # def __init__(self):
  # #     pass

  # #construtor com range
  # def __init__(self,normal_range):
  #     self.normal_range = normal_range

  # #retorna true se o valor esta no range normal
  # def isNormal(self, value):
  #     if(self.normal_range.has(value)==True):
  #         return True

  # #retorna normal_range
  # def getNormalRange(self):
  #     return self.normal_range

  # #retorna normal status
  # def getNormalStatus(self):
  #     return self.normal_status

  # #retorna otherReferenceRanges
  # def getOtherReferenceRanges(self):
  #     return self.otherReferenceRanges

  # #retorna true se a quantidade não possui range de referência
  # def isSimple(self):
  #     if(self.otherReferenceRange == None):
  #         return True

  # #verifica se duas instâncias são estritamente comparáveis
  # def isStrictlyComparableTo(self, DV_ORDERED):
  #     pass