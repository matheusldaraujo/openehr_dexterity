__author__ = 'chrispess'


from openehr.rm.datatypes.quantity.DV_AMOUNT import DV_AMOUNT
from openehr.BASIC_TYPES import typeInt


class DV_COUNT(DV_AMOUNT):

    #representa a magnitude numérica da quantidade
    magnitude = typeInt()

    #construtor
    def __init__(self, magnitude):
        self.magnitude = magnitude





