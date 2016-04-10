import numpy as np
from code import 

class Agent:
    def __init__(self, timestep, epsilon, gamma, training_steps):
        self.t = timestep
        self.epsilon = float(epsilon) #Greedy 
        self.gamma = float(gamma) #Discount factor
        self.train_iter = training_steps
        
    def get_Qvalue(self, state, action):
        """
        Should return Q(state, action)
        """
     
    def getValue(self, pstate, action, state, reward):
        """ What is the value of this state under the best action?
            V(s) = max_{a in actions} Q(s,a)
        """
    def getPolicy(self, state):
        """
        What is the best action to take in the state.
        policy(s) = arg_max_{a in actions} Q(s,a)
        If multiple actions with same max Q-value, choose random.
        """
        
    def choose_action(self):
        """
        Given a criteria, choose an actio from available action list and return it.
        Exploration - Exploitation code here.
        """
        
        
    
    
