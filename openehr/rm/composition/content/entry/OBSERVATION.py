# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.data_structure.HISTORY.HISTORY import HISTORY
from openehr.rm.composition.content.entry.CARE_ENTRY import CARE_ENTRY

class OBSERVATION(CARE_ENTRY):

 #os dados da  observação, na forma de um
 # histórico de valores de complexidade variável
 #TODO Matheus comentei a linha abaixo pois history recebe diversos argumentos
 #Olhar se é plausível criar uma condição na classe ou argumentos default
 #data = HISTORY()

 #opcional. Salva o estado do sujeito
 #da observação duranto processo da observação
 #na forma de um histórico separado de valores
 #que podem ser de qualquer complexidade
 #TODO Matheus comentei a linha abaixo pois history recebe diversos argumentos
 #Olhar se é plausível criar uma condição na classe ou argumentos default
 #state = HISTORY()

 #construtor
 def __init__(self, *args):
     if(len(args)==1):
      self.data = args[0]
     elif(len(args)==2):
      self.data = args[0]
      self.state = args[1]


