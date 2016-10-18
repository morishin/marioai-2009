import unittest

from ga import *


class TestController(unittest.TestCase):
    def test_select(self):
        individuals = [Individual(random=True) for i in range(10)]
        selection = Controller.select(individuals, [0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertTrue(set(individuals[:2]) == set(selection))


if __name__ == '__main__':
    unittest.main()
