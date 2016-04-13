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
        self.epsilon = 0.3 # Randomness
        self.gamma = 0.8 # Future discount factor
        self.eta = 0.3

    def update_Qvalue(self, pstate, action, nstate, reward):
        max_Qval = max(self.Qvals[nstate])
        value = reward + self.gamma * max_Qval
        pstate_action = pstate + [action]
        p_Qval = self.Qvals[pstate_action]

        self.Qvals[pstate_action] = p_Qval + self.eta * (reward + self.gamma * max_Qval - p_Qval)

    def choose_action(self, state):
        if np.random.random() <= self.epsilon:
            return self.actions[np.random.choice(len(self.actions)-1)] # Choose any element but last
        else:
            return self.Qvals.max_action(state)
