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

    def run(self):
        terminal=False
        while terminal!=True:
            action,terminal=self.update()
    
    def update(self):
        """ Run a single update step """
        prev_state = self.game.get_state()
        action = self.agent.choose_action(prev_state) # Decide best action according to the agent
        reward, terminal = self.game.act(action) # Execute that action
        next_state = self.game.get_state() # Get next state
        self.agent.update_Qvalue(prev_state, action, next_state, reward, terminal)
        return action,terminal   

            


if __name__ == "__main__":
    games_to_be_played=10000
    games_played=0
    
    while games_played<games_to_be_played:
        #game setup-goal and agent position random
        board=np.array([[0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 3],
            [0, 0, 0, 0, 1, 0]])
        goal=np.array([np.random.randint(0,board.shape[0]),np.random.randint(0,board.shape[1])])
        position=np.array([np.random.randint(0,board.shape[0]),np.random.randint(0,board.shape[1])])
        while goal[0]==position[0] and goal[1]==position[1]:
            position=np.array([np.random.randint(0,board.shape[0]),np.random.randint(0,board.shape[1])])
        board[position[0]][position[1]]=2
        board[goal[0]][goal[1]]=3
        
        game = GridWorld({'board': board, 'position':position, 'goal':goal})
        legal_actions = game.getPossibleActions()
        
        """ Initialize all 3 agents, random, Qagent and neural """
        ra = RandomAgent(game.get_ranges())
            #ta = QAgent(game.get_ranges())
            #na = NeuralLearner(game.get_ranges(), net, (4, 4))

        """ Initialize manager and run experiment """
        manager = GameManager(game, ra)
        manager.run()
