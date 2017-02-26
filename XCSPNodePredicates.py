from XCSPNode import XCSPNode

class XCSPNodePredicates(XCSPNode):
    def __init__(self):
        super(XCSPNodePredicates, self).__init__()
        self.node_name = "predicates"
        self.nb_name   = "nbPredicates"

    def addPredicate(self, pred):
        self.elements.append( pred )