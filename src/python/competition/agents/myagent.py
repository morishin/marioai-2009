from enum import IntEnum

import numpy
from .marioagent import MarioAgent


class LevelSceneCode(IntEnum):
    nothing = 0
    coin = 2
    block = -60
    princess = 5
    ground = 1


class LevelScene(object):
    @classmethod
    def is_obstacle(cls, code):
        return not (code == LevelSceneCode.nothing
                    or code == LevelSceneCode.coin
                    or code == LevelSceneCode.princess)


class Individual(object):
    length = 2**16
    gene_size = 2**5

    def __init__(self, random=False):
        self.data = numpy.random.randint(Individual.gene_size, size=self.length) if random else numpy.zeros(self.length, int)

    def gene_index_from_levelscene(self, levelscene):
        near_cells = [
            levelscene[10][10],
            levelscene[10][11],
            levelscene[10][12],
            levelscene[11][10],
            levelscene[11][12],
            levelscene[12][10],
            levelscene[12][12]
        ]
        return int(''.join(map(lambda cell: '1' if LevelScene.is_obstacle(cell) else '0', near_cells)), 2)

    def action(self, levelscene):
        fmt = '{0:0' + str(Individual.gene_size.bit_length()) + 'b}'
        digits = fmt.format(self.data[self.gene_index_from_levelscene(levelscene)])
        return list(map(lambda d: int(d), digits))


class MarioAction(IntEnum):
    left = 0
    right = 1
    down = 2
    jump = 3
    speed = 4


class MyAgent(MarioAgent):
    def __init__(self, individual):
        self.individual = individual

    def reset(self):
        self.action = numpy.zeros(5, int)

    def getAction(self):
        return self.individual.action(self.levelScene)

    def integrateObservation(self, obs):
        if (len(obs) != 6):
            pass # Episode is over
        else:
            self.mayMarioJump, self.isMarioOnGround, self.marioFloats, self.enemiesFloats, self.levelScene, dummy = obs
