from Predicate import Predicate

class PredicateEndsBeforeTime(Predicate):
    def __init__(self, name, agent, time):
        super(PredicateEndsBeforeTime, self).__init__(name, agent)
        self.time = time
        self.generatePredicate()

    def generatePredicate(self):
        and_str = 'and( #1#, #2#)'

        cycle       = self.agent.powerInfo()
        time_steps  = self.agent.time_steps

        max_cons    = max(cycle)

        and_str_cycle_is_continuous = and_str
        for time_step in range(0, time_steps):
            value = max_cons if time_step <= self.time else 0
            le_str = 'le(X{}, {})'.format(time_step, value)
            if time_step == (time_steps - 1):
                and_str_cycle_is_continuous = and_str_cycle_is_continuous.replace(and_str, le_str)
            else:
                and_str_cycle_is_continuous = and_str_cycle_is_continuous.replace('#2#', le_str).replace('#1#', and_str)

        # Imposto le variabli che saranno usate per generare il predicato effettivo
        self.expr          = and_str_cycle_is_continuous
        self.num_of_params = time_steps