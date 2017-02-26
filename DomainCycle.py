from Domain import Domain

class DomainCycle(Domain):
    def __init__(self, var, agent, t):
        super(DomainCycle, self).__init__(var, agent)
        self.time_step = t
        self.computeDomain()

    def computeDomain(self):
        cycle    = self.agent.powerInfo()
        duration = len(cycle)

        #####
        # Esempio:
        # Ciclo: 5 8 10 15 20
        # t: 6
        # time_steps: 10
        # duration - (time_steps - t) = 5 - (10 - 6) = 1
        # Inizio a scegliere i valori da ciclo[1] e non da ciclo[0]
        # perche' se iniziassi da ciclo[0] poi non riuscirei a finirlo in tempo
        #####

        start = max(0, duration - (self.agent.time_steps - self.time_step) )
        end   = min(duration, self.time_step) + 1

        # Aggiungo anche lo 0 come valore possible,
        # in quanto l'elettrodomestico potrebbe anche
        # essere spento
        domain = [0]
        domain.extend(cycle[start:end])
        domain = list(set(domain))

        self.addAdmissableValues( domain )
