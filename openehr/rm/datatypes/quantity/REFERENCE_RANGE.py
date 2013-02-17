# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.rm.datatypes.text.DV_TEXT import DV_TEXT
from openehr.rm.support.basic.Interval import Interval
from openehr.rm.datatypes.quantity.DV_ORDERED import DV_ORDERED
from openehr.rm.datatypes.quantity.DV_INTERVAL import DV_INTERVAL


class REFERENCE_RANGE(DATA_VALUE):

    meaning = DV_TEXT()
    #TODO
    range = DV_INTERVAL()


    #construtor
    def __init__(self, meaning, range):
        self.meaning = meaning
        self.range = range

    #retorna range
    def getRange(self):
        return self.range


    #retorna meaning
    def getMeaning(self):
        return self.meaning


    #retorna true se value está no range
    def isInRange(self, value = DV_ORDERED): ###essa definição está correta???
        return self.range.has(value)



