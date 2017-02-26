from XCSPNode import XCSPNode

class XCSPNodeDomains(XCSPNode):
    def __init__(self):
        super(XCSPNodeDomains, self).__init__()
        self.node_name = "domains"
        self.nb_name = "nbDomains"

    def addDomain(self, domain):
        self.elements.append( domain )