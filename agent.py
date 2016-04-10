import numpy as np
from code import 
import random
from code import * #Assuming states are defined in code - this should correspond to the environment or we have another file

class Agent:
    def __init__(self, force, timestep, epsilon, gamma):
        self.t = timestep
        self.epsilon = float(epsilon) #Greedy 
        self.gamma = float(gamma) #Discount factor
        self.Qvalues = {}
        self.actions = np.arange(-force,force, 10) #Amount of horizontal force
    
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
            
    def get_Qvalue(self, state, action):
        return self.Qvalues.get(str(state), str(action), 0.0)
    
    def get_reward(self, state, action):
        
    
    
