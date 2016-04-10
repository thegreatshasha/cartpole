
from code import *
import numpy as np
import random

class QLearningAgent:
    def __init__(self, timestep, epsilon, gamma, force, action_bins, theta_tolerance):
        self.t = timestep
        self.epsilon = float(epsilon) #Greedy 
        self.gamma = float(gamma) #Discount factor
        self.actions = np.arange(-force, force, action_bins)
        self.delta_theta = theta_tolerance
        self.Qvalues = {}
        
    def update_Qvalue(self, pstate, action, state, reward):
        max_qvalue = max([AgentG.get_Qvalue(self, state, a) for a in self.actions)])
        value = reward + self.gamma * max_qvalue
        old_qvalue = Agent.Qvalues.get(str(pstate), str(action), None)
        
        if old_qvalue = None:
            self.Qvalues[(str(pstate), str(action))] = reward
        else:
            self.Qvalues[(str(pstate), str(action))] = reward + self.gamma * (max_qvalue - old_value)
    
    def choose_actions(self):
        if random.random() <= self.epsilon:
            return self.actions[np.random.choice(len(self.actions))]
        else:
            q = [Agent.get_Qvalue(self, state, a) for a in self.actions]
            maxQ = max(q)                
            count = q.count(maxQ)
        
        if count > 1:
            best = [i for i in range(len(self.actions)) if q[i] == maxQ]
            i = best[np.random.choice(len(best))]
        else:
            i = q.index(maxQ)

        action = self.actions[i]
        return action
        
    def get_actions(self):
      return self.actions
    
    def get_reward(self, state, action):
      violate = QLearningAgent.failure(state)
      if violate = True:
        return = - 10
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
      
      if temp = True:
        return True
      else:
        return False
  
      
