from Agent import Agent
from Variable import Variable
from DomainCycle import DomainCycle
from ConstraintContinuity import ConstraintContinuity
from ConstraintEndsBeforeTime import ConstraintEndsBeforeTime

###
# Definisco i cicli possibili per la lavatrice
###
class WashingMachineCycle():
    IDLE      = {
                    'name'  : 'idle',
                    'power' : [0]
                }
    COTTON_60 = {
                    'name'  : 'Cotton 60',
                    'power' : [10, 15, 20, 8, 5]
                }

    COTTON_30 = {
                    'name' : 'Cotton 30',
                    'power': [1, 1, 3, 8, 10, 3, 2]
                }


########################
### Agente Lavatrice ###
########################

class WashingMachine(Agent):
    def __init__(self, name, time_steps):
        super(WashingMachine, self).__init__(name, time_steps)
        self.currentCycle = WashingMachineCycle.COTTON_60
        self.createVarsDomainsConstraints()

    def powerInfo(self):
        return self.currentCycle['power']

    def setCurrentCycle(self, cycle):
        self.currentCycle = cycle
        self.createVarsDomainsConstraints()

    def endsBefore(self, time):
        if ( time >= self.time_steps ):
            return False
        con = ConstraintEndsBeforeTime("wm_ends_before", self, self.variables, time)
        self.constraints.append(con)

    ###
    # Creazione delle variabili, dei domini
    # e dei constraint obbligatori
    ###

    def createVarsDomainsConstraints(self):
        self.createVariablesAndDomains()
        self.createContinuityConstraint()

    def createVariablesAndDomains(self):
        self.variables = []
        for t in range(0, self.time_steps):
            var = Variable("p_wm_{}".format( t ), self)
            dom = DomainCycle(var, self, t)

            var.setDomain(dom)

            self.variables.append( var )

    def createContinuityConstraint(self):
        con = ConstraintContinuity("continue_cycle_wm", self, self.variables)
        self.constraints.append( con )