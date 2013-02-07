__author__ = 'chrispess'

from openehr.rm.support.identification import OBJECT_ID
from openehr.rm.support.identification import UID

class UID_BASED_ID(OBJECT_ID):

    root=UID()

    extension = ""

    #construtor
    def __init__(self,root,extension):
        self.root = root
        self.extension =extension


    #retorna true se extension não for vazio
    def hasExtension(self):
        if(self.extension != None):
            return True