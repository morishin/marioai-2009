import unittest

from agents.myagent import *
from ga.individual import *


class TestMyAgent(unittest.TestCase):
    sample_levelscene = [
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,20,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,20,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,20,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,-10,-10,-10,-10,-10,-10,-10,-10,-10,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,-10,-10,-10,-10,-10,-10,-10,-10,-10,0],
      [-10,-10,-10,-10,-10,-10,0,0,0,0,0,0,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10],
      [-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    isMarioOnGround = True
    mayMarioJump = True

    def test_levelscene_is_obstacle(self):
        self.assertFalse(LevelScene.is_obstacle(LevelSceneCode.nothing))
        self.assertFalse(LevelScene.is_obstacle(LevelSceneCode.coin))
        self.assertTrue(LevelScene.is_obstacle(LevelSceneCode.block))
        self.assertFalse(LevelScene.is_obstacle(LevelSceneCode.princess))
        self.assertTrue(LevelScene.is_obstacle(LevelSceneCode.ground))

    def test_individual_gene_index_from_levelscene(self):
        individual = Individual()
        gene_index = individual.gene_index_from_levelscene(self.sample_levelscene, self.isMarioOnGround, self.mayMarioJump)
        self.assertTrue(gene_index < Individual.length)

    def test_individual_action(self):
        individual = Individual()
        action = individual.action(self.sample_levelscene, self.isMarioOnGround, self.mayMarioJump)
        self.assertTrue(action == [0] * Individual.gene_size.bit_length())


if __name__ == '__main__':
    unittest.main()
