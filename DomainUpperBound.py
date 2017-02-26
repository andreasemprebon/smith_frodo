from Domain import Domain

class DomainUpperBound(Domain):
    def __init__(self, var, agent, t):
        super(DomainUpperBound, self).__init__(var, agent)
        self.time_step = t
        self.computeDomain()

    def computeDomain(self):
        cycle    = self.agent.powerInfo()

        self.addAdmissableValues( range(0, cycle[ self.time_step ] + 1) )