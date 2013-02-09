# -*- coding: utf-8 -*-

__author__ = 'chrispess'

from openehr.rm.datatypes.text.DV_TEXT import DV_TEXT
from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE

#um item de texto cujo valor pode ser uma rubrica de uma terminologia controlada,
# em suma um DV_CODED_TEXT é a combinaão de uma CODE_PHRASE (um código) e a rubrica do termo,
# de um serviço de terminologias na linguagem em que foi autorado.

class DV_CODED_TEXT(DV_TEXT):


 defining_code = CODE_PHRASE() #a rubrica associada ao  'value'


 #construtor
 def __init__(self,definingCode, value, mappings, formatting, hyperlink, language, encoding):

    self.defining_code=definingCode  #este self valora o atributo defining_code definido acima


    super(DV_CODED_TEXT, self).__init__()
    self.value = value  #este self chama o atributo 'value' da superclasse DV_TEXT
    #demais atributos da super classe DV_TEXT
    self.mappings = mappings
    self.formatting = formatting
    self.hyperlink = hyperlink
    self.language = language
    self.encoding = encoding
    self.language = language




    #seta value e defining_code
    def setDefining_code(self,value, defining_code):
      self.defining_code - defining_code
      super(DV_CODED_TEXT,self).__init__()
      self.value= value



    #seta defining_code
    def setDefining_code(self, defining_code):
      self.defining_code - defining_code



    #retorna string value,defining_code
    def toString(self):
        return super(DV_CODED_TEXT,self).__init__().getValue()+self.defining_code


