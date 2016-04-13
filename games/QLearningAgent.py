import numpy as np
import math as m
import pdb
import random
import matplotlib.pyplot as plt
from TicTacToe import ticTacToe 

class qLearningAgent:
	
	def __init__(self,size,rewards,alpha,gamma,greedy_to_random):
		
		self.rewards=rewards
		self.dim=[3]*size*size
		self.dim.append(size*size)
		self.Qvalues=20.0*np.random.random_sample(size=tuple(self.dim))
		self.alpha=alpha
		self.gamma=gamma
		self.greedy_to_random=greedy_to_random

	def chooseAction(self,state,actions):
		
		choice=self.Qvalues[state]
		choice=[[choice[j],j] for j in range(len(choice))]
		choice.sort()
		j=len(choice)-1
		
		while actions[choice[j][1]]==-1:
			j-=1
		
		action=choice[j][1]
		Q_max=choice[j][0]
		
		return Q_max,action

	def updateQvalue(self,r_key,s_t,action,actions,s_tplus1=None):
		
		if r_key==0 or r_key==3 or r_key==1:
			Q_tplus1_max=0
			self.Qvalues[s_t][action]+= self.alpha * ( self.rewards[r_key] + self.gamma * Q_tplus1_max - self.Qvalues[s_t][action] )
		
		if r_key==4:
			Q_tplus1_max,_= self.chooseAction(s_tplus1,actions)
			self.Qvalues[s_t][action]+= self.alpha * ( self.rewards[r_key] + self.gamma * Q_tplus1_max - self.Qvalues[s_t][action] )