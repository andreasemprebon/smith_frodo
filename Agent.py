from lxml import etree

class Agent():
    def __init__(self, name, time_steps):
        self.name               = name
        self.time_steps         = time_steps
        self.isProducingPower   = False
        self.variables          = []
        self.constraints        = []

    def isProducingPower(self):
        return self.isProducingPower

    def powerInfo(self):
        return None

    def node(self):
        node = etree.Element("agent", name = self.name)
        return node