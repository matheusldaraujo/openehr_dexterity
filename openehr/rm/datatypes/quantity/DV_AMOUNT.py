__author__ = 'chrispess'


from openehr.rm.datatypes.quantity.DV_QUANTIFIED import DV_QUANTIFIED

class DV_AMOUNT(DV_QUANTIFIED):


#atributos mandatórios

    accuracy = 0,0

    accuracyPercent = False


def __init__(self, accuracy, accuracyPercent):
    self.accuracy = accuracy
    self.accuracyPercent = accuracyPercent







