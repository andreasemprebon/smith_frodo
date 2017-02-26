from lxml import etree

class Variable():
    def __init__(self, name, agent):
        self.name   = name
        self.agent  = agent
        self.domain = None
        self.values = []

    def setDomain(self, domain):
        self.domain = domain

    def addAdmissableValues(self, values):
        self.values.extend( values )
        self.values = list( set(self.values) )  # Only unique values

    def node(self):
        return etree.Element("variable",
                             name   =   self.name,
                             domain =   self.domain.name,
                             agent  =   self.agent.name
                             )