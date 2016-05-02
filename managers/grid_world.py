from base import BaseManager
from ..games.grid_world import GridWorld
from ..agents.neural import NeuralLearner
from ..agents.random_a import RandomAgent
from ..agents.qlearning import QAgent
import keras
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Flatten
from keras.layers.convolutional import Convolution2D
from keras.optimizers import SGD
import numpy as np

class GameManager(BaseManager):

    def run(self, epochs, steps):
        import pdb; pdb.set_trace()
        for epoch in xrange(epochs):
            for step in xrange(steps):
                self.update()
                #self.agent.update_epsilon(step+epoch*steps, epochs*steps)
                #if step%200==0:
                    #print "Epsilon: %f, score: %f, step: %f"%(self.agent.epsilon, self.game.score, step)
                    #self.game.score = 0


if __name__ == "__main__":
    """ Some config """
    history_length = 4

    """ Choose game """
    board=np.array([[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 3],
        [0, 0, 0, 0, 1, 0]])

    game = GridWorld({'board': board})
    legal_actions = game.getPossibleActions()
    #import pdb; pdb.set_trace()

   
    """ Initialize all 3 agents, random, Qagent and neural """
    ra = RandomAgent(game.get_ranges())
    #ta = QAgent(game.get_ranges())
    #na = NeuralLearner(game.get_ranges(), net, (4, 4))

    """ Initialize manager and run experiment """
    manager = GameManager(game, ra)
    manager.run(epochs=10, steps=1000)
