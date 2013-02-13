# -*- coding: utf-8 -*-
__author__ = 'chrispess'


from openehr.rm.support.identification.OBJECT_ID import OBJECT_ID

#
#forma léxica name [ '('  version  ')'  ]

from openehr.BASIC_TYPES import typeStr

class TERMINOLOGY_ID(OBJECT_ID):

     name = typeStr

     version_id = typeStr

     value = []

     #construtor
     def __init__(self, name, version_id):
         self.name = name
         self.version_id = version_id


     #retorna versionID
     def version_id(self):
         return self.version_id


     #retorna name
     def name(self):
         return self.name


     #retorna value a partir de name e vesion_id
     def getValue(self, name, version_id):

         if(version_id == ""):
            self.value.append(name)
         else:
            self.value.append("(")
            self.value.append(version_id)
            self.value.append(")")


     #seta value
     def setValue(self, value):
         self.value = value



