 # -*- coding: utf-8 -*-
__author__ = 'chrispess'


#classe criada para definir o conceito de valores ordenados

from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.rm.datatypes.quantity import DV_INTERVAL
from openehr.rm.datatypes.text.DV_CODED_TEXT import DV_CODED_TEXT
from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE
from openehr.rm.support.identification.TERMINOLOGY_ID import TERMINOLOGY_ID
from openehr.BASIC_TYPES import typeStr


#classe abstrata que define o conceito de valores ordenados
class DV_ORDERED(DATA_VALUE):

  otherReferenceRange =

  normal_range = DV_INTERVAL(0,0)

  normal_status = CODE_PHRASE(teminology_id = TERMINOLOGY_ID(), code_string = typeStr)





