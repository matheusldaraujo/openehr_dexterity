__author__ = 'chrispess'


from openehr.rm.datatypes.text.DV_CODED_TEXT import DV_CODED_TEXT
from openehr.BASIC_TYPES import typeBool

#nome do estado. determinados pela tabela'state/event'
# codificada utilizando terminologia OpenEHR
value = DV_CODED_TEXT() #value != vazio

#indica quando é um estado terminal, como "aborted","completed", etc
is_terminal = typeBool() # is_terminal != vazio

