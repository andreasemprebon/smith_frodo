from Predicate import Predicate

class PredicateContinuity(Predicate):
    def __init__(self, name, agent):
        super(PredicateContinuity, self).__init__(name, agent)
        self.generatePredicate()

    def generatePredicate(self):
        and_str = 'and( #1#, #2#)'
        or_str  = 'or( @1@, @2@)'

        cycle       = self.agent.powerInfo()
        duration    = len(cycle)
        time_steps  = self.agent.time_steps

        cycle_is_continuous = or_str

        possible_starts = self.agent.time_steps - duration

        for possible_start in range(0, possible_starts):
            and_str_cycle_is_continuous = and_str

            cycle_vec = [0] * time_steps
            cycle_vec[possible_start : possible_start+duration] = cycle

            for t in range(0, time_steps):
                eq_str = 'eq(X{}, {})'.format(t, cycle_vec[t])
                if t == (time_steps - 1):
                    and_str_cycle_is_continuous = and_str_cycle_is_continuous.replace(and_str, eq_str)
                else:
                    and_str_cycle_is_continuous = and_str_cycle_is_continuous.replace('#2#', eq_str).replace('#1#', and_str)

            if possible_start == (possible_starts - 1):
                cycle_is_continuous = cycle_is_continuous.replace(or_str, and_str_cycle_is_continuous)
            else:
                cycle_is_continuous = cycle_is_continuous.replace('@2@', and_str_cycle_is_continuous).replace('@1@', or_str)

        # Imposto le variabli che saranno usate per generare il predicato effettivo
        self.expr          = cycle_is_continuous
        self.num_of_params = time_steps