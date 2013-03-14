__author__ = 'chrispess'

from openehr.BASIC_TYPES import typeInt
from openehr.rm.data_structure.HISTORY.EVENT import EVENT
from openehr.rm.datatypes.quantity.DATE_TIME.DV_DURATION import DV_DURATION
from openehr.rm.datatypes.text.DV_CODED_TEXT import DV_CODED_TEXT
#classeque define um único intervalo numa série
class INTERVAL_EVENT(EVENT):

    #largura do intervalo
    width = DV_DURATION

    #funao matemática referente à data desse event.
    # Ex: "media", "maximum", etc.
    math_function = DV_CODED_TEXT

    #opcional. contador dos exemplos originais
    # aos quais o evento corresponde
    sample_count = typeInt


    #ponto inicial do intervalo desse evento
    def interval_start_time(self):
