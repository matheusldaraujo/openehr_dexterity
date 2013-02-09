# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.support.identification.OBJECT_ID import OBJECT_ID

class TEMPLATE_ID(OBJECT_ID):

    value = str()

    def __init__(self, value):
        self.value= value


