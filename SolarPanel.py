from Agent import Agent
from Variable import Variable
from DomainUpperBound import DomainUpperBound

##########################
### Agente Solar Panel ###
##########################

class SolarPanel(Agent):
    def __init__(self, name, time_steps):
        super(SolarPanel, self).__init__(name, time_steps)
        self.isProducingPower = True

        self.createVarsDomainsConstraints()
        # In questo caso non ci sono contraint obbligatori

    def powerInfo(self):
        return [0, 0, 0, 4, 5, 10, 19, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0]

    ###
    # Creazione delle variabili, dei domini
    # e dei constraint obbligatori
    ###

    def createVarsDomainsConstraints(self):
        self.createVariablesAndDomains()

    def createVariablesAndDomains(self):
        self.variables = []
        for t in range(0, self.time_steps):
            var = Variable("p_sp_{}".format( t ), self)
            dom = DomainUpperBound(var, self, t)

            var.setDomain(dom)

            self.variables.append( var )