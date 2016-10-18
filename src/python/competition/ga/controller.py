import numpy

class Controller(object):
    @classmethod
    def select(cls, individuals, probabilities):
        return numpy.random.choice(individuals, size=2, replace=False, p=probabilities)

    @classmethod
    def cross(cls):
        pass
