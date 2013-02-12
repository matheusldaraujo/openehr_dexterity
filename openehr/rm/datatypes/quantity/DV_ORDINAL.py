__author__ = 'chrispess'

from openehr.BASIC_TYPES import typeInt
from openehr.BASIC_TYPES import typeStr
from openehr.rm.datatypes.text.DV_CODED_TEXT import DV_CODED_TEXT
from openehr.rm.datatypes.quantity.DV_ORDERED import DV_ORDERED

class DV_ORDINAL(DV_ORDERED):

 #valor numa enumeraçãode valores. Qualquer inteiro pode ser usado
 value = typeInt()

 symbol = DV_CODED_TEXT(typeStr)


