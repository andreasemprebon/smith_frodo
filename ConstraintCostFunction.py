from Constraint import Constraint
from CostFunction import CostFunction

class ConstraintCostFunction(Constraint):
    def __init__(self, name, agents, variables, cost, tau):
        self.cost = cost
        self.tau  = tau

        costFun = CostFunction(name, agents, cost, tau)

        super(ConstraintCostFunction, self).__init__(name, agents, variables)
        self.setFunction( costFun )

        self.params = ' '.join(str(var.name) for var in self.variables)