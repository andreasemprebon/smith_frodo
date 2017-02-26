from lxml import etree

class XCSPNode():
    def __init__(self):
        self.node_name  = ""
        self.nb_name    = ""
        self.elements   = list()

    def node(self):
        node = etree.Element( self.node_name )
        node.set(self.nb_name, str( int( len( self.elements ) ) ) )

        for elem in self.elements:
            node.append( elem.node() )

        return node
