__author__ = 'chrispess'


from openehr.rm.datatypes.quantity import DV_AMOUNT


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




