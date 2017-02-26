from Agent import Agent
from Variable import Variable
from DomainCycle import DomainCycle
from ConstraintContinuity import ConstraintContinuity
from ConstraintEndsBeforeTime import ConstraintEndsBeforeTime

import math

#####################
### Agente Boiler ###
#####################

class Boiler(Agent):
    def __init__(self, name, time_steps, qty):
        super(Boiler, self).__init__(name, time_steps)
        self.min_qty = 0
        self.max_qty = 100
        self.setQty(qty)

        # Consuma 10 quando e' acceso
        self.power_when_on = 10

        self.createVarsDomainsConstraints()

    # Imposta la quantia' di acqua calda
    # presente nel boiler
    def setQty(self, val):
        qty = max(val, self.min_qty)
        qty = min(qty, self.max_qty)
        self.qty = qty

    # A partire da una certa quantita' di acqua
    # resituisce il tempo (misurato in numero di time step)
    # necessario per raggiungere una quantita' target
    def getTimeToReachQty(self, target_qty):
        if target_qty <= self.qty:
            return 0
        else:
            return math.floor( (target_qty - self.qty) / 5 )

    # Ciclo per raggiungere la massima capienza a partire
    # dalla quantita' di acqua calda attuale
    def powerInfo(self):
        duration = self.getTimeToReachQty(self.max_qty)
        return [self.power_when_on] * duration

    def endsBefore(self, time):
        if ( time >= self.time_steps ):
            return False
        con = ConstraintEndsBeforeTime("boiler_ends_before", self, self.variables, time)
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
            var = Variable("p_boiler_{}".format( t ), self)
            dom = DomainCycle(var, self, t)

            var.setDomain(dom)

            self.variables.append( var )

    def createContinuityConstraint(self):
        con = ConstraintContinuity("continue_cycle_boiler", self, self.variables)
        self.constraints.append( con )