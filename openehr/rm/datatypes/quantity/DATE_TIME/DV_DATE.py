__author__ = 'chrispess'

from datetime import datetime
from openehr.rm.datatypes.quantity.DATE_TIME.DV_TEMPORAL import Dv_TEMPORAL
from openehr.BASIC_TYPES import typeInt
class DV_DATE(Dv_TEMPORAL):

    #ISO 8601 data string
    value = datetime

    #construtor
    def __init__(self,day = typeInt, month = typeInt, year = typeInt):
        self.value = datetime(day, month, year)

    #valor numérico da data em dias desde a origem do calendário 1/1/0000
    def magnitude(self):
        pass