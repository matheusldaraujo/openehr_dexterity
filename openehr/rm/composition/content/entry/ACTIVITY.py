__author__ = 'chrispess'

from openehr.rm.data_structure.ITEM_STRUCTURE.ITEM_STRUCTURE import ITEM_STRUCTURE
from openehr.BASIC_TYPES import typeStr
from openehr.rm.datatypes.encapsulated.DV_PARSABLE import DV_PARSABLE
from openehr.rm.common.archetyped.LOCATABLE import LOCATABLE

class ACTIVITY(LOCATABLE):

    #descrião da ACTIVITY na  forma de uma estrutura
    description = ITEM_STRUCTURE

    #"timing" da ACTIVITY naforma de uma string parsable,
    # como ISO8601 OU HL7 GTS
    timing = DV_PARSABLE

    #padrão regular de expressão fechado pelos delimitadores '//',
    #indicando o identificador válido para archetipes ACTIONS
    # correspondendo à especificação da ACTIVITY
    #default "/.*/", significando qualquer archetype
    action_archetype_id = typeStr

