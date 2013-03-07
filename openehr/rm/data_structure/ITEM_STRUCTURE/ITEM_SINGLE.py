__author__ = 'chrispess'


from openehr.rm.data_structure.ITEM_STRUCTURE.REPRESENTATION.ELEMENT import ELEMENT
from openehr.rm.data_structure.ITEM_STRUCTURE.ITEM_STRUCTURE import ITEM_STRUCTURE
from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.rm.datatypes.text.DV_CODED_TEXT import DV_CODED_TEXT
class ITEM_SINGLE(ITEM_STRUCTURE):

 item = ELEMENT(value = DATA_VALUE, null_flavour = DV_CODED_TEXT)

