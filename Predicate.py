from lxml import etree

class Predicate():
    def __init__(self, name, agent):
        self.name           = name
        self.agent          = agent
        self.num_of_params  = 0
        self.expr           = ""

    def node(self):
        node = etree.Element("predicate",
                             name = self.name)

        parameters = etree.Element("parameters")
        parameters.text = ' '.join("X{}".format(i) for i in range(0, self.num_of_params))

        expression = etree.Element("expression")
        functional = etree.Element("functional")

        functional.text = self.expr

        expression.append(functional)

        node.append(parameters)
        node.append(expression)

        return node