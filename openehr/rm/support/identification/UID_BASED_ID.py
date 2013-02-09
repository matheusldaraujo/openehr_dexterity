# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.support.identification.OBJECT_ID import OBJECT_ID
from openehr.rm.support.identification.UID import UID



# modelo para um identificador UID-based, consistindo de duas partes: 'root' e uma
# parte opcional 'extension'. forma lexica: root::extension


class UID_BASED_ID(OBJECT_ID):

    value = [] # onde value = root [::extension]

    #TODO Matheus: Passando valor dumie
    root = UID(5)

    extension = str()

    #construtor
    def __init__(self,root,extension):
        self.root = root
        self.extension = extension

        self.value.append(root)
        self.value.append("::")
        self.value.append(extension)

    #construtor sem extension
    def __init__(self,root):
        self.root = root
        self.value.append(root)


    #retorna true se extension não for vazio
    def hasExtension(self):
        if(self.extension != None):
            return True

    #retorna a parte root à esquerda do separador '::'
    def Root(self):
        return self.root

    #retorna a parte extension à direita do separador '::'
    def Extension(self):
        return self.extension

