__author__ = 'chrispess'

from openehr.rm.data_structure.ITEM_STRUCTURE.REPRESENTATION.CLUSTER import CLUSTER

#data structure do tipo table.
#No caso do OpenEHR, uma lista de Clusters

class ITEM_TABLE(CLUSTER):

 #representação de uma tabela como uma lista de clusters
 rows = CLUSTER[]

 #construtor
 def __init__(self, rows = CLUSTER[]):
     self.rows = rows


 #retorna o número de linhas
 def rowCount(self):

