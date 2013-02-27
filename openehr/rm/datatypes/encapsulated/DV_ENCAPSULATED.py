__author__ = 'chrispess'

from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE
from openehr.BASIC_TYPES import typeInt


class DV_ENCAPSULATED(DATA_VALUE):

 #
 charset = CODE_PHRASE
 # (opcional) indicador opcional da linguagem em que os dados são  escritos.
 language = CODE_PHRASE
 #tamanho original em bytes
 size = typeInt

 #construtor
 def __init__(self,charset,language):
     self.charset = charset
     self.language = language


 #retorna charset
 def getcharset(self):
     return self.charset
