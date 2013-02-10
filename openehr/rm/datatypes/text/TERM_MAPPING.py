__author__ = 'chrispess'

from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE
from openehr.rm.datatypes.text.DV_CODED_TEXT import DV_CODED_TEXT
from openehr.BASIC_TYPES import typechar



class TERM_MAPPING():

  # o termo alvo do mapeamento
  target = CODE_PHRASE()

  #correspondência relativa do termo alvo com respeito ao item de texto mapeado.
  # os resultados podem ter os seguintes significados:
  # '>': o mapeamento é mais amplo. ex: texto original = "arbovirus infection"
  # e o target = 'viral infection'
  # '=': mapeamento éequivalente ao termo original
  # '<': o mapeamento é menos amplo. ex: textooriginal = 'diabetes'
  # e o target = 'diabetes mellitus'
  #'?': desconhecido
  match = typechar()

  #proposito do mapeamento. ex: "interoperabilidade", "automação de data mining"...
  purpose =  DV_CODED_TEXT()


  #construtor
  def __init__(self,target,match,purpose):
      self.target =target
      self.match = match
      self.purpose = purpose






