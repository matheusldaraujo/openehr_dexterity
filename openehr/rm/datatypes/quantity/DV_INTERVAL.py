__author__ = 'chrispess'

from openehr.rm.support.basic.Interval import Interval
from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.rm.support.basic.Interval import Interval

#classe genérica para definião de um intervalo.
# Usada para definir intervalos de datas, tempo, quantidades

class DV_INTERVAL(DATA_VALUE):

 interval = Interval(0, 0)


 #construtor
 def __init__(self, lower, upper):
     self.interval.set_inf(lower)
     self.interval.set_sup(upper)



 def has(self, value):
     if(self.interval.has(value)==True):
         return True
     else:return False