__author__ = 'chrispess'

from openehr.BASIC_TYPES import typeStr
from openehr.rm.datatypes.basic.DV_IDENTIFIER import DV_IDENTIFIER

class PARTY_IDENTIFIED(object):
   #opcional, nome legível
   name = typeStr

   #um ou mais identificadores
   identifiers = DV_IDENTIFIER[]

   #construtor
   def __init__(self, *args):
       if(len(args)==1):
           self.name = args[0]

       elif(len(args)==2):
           self.name = args[0]
           self.identifiers = args[1]


   #seta name
   def setName(self, name = typeStr):
       self.name = name

   #seta identifiers
   def setIdentifiers(self,identifiers = DV_IDENTIFIER[]):
       self.identifiers = identifiers

   #retorna name
   def getName(self):
       return self.name

   #retorna identifiers
   def getIdentifiers(self):
       return self.identifiers

