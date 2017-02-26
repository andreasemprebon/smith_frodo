from XCSPNode import XCSPNode

class XCSPNodeConstraint(XCSPNode):
    def __init__(self, xcsppredicate, xcspfunction):
        super(XCSPNodeConstraint, self).__init__()
        self.node_name = "constraints"
        self.nb_name = "nbConstraints"
        self.xcsppredicate = xcsppredicate
        self.xcspfunction  = xcspfunction

    def addConstraint(self, const):
        self.elements.append( const )

        if ( const.predicate ):
            self.xcsppredicate.addPredicate( const.predicate )

        if ( const.function ):
            self.xcspfunction.addFunction( const.function )
