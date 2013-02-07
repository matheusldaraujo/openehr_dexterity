__author__ = 'chrispess'

from openehr.rm.support.identification import OBJECT_REF

from openehr.rm.support.identification import OBJECT_ID



class PARTY_REF(OBJECT_REF):


  id = OBJECT_ID()  #id unico de um objeto. != null


  type = str()      #nome da classe do objeto aque o identificador se refere. !=null


  #construtor
  def __init__(self, id, type):
    self.id = id
    self.type = type



