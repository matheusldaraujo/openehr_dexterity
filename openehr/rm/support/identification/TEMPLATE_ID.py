__author__ = 'chrispess'

from openehr.rm.support.identification import OBJECT_ID

class TEMPLATE_ID(OBJECT_ID):

    value = str()

    def __init__(self, value):
        self.value= value


