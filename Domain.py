from Variable import Variable
from lxml import etree

class Domain():
    def __init__(self, var, agent):
        self.name   = "DOMAIN_" + var.name
        self.agent  = agent
        self.var    = var
        self.values = []

    def addAdmissableValues(self, values):
        self.values.extend(values)
        self.values = list(set(self.values))  # Only unique values

        self.var.addAdmissableValues( self.values )

    def node(self):
        node = etree.Element("domain",
                             name       =   self.name,
                             nbValues   =   str( len(self.values) )
                             )
        node.text = ' '.join(map(str, self.values))
        return node