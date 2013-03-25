__author__ = 'chrispess'

from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE
from openehr.rm.common.generic.PARTY_PROXY import PARTY_REF
from openehr.rm.common.generic.PARTICIPATION import PARTICIPATION
from openehr.rm.support.identification.OBJECT_REF import OBJECT_REF
from openehr.BASIC_TYPES import typeBool
from openehr.BASIC_TYPES import typeStr
from openehr.rm.composition.content.CONTENT_ITEM import CONTENT_ITEM
from openehr.rm.support.identification.TERMINOLOGY_ID import TERMINOLOGY_ID


class ENTRY(CONTENT_ITEM):

    #linguagem em que a ENTRY é escrita. codificada pelo
    # openEHR code Set "languages"
    language = CODE_PHRASE(teminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr), code_string=typeStr)