__author__ = 'chrispess'

from openehr.rm.data_structure.DATA_STRUCTURE import DATA_STRUCTURE
from openehr.rm.datatypes.quantity.DATE_TIME.DV_DATE_TIME import DV_DATE_TIME
from openehr.BASIC_TYPES import typeInt

#objeto raiz de uma  história linear
class HISTORY(DATA_STRUCTURE):

 origin = DV_DATE_TIME(dia = typeInt, hora = typeInt, minuto = typeInt , segundo = typeInt)

 #construtor
 def __init__(self, origin = DV_DATE_TIME (typeInt, hora = typeInt, minuto = typeInt , segundo = typeInt)):
     self.origin = origin

