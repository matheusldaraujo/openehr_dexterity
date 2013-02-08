__author__ = 'chrispess'


from openehr.rm.support.identification import OBJECT_ID

#
#forma léxica name [ '('  version  ')'  ]

class TERMINOOLOGY_ID(OBJECT_ID):

     name = str()

     version_id = str()

     value = []

     #construtor
     def __init__(self, name, version_id):
         self.name = name
         self.version_id = version_id


     #retorna versionID
     def getVersionID(self):
         return self.version_id


     #retorna name
     def getName(self):
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



