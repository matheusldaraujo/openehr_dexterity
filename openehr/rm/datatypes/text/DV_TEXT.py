# -*- coding: utf-8 -*-

__author__ = 'chrispess'


from openehr.rm.datatypes.basic import DATA_VALUE
from openehr.rm.datatypes.uri import DV_URI
from openehr.rm.datatypes.text import CODE_PHRASE

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
  hyperlink = DV_URI()

  #indicador opcional da linguagem em que 'value' é escreto
  language = CODE_PHRASE()

  #nome do eschema de caracteres em que 'value' é encodado
  encoding = CODE_PHRASE()

  #construtor
  def __init__(self, value, mappings, formatting, hyperlink, language, encoding):
      self.value = value
      self.mappings = mappings
      self.formatting = formatting
      self.hyperlink = hyperlink
      self.language = language
      self.encoding = encoding







