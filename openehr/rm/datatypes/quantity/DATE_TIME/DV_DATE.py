# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from datetime import datetime
from datetime import date
from openehr.rm.datatypes.quantity.DATE_TIME.DV_TEMPORAL import Dv_TEMPORAL
from openehr.BASIC_TYPES import typeInt

#representa um ponto absoluto no tempo, conforme ocalendário gregoriano
# e especificado como um dia. semântica dada por ISO 8601
class DV_DATE(Dv_TEMPORAL):

    #ISO 8601 data string
    value = datetime

    #construtor
    def __init__(self,year = typeInt, month = typeInt, day = typeInt ):
        self.value = datetime(year, month, day)

    #retorna objeto date
    def getDate(self):
        return self.value

    #retorna a string associada à data
    def getDateStr(self):
        return self.value.strftime('%Y-%m-%d')



    #valor numérico da data em dias desde a origem do calendário 1/1/0000
    def magnitude(self):
        pass