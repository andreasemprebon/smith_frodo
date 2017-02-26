from Constraint import Constraint
from PredicateContinuity import PredicateContinuity

class ConstraintContinuity(Constraint):
    def __init__(self, name, agent, variables):
        pred = PredicateContinuity(name, agent)
        super(ConstraintContinuity, self).__init__(name, agent, variables)
        self.setPredicate(pred)
        self.params = ' '.join(str(var.name) for var in self.variables)