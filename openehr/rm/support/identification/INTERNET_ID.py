__author__ = 'chrispess'

from openehr.rm.support.identification import UID

#usado como identificador único de um domínio de internet

class INTERNET_ID(UID):

    value = str()

    # construtor
    def __init__(self, value):
       self.value = value
