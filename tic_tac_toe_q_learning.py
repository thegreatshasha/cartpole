import numpy as np
import math as m
import pdb
import random
import matplotlib.pyplot as plt

class TicTacToe:
    
    def __init__(self,size):
    	#values 0 and 1 represent x and o respectively and -1 for blank
    	self.size=size
    	self.board=np.zeros((self.size,self.size))
    	
 
    def setBoard(self):
    	for i in range(len(self.board)):
    		for j in range(len(self.board[0])):
    			self.board[i][j]=2

    def play(self,action,player):
    	#player 0-x and 1-o, action is the position
    	i=action/self.size
    	j=action%self.size
    	self.board[i][j]=player

    def printBoard(self):
    	#prints the current board
    	for row in self.board:
    		p_row=[]
    		for e in row:
    			if(e==0):
    				p_row.append('x')
    			elif(e==1):
    				p_row.append('o')
    			else:
    				p_row.append('_')
    		print' '.join(map(str,p_row))		
    
    def seqCheck(self,seq):
    	val=seq[0]
    	if val==2:
    		return 0
    	for i in seq:
    		if i!=val:
    			return 0
    	return 1

    def getState(self):
    	return tuple(x for x in np.reshape(self.board,self.size*self.size))
 
    def gameOverCheck(self):
    	#returns False,4 if not over and True,winner if over and won or True,3 if tie
    	outcome=0
    	s=self.size
    	A=self.board
    	c=0
    	for row in A:
    		if(self.seqCheck(row)):
    			#print "row made"
    			return True,row[0]
    
    	for col in A.transpose():
    		if(self.seqCheck(col)):
    			#print "col made"
    			return True,col[0]
    	
    	d1=[A[i][i] for i in range(s)]
    	d2=[A[s-1-i][s-1-i] for i in range(s)]
    	if self.seqCheck(d1):
    		#print "diagonal made"
    		return True,d1[0]
    	if self.seqCheck(d2):
    		return True,d2[0]
    	
    	for row in A:
    		for col in row:
    			if col==2:
    				return False,4
    	return True,3
    	

def chooseMaxQ(state,actions):

	choice=values[state]#q val for all actions
	choice=[[choice[j],j] for j in range(len(choice))]
	choice.sort()
	j=len(choice)-1
		
	while actions[choice[j][1]]==-1:
		j-=1
		
	action=choice[j][1]
	Q_max=choice[j][0]
	
	return Q_max,action

#constants and Q-Learning params
size=3
dim=[size]*(size*size)
dim.append(size*size)
#dim=tuple(dim)
#Q-utility table
values=np.zeros(shape=dim)

#q-knobs
rewards={0:50.0,1:-1000.0,3:5.0,4:1.0}
alpha=0.1
gamma=0.8
greedy=1

#progress tracking
games_played=0
games_won=0
games_won2=0
a1=[]
b1=[]
total_games=100000

step=100
d_greedy=1/(total_games/step)

while games_played<total_games:

	#reset these every game
	a=TicTacToe(3)
	a.setBoard()#create game
	gs=False#gameover check flag
	turn=np.random.randint(0,1)#random choice to decide who starts
	actions=range(9)

	#progress montioring
	print "iteration:%d"%games_played
	
	
	if games_played>=step and games_played%step==0:
		
		greedy=greedy-d_greedy
		print 'games won by Q-learning agent:%d/10000,games won by RA:%d/10000'%(games_won,games_won2)
		a1.append([games_played,games_won])
		b1.append([games_played,games_won2])
		
		
		games_won=0
		games_won2=0
	
	while not gs:
		
		
		if turn==0:
			r=np.random.uniform()
			if a>greedy:	
			#code for random agent
				print 'x turn:Q-learning agent'
			
				s_t=a.getState()
				Q_t_max,a_t = chooseMaxQ(s_t,actions)
			
				print 'action is:%d'%a_t
				a.play(a_t,turn)
				actions[a_t]=-1
			
				s_t = list(s_t)
				s_t.insert(size*size,a_t)#state,action pair for which the Q-value is updated
				s_a_t= tuple(s_t)

				gs,r_key=a.gameOverCheck()
			
				s_tplus1=a.getState()

				if gs:
					for j in range(len(actions)):
						values[s_tplus1][j]=0
					if r_key==0:
						games_won=games_won+1
					Q_tplus1_max=0
				else:
					Q_tplus1_max,a_max=chooseMaxQ(s_tplus1,actions)
			
				values[s_a_t]+= alpha * ( rewards[r_key] + gamma * Q_tplus1_max - values[s_a_t] )
			#q-learning generates action
			else:
				
				print 'o turn:random agent'
				action=random.choice(actions)
			
				while action==-1:
					action=random.choice(actions)#random agent generates action
			
				print 'action is:%d'%action
				a.play(action,turn)
				actions[action]=-1#remove the action from the action set	
			
				gs,r_key=a.gameOverCheck()#check if the game is over
				if r_key==0:
					games_won+=1

			turn=1
			
			#RANDOM AGENT VS RANDOM AGENT _____________________________________________________
			#action=random.choice(actions)
			
			#while action==-1:
			#	action=random.choice(actions)#random agent generates action
			
			#print 'action is:%d'%action
			#a.play(action,turn)
			#actions[action]=-1
			
			#turn=1#change turn
			
			#gs,r_key=a.gameOverCheck()
			#print 'reward:%d'%r_key
			
			continue

		if turn==1:
			
			print 'o turn:random agent'
			action=random.choice(actions)
			
			while action==-1:
				action=random.choice(actions)#random agent generates action
			
			print 'action is:%d'%action
			a.play(action,turn)
			actions[action]=-1#remove the action from the action set	
			
			gs,r_key=a.gameOverCheck()#check if the game is over
			if r_key==1:
				games_won2+=1
			turn=0

	games_played+=1
plt.plot(*zip(*a1), marker='o', color='r', ls='')
plt.plot(*zip(*b1), marker='o', color='b', ls='')	
plt.show()