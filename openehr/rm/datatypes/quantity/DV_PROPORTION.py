__author__ = 'chrispess'


from openehr.BASIC_TYPES import typeFloat
from openehr.BASIC_TYPES import typeInt
from openehr.rm.datatypes.quantity.DV_AMOUNT import DV_AMOUNT
from openehr.rm.datatypes.quantity.PROPORTION_KIND import PROPORTION_KIND


class DV_PROPORTION(DV_AMOUNT):

   numerator = typeFloat()
   denominator = typeFloat()
   type = PROPORTION_KIND()
   precision = typeInt()