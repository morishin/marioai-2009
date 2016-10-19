import numpy

class Controller(object):
    @classmethod
    def select(cls, individuals, probabilities):
        return numpy.random.choice(individuals, size=2, replace=False, p=probabilities)

    @classmethod
    def two_points_cross(cls, individual1, individual2, indices=None):
        if indices is None:
            max_index = min(len(individual1.data), len(individual2.data))
            index1 = numpy.random.randint(0, max_index)
            index2 = numpy.random.randint(index1, max_index)
            indices = (index1, index2)

        child1 = numpy.hstack((individual1.data[:indices[0]],
            individual2.data[indices[0]:indices[1]],
            individual1.data[indices[1]:]))
        child2 = numpy.hstack((individual2.data[:indices[0]],
            individual1.data[indices[0]:indices[1]],
            individual2.data[indices[1]:]))

        return (child1, child2)
