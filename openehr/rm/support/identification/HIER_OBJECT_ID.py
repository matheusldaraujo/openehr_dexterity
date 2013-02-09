# -*- coding: utf-8 -*-
__author__ = 'chrispess'


from openehr.rm.support.identification.UID_BASED_ID import UID_BASED_ID

class HIER_OBJECT_ID(UID_BASED_ID):

    value = str


    #construtor
    def __init__(self, value):
        self.value = value


