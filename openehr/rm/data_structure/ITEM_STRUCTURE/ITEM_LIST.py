__author__ = 'chrispess'

from openehr.rm.data_structure.ITEM_STRUCTURE.ITEM_STRUCTURE import ITEM_STRUCTURE
from openehr.BASIC_TYPES import typeInt
class ITEM_LIST(ITEM_STRUCTURE):

    #representação de uma listade elementos
    items = []

    #consturtor
    def __init__(self, items = []):
        self.items = items


    #retorna a lista de items
    def getItems(self):
        return self.items


    #retorna o numero de elementos da  lista
    def getItemCount(self):
        return self.items.len()

    #retorna um elemento da lista
    def getIthItem(self, i = typeInt):
        return self.items[i]


