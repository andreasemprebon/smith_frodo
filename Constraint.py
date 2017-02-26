from lxml import etree

class Constraint():
    def __init__(self, name, agent, variables):
        self.name       = name
        self.agent      = agent
        self.variables  = variables
        self.predicate  = None
        self.function   = None
        self.reference  = None

    def setPredicate(self, predicate):
        self.predicate = predicate
        self.setReference( self.predicate.name )

    def setFunction(self, function):
        self.function = function
        self.setReference( self.function.name )

    def setReference(self, reference):
        self.reference = reference

    def setParams(self, params_list):
        self.params = None

    def node(self):
        scope = ' '.join( str(var.name) for var in self.variables )

        node = etree.Element("constraint",
                             name       = self.name,
                             arity      = str( len( self.variables ) ),
                             scope      = scope,
                             reference  = self.reference
                             )
        parameters = etree.Element("parameters")
        parameters.text = self.params

        node.append(parameters)

        return node