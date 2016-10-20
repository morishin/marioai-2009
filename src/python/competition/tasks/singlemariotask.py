from client.marioenvironment import MarioEnvironment

from .episodictask import EpisodicTask
from .mariotask import MarioTask

if __name__ != "__main__":
    print("Loading %s ..." % __name__);


class SingleMarioTask(MarioTask):
    def getObservation(self):
        obs = EpisodicTask.getObservation(self)
        if len(obs) == MarioEnvironment.numberOfFitnessValues:
            self.reward = obs[1]
            self.status = obs[0]
            self.finished = True
            # Close socket when single task has been finished
            self.env.client.sock.close()
        return obs
