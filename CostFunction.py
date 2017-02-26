from lxml import etree

class CostFunction():
    def __init__(self, name, agents, cost, tau):
        self.name   = name
        self.agents = agents
        self.cost   = cost
        self.tau    = tau

    def node(self):
        node = etree.Element( "function",
                              name = self.name )

        node.attrib['return'] = "int"

        parameters = etree.Element("parameters")
        parameters.text = ' '.join("X{}".format(i) for i in range(0, len(self.agents)))
        expression = etree.Element("expression")
        functional = etree.Element("functional")

        sum_str = 'add( #1#, #2#)'
        sum_str_cost_fun = sum_str
        for i in range(0, len( self.agents )):
            curr_agent = 'X{}'.format(i)

            if self.agents[i].isProducingPower:
                curr_agent = 'neg({})'.format(curr_agent)

            if i == (len(self.agents) - 1):
                sum_str_cost_fun = sum_str_cost_fun.replace(sum_str, curr_agent)
            else:
                sum_str_cost_fun = sum_str_cost_fun.replace('#2#', curr_agent).replace('#1#', sum_str)

        mul_str = 'mul({}, mul({}, {}) )'.format(sum_str_cost_fun, self.cost, self.tau)
        functional.text = mul_str

        expression.append(functional)
        node.append(parameters)
        node.append(expression)

        return node