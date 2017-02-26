from Constraint import Constraint
from PredicateEndsBeforeTime import PredicateEndsBeforeTime

class ConstraintWeightedSum(Constraint):
    def __init__(self, name, agents, variables, comparison, right_hand):

        super(ConstraintWeightedSum, self).__init__(name, agents, variables)
        self.setReference('global:weightedSum')

        expr = "[ "

        for i in range(0, len(agents) ):
            weight = 1 if not agents[i].isProducingPower else -1
            expr += "{{ {} {} }} ".format( weight, variables[i].name )

        expr += "] "

        expr += "<{}/> {}".format(comparison, right_hand)

        self.params = expr