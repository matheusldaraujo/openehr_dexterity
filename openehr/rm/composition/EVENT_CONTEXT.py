__author__ = 'chrispess'

from openehr.rm.common.generic.PARTY_IDENTIFIED import PARTY_IDENTIFIED
from openehr.rm.datatypes.basic.DV_IDENTIFIER import DV_IDENTIFIER
from openehr.rm.datatypes.quantity.DATE_TIME.DV_DATE_TIME import DV_DATE_TIME
from openehr.BASIC_TYPES import typeInt

class EVENT_CONTEXT(object):


    #opcional. Descrição original:"The health care facility under
    #whose care the event took place."
    health_care_facility = PARTY_IDENTIFIED(identifiers = DV_IDENTIFIER[])

    #início da sessão clínica ou outro tipo de evento referente ao paciente
    start_time = DV_DATE_TIME(dia = typeInt, hora = typeInt, minuto = typeInt , segundo = typeInt)

    #opcional. fim da sessão clínica
    end_time = DV_DATE_TIME(dia = typeInt, hora = typeInt, minuto = typeInt , segundo = typeInt)

    #outros envolvidos no evento de cuidado
    participations =