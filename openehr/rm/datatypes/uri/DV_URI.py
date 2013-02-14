# -*- coding: utf-8 -*-

__author__ = 'chrispess'

from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.BASIC_TYPES import typeStr

    #referência objeto conforme Universal Resource Identifier (URI) standardt

class DV_URI(DATA_VALUE):

 #string representando o valor da URI
 value = typeStr

 #"espaço" em que a informação existe.
 # Simultaneamente especifica o espaço de
 # informação eo mecanismo para  acessar objetos nesse espaço.
 # ex: "ftp", "telnet", "mailto"
 scheme = typeStr

 def __init__(self, value):
     self.value = value


 def getValue(self):
     return self.value