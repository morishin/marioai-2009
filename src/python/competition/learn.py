__author__ = "Sergey Karakovskiy, sergey at idsia dot ch"
__date__ = "$Apr 30, 2009 1:46:32 AM$"

import sys

from experiments.episodicexperiment import EpisodicExperiment
from tasks.mariotask import MarioTask
from agents.myagent import *


#from pybrain.... episodic import EpisodicExperiment
#TODO: reset sends: vis, diff=, lt=, ll=, rs=, mariomode, time limit, pw,
# with creatures, without creatures HIGH.
# send creatures.

class IndividualReward:
    def __init__(self, individual, reward):
        self.individual = individual
        self.reward = reward

    def __str__(self):
        return str(self.reward)

def main():
    n_individuals = 10
    initial_group = [Individual(random=True) for i in range(n_individuals)]
    rewards = []
    for individual in initial_group:
        agent = MyAgent(individual)
        task = MarioTask(agent.name)
        task.env.initMarioMode = 2
        task.env.levelDifficulty = 0
        exp = EpisodicExperiment(task, agent)
        exp.doEpisodes(1)
        rewards.append(IndividualReward(individual, task.reward))
        # for disconnecting client socket
        del(task)
        del(agent)
        del(exp)
    for r in rewards:
        print(r)

#    clo = CmdLineOptions(sys.argv)
#    task = MarioTask(MarioEnvironment(clo.getHost(), clo.getPort(), clo.getAgent().name))
#    exp = EpisodicExperiment(clo.getAgent(), task)
#    exp.doEpisodes(3)

if __name__ == "__main__":
    main()
else:
    print("This is module to be run rather than imported.")
