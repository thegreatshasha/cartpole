import numpy as np
import random
import math.pi as m

class QAgent:
    def __init__(self, state_range, action_range):
        self.epsilon = 0.5 #Greedy
        self.gamma = 0.5 #Discount factor
        self.state_ranges = state_ranges
        self.actions = action_range
        qval_dim = [dim.shape[0] for dim in self.state_ranges] + [self.actions.shape[0]]
        self.Qvalues = np.random.randn()

    def get_state(self, state):
        # Returns 1d array for q value correponding to
        state_inds = [np.digitize(dim)-1 for dim in state]
        return self.Qvalues[state_inds]

    def set_state(self, state, action_index, value):
        

    def get_action(self):


    def update_Qvalue(self, pstate, action, state, reward):
        max_qvalue = max([self.get_Qvalue(self, state, a) for a in self.actions])
        value = reward + self.gamma * max_qvalue
        old_qvalue = self.Qvalues.get(str(pstate), str(action), None)

        if old_qvalue == None:
            self.Qvalues[(str(pstate), str(action))] = reward
        else:
            self.Qvalues[(str(pstate), str(action))] = reward + self.gamma * (max_qvalue - old_value)

    def choose_actions(self, state):
        if random.random() <= self.epsilon:
            return self.actions[np.random.choice(len(self.actions))]
        else:
            q = [self.get_Qvalue(self, state, a) for a in self.actions]
            maxQ = max(q)
            count = q.count(maxQ)

        if count > 1:
            best = [i for i in range(len(self.actions)) if q[i] == maxQ]
            i = best[np.random.choice(len(best))]
        else:
            i = q.index(maxQ)
        action = self.actions[i]
        return action

    def get_Qvalue(self,state, action):
        return self.Qvalues.get((str(state), str(action)), 0.0)

    def get_actions(self):
        return self.actions

    def get_reward(self, prev_state, next_state, action):
        return
