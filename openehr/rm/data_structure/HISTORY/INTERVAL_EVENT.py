__author__ = 'chrispess'

from openehr.BASIC_TYPES import typeInt
from openehr.BASIC_TYPES import typeStr
from openehr.rm.support.identification.TERMINOLOGY_ID import TERMINOLOGY_ID
from openehr.rm.data_structure.HISTORY.EVENT import EVENT
from openehr.rm.datatypes.quantity.DATE_TIME.DV_DURATION import DV_DURATION
from openehr.rm.datatypes.text.DV_CODED_TEXT import DV_CODED_TEXT
from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE
from openehr.rm.datatypes.quantity.DATE_TIME.DV_DATE_TIME import DV_DATE_TIME
#classeque define um único intervalo numa série
class INTERVAL_EVENT(EVENT):

    #largura do intervalo
    width = DV_DURATION(dia = typeInt, hora = typeInt, minuto = typeInt , segundo = typeInt)

    #função matemática referente à data desse event.
    # Ex: "media", "maximum", etc.
    math_function = DV_CODED_TEXT(CODE_PHRASE(teminology_id=TERMINOLOGY_ID(typeStr,typeStr), code_string=typeStr))

    #opcional. contador dos exemplos originais
    # aos quais o evento corresponde
    sample_count = typeInt


    #início do intervalo
    startTime = DV_DATE_TIME(dia = typeInt, hora = typeInt, minuto = typeInt , segundo = typeInt)

    #ponto inicial do intervalo desse evento
    def interval_start_time(self, startTime = DV_DATE_TIME(dia = typeInt, hora = typeInt, minuto = typeInt , segundo = typeInt)):
        self.startTime = startTime


    #seta width
    def setWidth(self,startTime = DV_DURATION(dia = typeInt, hora = typeInt, minuto = typeInt , segundo = typeInt) ):
        self.startTime = startTime

