__author__ = 'chrispess'

from openehr.rm.datatypes.quantity.DATE_TIME.DV_DATE_TIME import DV_DATE_TIME
from openehr.rm.data_structure.ITEM_STRUCTURE.ITEM_STRUCTURE import ITEM_STRUCTURE
from openehr.rm.datatypes.quantity.DATE_TIME.DV_DURATION import DV_DURATION
from openehr.BASIC_TYPES import typeInt

#classe genérica que define a noção  abstrata
# de um evento simples numa série
class EVENT(object):

 #tempo do evento
 time = DV_DATE_TIME (typeInt, hora = typeInt, minuto = typeInt , segundo = typeInt)

 #data associada ao evento
 data = ITEM_STRUCTURE

 #opcional. estado da data para este evento
 state = ITEM_STRUCTURE

 #duração do evento
 duration = DV_DURATION(dia = typeInt, hora = typeInt, minuto = typeInt , segundo = typeInt)

 #construtor
 def __init__(self, *args):
     if(len(args)==2):
         self.time = args[0]
         self.data = args[1]
     elif(len(args)==3):
         self.time = args[0]
         self.data = args[1]
         self.state = args[2]


 #seta duration (offset)
 def setDuration(self,duration = DV_DURATION(dia = typeInt, hora = typeInt, minuto = typeInt , segundo = typeInt)):
     self.duration = duration

 #retorna duration (offset)
 def offset(self):
     return self.duration
