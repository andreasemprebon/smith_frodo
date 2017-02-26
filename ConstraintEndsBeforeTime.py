from Constraint import Constraint
from PredicateEndsBeforeTime import PredicateEndsBeforeTime

class ConstraintEndsBeforeTime(Constraint):
    def __init__(self, name, agent, variables, time):
        self.time = time
        pred = PredicateEndsBeforeTime(name, agent, time)
        super(ConstraintEndsBeforeTime, self).__init__(name, agent, variables)

        self.setPredicate(pred)

        self.params = ' '.join(str(var.name) for var in self.variables)