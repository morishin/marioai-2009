__author__="Sergey Karakovskiy, sergey at idsia fullstop ch"
__date__ ="$May 13, 2009 1:05:14 AM$"

class Experiment(object):
    """ An experiment matches up a task with an agent and handles their interactions.
    """

    def __init__(self, task, agent):
        self.task = task
        self.agent = agent
        self.stepid = 0

    def doInteractions(self, number = 1):
        """ The default implementation directly maps the methods of the agent and the task.
            Returns the number of interactions done.
        """
        for dummy in range(number):
            reward = self._oneInteraction()
        return reward

    def _oneInteraction(self):
        self.stepid += 1
        self.agent.integrateObservation(self.task.getObservation())
#        print "experiment.py self.agent.getAction(): ", self.agent.getAction(), "\n"
        self.task.performAction(self.agent.getAction())
        reward = self.task.getReward()
        self.agent.giveReward(reward)
        return reward
