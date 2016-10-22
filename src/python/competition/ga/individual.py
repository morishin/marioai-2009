from enum import IntEnum

import numpy


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
    length = 2**9
    gene_size = 2**5

    def __init__(self, data=None, random=False):
        self.data = data if data is not None else numpy.random.randint(Individual.gene_size, size=self.length) if random else numpy.zeros(self.length, int)

    def to_list(self):
        return list(self.data)

    @classmethod
    def from_list(cls, lst):
        return Individual(data=numpy.array(lst))

    def gene_index_from_levelscene(self, levelscene, isMarioOnGround, mayMarioJump):
        near_cells = [
            levelscene[10][10],
            levelscene[10][11],
            levelscene[10][12],
            levelscene[11][10],
            levelscene[11][12],
            levelscene[12][10],
            levelscene[12][12]
        ]
        cells_info = list(map(lambda cell: '1' if LevelScene.is_obstacle(cell) else '0', near_cells))
        mario_info = [str(int(isMarioOnGround)), str(int(mayMarioJump))]
        return int(''.join(cells_info + mario_info), 2)

    def action(self, levelscene, isMarioOnGround, mayMarioJump):
        fmt = '{0:0' + str(Individual.gene_size.bit_length()) + 'b}'
        digits = fmt.format(self.data[self.gene_index_from_levelscene(levelscene, isMarioOnGround, mayMarioJump)])
        return list(map(lambda d: int(d), digits))
