from base import BaseManager
from ..games.dodge_brick import DodgeBrick
from ..agents.neural import NeuralLearner
from ..agents.random_a import RandomAgent
from ..agents.qlearning import QAgent
import keras
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Flatten
from keras.layers.convolutional import Convolution2D
from keras.optimizers import SGD

class GameManager(BaseManager):

    def run(self, epochs, steps):
        for epoch in xrange(epochs):
            for step in xrange(steps):
                self.update()
                self.agent.update_epsilon(step+epoch*steps, epochs*steps)
                if step%200==0:
                    print "Epsilon: %f, score: %f, step: %f"%(self.agent.epsilon, self.game.score, step)
                    self.game.score = 0


if __name__ == "__main__":
    """ Some config """
    history_length = 4

    """ Choose game """
    game = DodgeBrick({'size': (4,4)})
    legal_actions = game.getPossibleActions()
    #import pdb; pdb.set_trace()

    """ Neural network for agent """
    net = Sequential()
    """ Switch to dynamic dimension here """
    # net.add(Convolution2D(8, 2, 2, subsample=(1,1), input_shape=(history_length, 4, 4)))
    # net.add(Activation('relu'))
    net.add(Convolution2D(8, 1, 1, subsample=(1,1), input_shape=(history_length, 4, 4)))
    net.add(Activation('relu'))
    net.add(Flatten())
    net.add(Dense(16))
    net.add(Activation('relu'))
    net.add(Dense(legal_actions.shape[0]))
    #rmsp = keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-6)
    adadelta = keras.optimizers.Adadelta(lr=1.0, rho=0.95, epsilon=1e-6)
    #sgd = SGD(lr=0.0001, decay=1e-6)
    net.compile(loss='mean_squared_error', optimizer=adadelta)

    """ Initialize all 3 agents, random, Qagent and neural """
    ra = RandomAgent(game.get_ranges())
    ta = QAgent(game.get_ranges())
    na = NeuralLearner(game.get_ranges(), net, (4, 4))

    """ Initialize manager and run experiment """
    manager = GameManager(game, na)
    manager.run(epochs=10, steps=1000)
