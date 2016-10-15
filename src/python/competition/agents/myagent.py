from enum import IntEnum

import numpy
from .marioagent import MarioAgent


class MarioAction(IntEnum):
    left = 0
    right = 1
    down = 2
    jump = 3
    speed = 4
    up = 5

class MyAgent(MarioAgent):
    def __init__(self):
        pass

    def reset(self):
        self.action = numpy.zeros(6, int)

    def getAction(self):
        self.action[MarioAction.right] = 1
        return self.action

    def integrateObservation(self, obs):
        if (len(obs) != 6):
            pass # Episode is over
        else:
            self.mayMarioJump, self.isMarioOnGround, self.marioFloats, self.enemiesFloats, self.levelScene, dummy = obs
