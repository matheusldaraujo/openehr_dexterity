__author__ = 'chrispess'

from openehr.rm.datatypes.quantity.DV_ABSOLUTE_QUANTITY import DV_ABSOLUTE_QUANTITY
from openehr.BASIC_TYPES import typeStr
from datetime import datetime

class Dv_TEMPORAL(DV_ABSOLUTE_QUANTITY):

    #construtor
    def __init__(self):
        pass


    #diferença entreduas quantidades temporais
    def diff(self, other):

     super(Dv_TEMPORAL, self).__init__()

     return self.diff(other)