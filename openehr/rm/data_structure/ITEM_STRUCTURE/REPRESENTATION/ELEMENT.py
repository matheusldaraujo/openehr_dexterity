__author__ = 'chrispess'

from openehr.rm.datatypes.text.DV_CODED_TEXT import DV_CODED_TEXT
from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.rm.data_structure.ITEM_STRUCTURE.REPRESENTATION.ITEM import ITEM

class ELEMENT (ITEM):

 # data value desse nodo
 value = DATA_VALUE

 #tipo do null value: "indeterminado", "não perguntado"
 null_flavour = DV_CODED_TEXT()

 #construtor
 def __init__(self,value, null_flavour ):
     self.value = value
     self.null_flavour= null_flavour


 #seta value
 def setValue(self, value = DATA_VALUE):
     self.value = value

 #seta null_flavour
 def setNull_flavour(self, null_flavour = DV_CODED_TEXT):
     self.null_flavour = null_flavour

 #retorna value
 def getValue(self):
     return self.value

 #retorna null_flavour
 def getNullFlavour(self):
     return self.null_flavour



