__author__ = 'chrispess'

#superclasse abstrata que define o conceito de valores quantificáveis, ordenados e com precisão na magnitude

from openehr.rm.datatypes.quantity import DV_ORDERED


class DV_QUANTIFIED(DV_ORDERED):



#atributos mandatórios

 magnitude_status = "magnitude_status"


#construtores

def __init__(self):

 pass

def __init__(self, magnitude_status):

 self.magnitude_status = magnitude_status


#retorna magnitude_status
def getMagnitudeStatus(self):
    return self.magnitude_status

