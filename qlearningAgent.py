
from code import *
import numpy as np
import random

class QAgent:
    def __init__(self):
        self.epsilon = float(epsilon) #Greedy 
        self.gamma = float(gamma) #Discount factor
        self.action_bins = 10
        self.force = 100
        self.actions = np.arange(-self.force, self.force, action_bins)
        self.delta_theta = 10
        self.Qvalues = {}
        
    def update_Qvalue(self, pstate, action, state, reward):
        max_qvalue = max([QAgent.get_Qvalue(self, state, a) for a in self.actions])
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
    
    def get_reward(self, state, action):
      violate = self.failure(state)
      if violate == True:
        return -10
      else:
        return 1
      
    def failure(self, state):
      temp = False
      """
      state = [theta, omega, alpha]
      Just assuming for now that theta has to be within a tolerance band.
      Later can add constraints on each state variable.
      """
      angle, vel, alpha = state[0], state[1], state[2]
      temp = ((angle < -self.delta_theta) or (angle > self.delta_theta))
      
      if temp == True:
        return True
      else:
        return False
  
      
