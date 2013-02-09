# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.support.identification.OBJECT_REF import OBJECT_REF

from openehr.rm.support.identification.OBJECT_ID import OBJECT_ID



class PARTY_REF(OBJECT_REF):


	#TODO Matheus: Passando valor dumie
  id = OBJECT_ID(5)  #id unico de um objeto. != null


  type = str()      #nome da classe do objeto aque o identificador se refere. !=null


  #construtor
  def __init__(self, id, type):
    self.id = id
    self.type = type



