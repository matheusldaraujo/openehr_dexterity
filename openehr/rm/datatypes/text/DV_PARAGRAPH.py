__author__ = 'chrispess'

from  openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from  openehr.rm.datatypes.text.DV_TEXT import DV_TEXT

class DV_PARAGRAPH(DATA_VALUE):


  items = DV_TEXT[]

