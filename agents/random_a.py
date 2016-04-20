import numpy as np
from abstract import AbstractAgent

class RandomAgent(AbstractAgent):
    def __init__(self, rngs):
        self.actions = rngs[-1] # Last range is action range
        self.long_press_times = 1
        self.epsilon = 1

    def update_Qvalue(self, pstate, action, nstate, reward, terminal):
        pass

    def choose_action(self, state):
        return self.actions[np.random.choice(len(self.actions)-1)] # Choose any element but last
