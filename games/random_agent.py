import numpy as np
import math as m
import pdb
import random
import matplotlib.pyplot as plt
from TicTacToe import ticTacToe 

class randomAgent():
	
	def __init__(self):
		pass

	def chooseAction(self,actions):	
		#returns the index of the selected action
		action=random.choice(actions)
		while action==-1:
			action=random.choice(actions)#random agent generates action

		return action