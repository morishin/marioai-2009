from enum import IntEnum

import numpy
from .marioagent import MarioAgent
from ga.individual import Individual

class MyAgent(MarioAgent):
    def __init__(self, individual):
        self.individual = individual

    def reset(self):
        self.action = numpy.zeros(5, int)

    def getAction(self):
        return self.individual.action(self.levelScene, self.isMarioOnGround, self.mayMarioJump)

    def integrateObservation(self, obs):
        if (len(obs) != 6):
            pass # Episode is over
        else:
            self.mayMarioJump, self.isMarioOnGround, self.marioFloats, self.enemiesFloats, self.levelScene, dummy = obs
