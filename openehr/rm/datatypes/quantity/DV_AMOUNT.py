__author__ = 'chrispess'


from openehr.rm.datatypes.quantity.DV_QUANTIFIED import DV_QUANTIFIED

class DV_AMOUNT(DV_QUANTIFIED):


#atributos mandatórios

    accuracy = 0,0

    accuracyPercent = False


#construtor

def __init__(self, accuracy, accuracyPercent):
    self.accuracy = accuracy
    self.accuracyPercent = accuracyPercent

#retorna accuracy

def getAccuracy(self):
    return self.accuracy


#retorna accuracyPercent

def isAccuracyPercent(self):
    return self.accuracyPercent








