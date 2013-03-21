__author__ = 'chrispess'

from openehr.rm.common.generic.PARTY_IDENTIFIED import PARTY_IDENTIFIED
from openehr.rm.datatypes.basic.DV_IDENTIFIER import DV_IDENTIFIER
from openehr.rm.datatypes.quantity.DATE_TIME.DV_DATE_TIME import DV_DATE_TIME
from openehr.rm.common.generic.PARTICIPATION import PARTICIPATION
from openehr.rm.datatypes.text.DV_CODED_TEXT import DV_CODED_TEXT
from openehr.rm.support.identification.TERMINOLOGY_ID import TERMINOLOGY_ID
from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE
from openehr.rm.data_structure.ITEM_STRUCTURE import ITEM_STRUCTURE
from openehr.BASIC_TYPES import typeInt
from openehr.BASIC_TYPES import typeStr

class EVENT_CONTEXT(object):


    #opcional. Descrição original:"The health care facility under
    #whose care the event took place."
    health_care_facility = PARTY_IDENTIFIED(identifiers = DV_IDENTIFIER[])

    #início da sessão clínica ou outro tipo de evento referente ao paciente
    start_time = DV_DATE_TIME(dia = typeInt, hora = typeInt, minuto = typeInt , segundo = typeInt)

    #opcional. fim da sessão clínica
    end_time = DV_DATE_TIME(dia = typeInt, hora = typeInt, minuto = typeInt , segundo = typeInt)

    #opcional. outros envolvidos no evento de cuidado
    participations = PARTICIPATION[]

    #opcional. atual localização onde ocorreu a sessão
    location = typeStr

    #opcional. codificado pela OpenEHR Terminology
    setting = DV_CODED_TEXT(defining_code = CODE_PHRASE( teminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr), code_string=typeStr))

    #opcional. outros dados de contexto
    other_context = ITEM_STRUCTURE

