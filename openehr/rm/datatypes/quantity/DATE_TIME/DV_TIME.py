# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from  openehr.rm.datatypes.quantity.DATE_TIME.DV_TEMPORAL import Dv_TEMPORAL
from  openehr.BASIC_TYPES import typeStr

class DvTime(Dv_TEMPORAL):

    #ISO 8601 time string
    value = typeStr

    #construtor
    def __init__(self, value):
        self.value = value


    #seta value
    def setValue(self, value):
        self.value = value


    #retorna valor numérico do tempo em segundos desde o início do dia
    def magnitude(self):
        pass
