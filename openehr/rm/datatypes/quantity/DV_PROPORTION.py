__author__ = 'chrispess'


from openehr.BASIC_TYPES import typeFloat
from openehr.BASIC_TYPES import typeInt
from openehr.rm.datatypes.quantity.DV_AMOUNT import DV_AMOUNT
from openehr.rm.datatypes.quantity.PROPORTION_KIND import PROPORTION_KIND


class DV_PROPORTION(DV_AMOUNT):

   #numerador da razão
   numerator = typeFloat()

   #denominador da razão
   denominator = typeFloat()

   #indica o tipo da proporção
   type = PROPORTION_KIND()

   #expressa a precisão em termos decasas decimais. 0 -> integral,
   # -1 -> qualquer número decasas decimais
   precision = typeInt()


