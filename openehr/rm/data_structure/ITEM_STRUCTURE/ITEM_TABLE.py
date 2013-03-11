__author__ = 'chrispess'

from openehr.rm.data_structure.ITEM_STRUCTURE.REPRESENTATION.CLUSTER import CLUSTER

#data structure do tipo table

class ITEM_TABLE(CLUSTER):

 rows = CLUSTER[]

 #construtor
 def __init__(self, rows = CLUSTER[]):
     self.rows = rows

