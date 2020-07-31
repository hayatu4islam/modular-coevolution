from Evolution.AgentTypeRegistry import AgentTypeRegistry

import abc


# The superclass of both attacker and defender agents generated by the attacker and defender generators.
# All agents must implement either BaseAttacker or BaseDefender, as well as the abstract methods here.
class BaseAgent(metaclass=AgentTypeRegistry):
    agent_type_name = "no type name"

    # Return a string which displays relevant parameters to the agent for logging purposes, such that the agent can be reconstructed later. For example, a genome.
    @abc.abstractmethod
    def parameterString(self):
        pass

    @abc.abstractmethod
    def getParameters(self):
        pass

    @abc.abstractmethod
    def applyParameters(self, parameters):
        pass

    @abc.abstractmethod
    def performAction(self):
        pass

    def __init__(self, parameters=None, active=True, *args, **kwargs):
        self.active = active
        if parameters is not None:
            self.applyParameters(parameters)
