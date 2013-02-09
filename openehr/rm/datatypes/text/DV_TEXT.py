# -*- coding: utf-8 -*-

__author__ = 'chrispess'


from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.rm.datatypes.uri.DV_URI import DV_URI
from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE

#classe para representar qualquer
# tipo de item de texto atômico, codificado ou não codificado

class DV_TEXT(DATA_VALUE):

  #um item de texto que pode conter um arranjo de caracteres como palavras,
  # sentenças (um  DV_TEXT pode conter mais de uma palavra) com hyprlinks, inclusive.
  value = str()

  #termos de outras terminologias que mais se aproximam do termo expresso
  mappings = []

  #string formatado na forma "name:value;name:value...",
  # por exemplo "font-weight:bold; font-family:Arial; font "
  formatting = str()

  #link opcional
  #TODO Matheus: Dummie value attribute, setar Default ou adicionar aqui
  hyperlink = DV_URI(1)

  #indicador opcional da linguagem em que 'value' é escreto
  #TODO Matheus: Dummie value attribute, setar Default ou adicionar aqui
  language = CODE_PHRASE("terminologias","string")

  #nome do eschema de caracteres em que 'value' é encodado
  #TODO Matheus: Dummie value attribute, setar Default ou adicionar aqui
  encoding = CODE_PHRASE("terminologias","string")

  #construtor
  def __init__(self, value, mappings, formatting, hyperlink, language, encoding):
      self.value = value
      self.mappings = mappings
      self.formatting = formatting
      self.hyperlink = hyperlink
      self.language = language
      self.encoding = encoding







