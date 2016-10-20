import unittest

from ga import *


class TestController(unittest.TestCase):
    def test_select(self):
        individuals = [Individual(random=True) for i in range(10)]
        selection = Controller.select(individuals, [0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertTrue(set(individuals[:2]) == set(selection))

    def test_two_points_cross(self):
        individual1 = Individual()
        individual1.data = numpy.array([0, 0, 0, 0])
        individual2 = Individual()
        individual2.data = numpy.array([1, 1, 1, 1])
        child1, child2 = Controller.two_points_cross(individual1, individual2, indices=(1, 3))
        self.assertTrue(numpy.array_equal(child1.data, [0, 1, 1, 0]))
        self.assertTrue(numpy.array_equal(child2.data, [1, 0, 0, 1]))


if __name__ == '__main__':
    unittest.main()
