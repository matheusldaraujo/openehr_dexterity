__author__ = 'chrispess'

from openehr.rm.common.generic.PARTY_PROXY import PARTY_PROXY
from openehr.rm.datatypes.text.DV_TEXT import DV_TEXT
from openehr.rm.datatypes.text.DV_CODED_TEXT import DV_CODED_TEXT
from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE
from openehr.rm.support.identification.TERMINOLOGY_ID import TERMINOLOGY_ID
from openehr.BASIC_TYPES import typeStr
from openehr.BASIC_TYPES import typeInt
from openehr.rm.datatypes.quantity.DATE_TIME.DV_DURATION import DV_DURATION

class PARTICIPATION(object):

    # o id de participantes na atividade
    performer = PARTY_PROXY()

    #a função do participante. pode ser codificado
    function = DV_TEXT(value = typeStr)

    #o modo em que houve a interação.
    # ex: presencial, por telefone, email, etc
    mode = DV_CODED_TEXT(defining_code = CODE_PHRASE( teminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr), code_string=typeStr))


    # o intervalo de tempo durante o qual a participação ocorreu
    # optou-se por utilizar a classe DV_DURATION para esta representação
    time = DV_DURATION(dia = typeInt, hora = typeInt, minuto = typeInt , segundo = typeInt)

    #construtor
    def __init__(self, *args):
        if(len(args)==3):
           self.performer = args[0]
           self.function = args[1]
           self.mode = args[2]

        elif(len(args)==4):
         self.performer = args[0]
         self.function = args[1]
         self.mode = args[2]
         self.time = args[3]

