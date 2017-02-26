from XCSPNode import XCSPNode

class XCSPNodeVariables(XCSPNode):
    def __init__(self, xcspdoms):
        super(XCSPNodeVariables, self).__init__()
        self.node_name = "variables"
        self.nb_name = "nbVariables"
        self.xcspdomains = xcspdoms

    def addVariable(self, var):
        self.elements.append( var )
        self.xcspdomains.addDomain( var.domain )