__author__ = 'chrispess'

from openehr.rm.datatypes.quantity.DATE_TIME.DV_DATE_TIME import DV_DATE_TIME
from openehr.rm.data_structure.ITEM_STRUCTURE.ITEM_STRUCTURE import ITEM_STRUCTURE
from openehr.rm.datatypes.quantity.DATE_TIME.DV_DURATION import DV_DURATION

#classe genérica que define a noção  abstrata
# de um evento simples numa série
class EVENT(object):

 #tempo do evento
 time = DV_DATE_TIME

 #data associada ao evento
 data = ITEM_STRUCTURE

 #opcional. estado da data para este evento
 state = ITEM_STRUCTURE


