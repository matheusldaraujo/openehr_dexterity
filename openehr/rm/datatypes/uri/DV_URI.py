# -*- coding: utf-8 -*-

__author__ = 'chrispess'

from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE

    #####verificar se o python possui alguma biblioteca como o java.net.URI,
    # que retorna path, scheme, fragment_id do string value. Em
    # caso afirmativo, sobrescrever os métodos...

class DV_URI(DATA_VALUE):


 value = str


 def __init__(self, value):
     self.value = value


 def getValue(self):
     return self.value