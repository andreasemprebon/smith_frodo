from XCSPNode import XCSPNode

class XCSPNodeAgents(XCSPNode):
    def __init__(self, xcspvar, xcspconst):
        super(XCSPNodeAgents, self).__init__()
        self.node_name = "agents"
        self.nb_name = "nbAgents"
        self.xcspvariables = xcspvar
        self.xcspconstraint = xcspconst

    def addAgent(self, agent):
        self.elements.append( agent )

        for v in agent.variables:
            self.xcspvariables.addVariable( v )

        for c in agent.constraints:
            self.xcspconstraint.addConstraint( c )