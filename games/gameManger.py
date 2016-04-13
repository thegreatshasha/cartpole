import numpy as np
import math as m
import pdb
import random
import matplotlib.pyplot as plt
from TicTacToe import ticTacToe
from random_agent import randomAgent
from QLearningAgent import qLearningAgent
from CreateGame import createGame

games_played = 0
games_won_x = 0
games_won_o = 0
total_games = 10000000

#GAME PARAMS
size = 3

#Q-LEARNING PARAMS
alpha = 0.1
gamma = 0.8
greedy_to_random = 1
rewards = {0:100,1:-100,3:-10,4:1}

#AGENTS:qLearningAgent(self,size,rewards,alpha,gamma,greedy_to_random)
random_agentX = qLearningAgent(size,rewards,alpha,gamma,greedy_to_random)
random_agentO = randomAgent()

while games_played < total_games:
	
	game,turn,gs,agent_played = createGame(size)
	if games_played >= 10000 and games_played % 1000==0:

		print 'games_won_x:%d,games_won_o:%d'%(games_won_x,games_won_o)
		games_won_o,games_won_x = 0,0
		pdb.set_trace()
	
	while not gs:
		game.printBoard()
		if turn==0:
			agent_played=True
			s_t=game.getState()
		
			utility,action1=random_agentX.chooseAction(s_t,game.getActions())
			
			game.play(action1,turn)
			
			gs,r_key=game.gameOverCheck()

			
			if r_key==0 or r_key==3:
				random_agentX.updateQvalue(r_key,s_t,action1,game.getActions())
			
			if r_key==0:
				games_won_x+=1

			turn=1
			continue

		if turn==1:
			#interaction between agent and game
			action=random_agentO.chooseAction(game.getActions())
			game.play(action,turn)
			s_tplus1=game.getState()
			gs,r_key=game.gameOverCheck()
			
			if r_key==4 and agent_played:	
				random_agentX.updateQvalue(r_key,s_t,action1,game.getActions(),s_tplus1)
			
			if r_key==1:
				random_agentX.updateQvalue(r_key,s_t,action1,game.getActions())	
				games_won_o+=1
			
			turn=0

	games_played+=1

print 'games won by x:%d, games won by o:%d'%(games_won_x,games_won_o)