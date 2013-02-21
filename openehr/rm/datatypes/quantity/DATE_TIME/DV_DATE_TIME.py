__author__ = 'chrispess'

from datetime import datetime
from datetime import date
from openehr.rm.datatypes.quantity.DATE_TIME.DV_TEMPORAL import Dv_TEMPORAL

class DV_DATE_TIME(Dv_TEMPORAL):

    #data e tempo na forma YYYY-mm-dd  HH:mm:ss
    value = datetime

    def __init__(self, ano, mes, dia, hora, minuto , segundo):
        #define o objeto datetime, value
        self.value = datetime(ano, mes, dia, hora, minuto,segundo)


