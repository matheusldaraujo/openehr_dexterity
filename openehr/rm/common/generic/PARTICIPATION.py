__author__ = 'chrispess'

from openehr.rm.common.generic.PARTY_PROXY import PARTY_PROXY
from openehr.rm.datatypes.text.DV_TEXT import DV_TEXT
class PARTICIPATION(object):

    # o id de participantes na atividade
    performer = PARTY_PROXY()

    #a função do participante. pode ser codificado
    function = DV_TEXT


