from XCSPNode import XCSPNode

class XCSPNodeFunctions(XCSPNode):
    def __init__(self):
        super(XCSPNodeFunctions, self).__init__()
        self.node_name = "functions"
        self.nb_name = "nbFunction"

    def addFunction(self, function):
        self.elements.append( function )