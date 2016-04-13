import numpy as np
import random
import math as m
from ..datastructures.table import Table
from abstract import AbstractAgent

class QAgent(AbstractAgent):
    def __init__(self, rngs):
        # Initialize the state action table
        self.Qvals = Table(ranges=rngs)
        self.actions = rngs[-1] # Last range is action range

        # Q learning parameters
        self.epsilon = 1.0 # Randomness
        self.gamma = 0.9 # Future discount factor
        self.eta = 0.8

    def update_epsilon(self, step, total):
        self.epsilon = max((total - float(step))/total, 0.1)

    def update_Qvalue(self, pstate, action, nstate, reward, terminal):
        max_Qval = max(self.Qvals[nstate])
        value = reward + self.gamma * max_Qval
        pstate_action = np.concatenate([pstate, [action]])
        p_Qval = self.Qvals[pstate_action]
        if terminal:
            self.Qvals[pstate_action] = self.eta * reward
        else:
            self.Qvals[pstate_action] = p_Qval + self.eta * (reward + self.gamma * max_Qval - p_Qval)

    def choose_action(self, state):
        if np.random.random() <= self.epsilon:
            return self.actions[np.random.choice(len(self.actions)-1)] # Choose any element but last
        else:
            return self.Qvals.max_action(state)
