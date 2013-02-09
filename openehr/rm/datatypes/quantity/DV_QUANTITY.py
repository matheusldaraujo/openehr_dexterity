 # -*- coding: utf-8 -*-
__author__ = 'chrispess'


from openehr.rm.datatypes.quantity.DV_AMOUNT import DV_AMOUNT


class DV_QUANTITY(DV_AMOUNT):

    #atributos

    magnitude = 0.0  #doublegrandeza numérica

    precision = 0    # int  precisão em termos de valores decimais. 0 implica quantidade integral e -1 implioca nenhum limite

    units = ""       # String expressando unidades como kg/m2, mm[Hg], km/h,...


    #construtor

def __init__(self, magnitude, units, precision):

    self.magnitude = magnitude
    self.units = units
    self.precision = precision


    #métodos

    #retorna magnitude
def getMagnitude(self):
    return self.magnitude


    #retorna units
def getUnits(self):
    return self.units


    #retorna precisão
def getPrecision(self):
    return self.precision

    #seta precisão
def setPrecision(self, precision):
    self.precision = precision

    #seta magnitude
def setMagnitude(self, magnitude):
    self.magnitude = magnitude





