import numpy as np
import random
import math.pi as m
from table import Table

class QAgent:
    def __init__(self, rngs):
        # Initialize the state action table
        self.Qvals = Table(ranges=rngs)
        self.actions = rngs[-1] # Last range is action range

        # Q learning parameters
        self.epsilon = 0.5 # Randomness
        self.gamma = 0.5 # Future discount factor

    def update_Qvalue(self, pstate, action, nstate, reward):
        max_qvalue = max(self.Qvals[nstate])
        value = reward + self.gamma * max_qvalue
        pstate_action = pstate + [action]
        p_Qval = self.Qvals[pstate_action]

        self.Qvals[pstate_action] = reward + self.gamma * (max_Qval - p_Qval)

    def choose_action(self, state):
        if random.random() <= self.epsilon:
            return self.actions[np.random.choice(len(self.actions)-1)] # Choose any element but last
        else:
            q = max(self.Qvals)
            count = q.count(maxQ)

        if count > 1:
            best = [i for i in range(len(self.actions)) if q[i] == maxQ]
            i = best[np.random.choice(len(best))]
        else:
            i = q.index(maxQ)
        action = self.actions[i]
        return action

    def get_reward(self, prev_state, next_state, action):
        return 0
