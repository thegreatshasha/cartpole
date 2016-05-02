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

    def run(self,games_to_be_played):
        games_played=0
        while games_played<games_to_be_played:
            _,terminal=self.update()
            if terminal==True:
                games_played+=1

    def update(self):
        """ Run a single update step """
        prev_state = self.game.get_state()
        action = self.agent.choose_action(prev_state) # Decide best action according to the agent
        reward, terminal = self.game.act(action) # Execute that action
        if(terminal==True):
            self.game.reset()
        next_state = self.game.get_state() # Get next state
        self.agent.update_Qvalue(prev_state, action, next_state, reward, terminal)
        return action,terminal   

            


if __name__ == "__main__":
    
    """Create game to pass to game Manager"""
    board = np.array([[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 3],
        [0, 0, 0, 0, 1, 0]])

    goal = np.array([np.random.randint(0,board.shape[0]),np.random.randint(0,board.shape[1])])
    position = np.array([np.random.randint(0,board.shape[0]),np.random.randint(0,board.shape[1])])
    while goal[0] == position[0] and goal[1] == position[1]:
        position = np.array([np.random.randint(0,board.shape[0]),np.random.randint(0,board.shape[1])])
    board[position[0]][position[1]] = 2
    board[goal[0]][goal[1]] = 3
    
    game = GridWorld({'board': board, 'position':position, 'goal':goal})
    legal_actions = game.getPossibleActions()
    st = game.get_state()
    
    """ Initialize all 3 agents, random, Qagent and neural """
    #ra = RandomAgent(game.get_ranges())
    #ta = QAgent(game.get_ranges())
    history_length = 1

    """ Neural network for agent """
    net = Sequential()
    
    """ Switch to dynamic dimension here """
    # net.add(Convolution2D(8, 2, 2, subsample=(1,1), input_shape=(history_length, 4, 4)))
    # net.add(Activation('relu'))
    # just modify network here
    net.add(Flatten(input_shape=(history_length, 8)))
    net.add(Dense(32))
    net.add(Activation('relu'))
    net.add(Dense(64))
    net.add(Activation('relu'))
    net.add(Dense(legal_actions.shape[0]))
    #rmsp = keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-6)
    adadelta = keras.optimizers.Adadelta(lr=1.0, rho=0.95, epsilon=1e-6)
    #sgd = SGD(lr=0.0001, decay=1e-6)
    net.compile(loss='mean_squared_error', optimizer=adadelta)

    """ Initialize all 3 agents, random, Qagent and neural """
    #ra = RandomAgent(game.get_ranges())
    #ta = QAgent(game.get_ranges())
    na = NeuralLearner(game.get_ranges(), net, st.shape)

    """ Initialize manager and run experiment """
    manager = GameManager(game, na)
    manager.run(500)