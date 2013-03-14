__author__ = 'chrispess'

from openehr.rm.data_structure.DATA_STRUCTURE import DATA_STRUCTURE
from openehr.rm.data_structure.ITEM_STRUCTURE.ITEM_STRUCTURE import ITEM_STRUCTURE
from openehr.rm.datatypes.quantity.DATE_TIME.DV_DATE_TIME import DV_DATE_TIME
from openehr.rm.datatypes.quantity.DATE_TIME.DV_DURATION import DV_DURATION
from openehr.BASIC_TYPES import typeInt

#objeto raiz de uma  história linear
class HISTORY(DATA_STRUCTURE):

 #tempo da origem desse evento do tipo history
 origin = DV_DATE_TIME(dia = typeInt, hora = typeInt, minuto = typeInt , segundo = typeInt)

 #os eventos dessa serie
 events = []

 #periodo entre amostras neste segmento (se for periódico)
 period = DV_DURATION

 #duração da história inteira
 duration = DV_DURATION


 #opcional. texto ou imagem que
 # sumariza a história inteira
 summary = ITEM_STRUCTURE

 #construtor
 def __init__(self, origin = DV_DATE_TIME (typeInt, hora = typeInt, minuto = typeInt , segundo = typeInt)):
     self.origin = origin

