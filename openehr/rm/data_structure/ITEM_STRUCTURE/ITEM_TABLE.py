# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.data_structure.ITEM_STRUCTURE.REPRESENTATION.CLUSTER import CLUSTER

#data structure do tipo table.
#No caso do OpenEHR, uma lista de Clusters

class ITEM_TABLE(CLUSTER):

 #representação de uma tabela como uma lista de clusters
 #TODO: Matheus CLUSTER precisa receber uma lista como argumentos
 #coloquei uma dummie lista para passar
  rows = CLUSTER([])

 #construtor
 ##TODO: Matheus CLUSTER precisa receber uma lista como argumentos
 #coloquei uma dummie lista para passar
  def __init__(self, rows = CLUSTER([])):
     self.rows = rows


  #retorna o número de linhas
  def rowCount(self):
    #TODO:Matheus colocando pass pois funcao precisa de corpo
    pass

  #retorna o número de  colunas
  def columnCount(self):
    #TODO:Matheus colocando pass pois funcao precisa de corpo
    pass

  #retorna uma lista com o nome das linhas
  def rowNames(self):
    #TODO:Matheus colocando pass pois funcao precisa de corpo
    pass

  #retorna umalista com o nome das colunas
  def columnNames(self):
    #TODO:Matheus colocando pass pois funcao precisa de corpo
    pass

  #retorna a í-ésima linha
  def ithRow(self):
    #TODO:Matheus colocando pass pois funcao precisa de corpo
    pass

