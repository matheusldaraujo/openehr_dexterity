__author__ = 'chrispess'

from openehr.rm.data_structure.ITEM_STRUCTURE.REPRESENTATION.ITEM import ITEM

class CLUSTER(ITEM):

    #lista ordenada de items:clusters ou elements
    items = []

    #construtor
    def __init__(self, items):
        self.items = items

    #retorna a lista de  items
    def getItems(self):
        return self.items

    #seta a lista de items
    def setItems(self,items = []):
        self.items = items



