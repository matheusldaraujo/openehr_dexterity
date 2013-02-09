# -*- coding: utf-8 -*-

__author__ = 'chrispess'


from openehr.rm.datatypes.basic import DATA_VALUE
from openehr.rm.datatypes.uri import DV_URI
from openehr.rm.datatypes.text import CODE_PHRASE

#classe para representar qualquer
# tipo de item de texto atômico, codificado ou não codificado

class DV_TEXT(DATA_VALUE):

  value = str()
  mappings = []
  formatting = str()
  hyperlink = DV_URI()
  language = CODE_PHRASE()
  encoding = CODE_PHRASE()

  #construtor
  def __init__(self, value, mappings, formatting, hyperlink, language, encoding):
      self.value = value
      self.mappings = mappings
      self.formatting = formatting
      self.hyperlink = hyperlink
      self.language = language
      self.encoding = encoding





