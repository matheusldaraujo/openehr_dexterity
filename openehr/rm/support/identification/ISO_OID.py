__author__ = 'chrispess'


from openehr.rm.support.identification import UID


class ISO_OID(UID):

    value = str()

# construtor
    def __init__(self, value):
        self.value = value


