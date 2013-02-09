# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.support.identification import UID

class UUID(UID):

  value = str()


  # construtor
  def __init__(self, value):
      self.value = value

