import numpy as np
import math as m
import pdb
import random

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
    	

"""
size=3
dim=[size]*(size*size)
dim.append(size*size)
values=np.zeros(shape=dim)
rewards={0:50.0,1:-50.0,3:5.0,4:1.0}
alpha=0.1
gamma=0.8
"""
i=0


while i<1:

	a=TicTacToe(3)
	a.setBoard()#create game
	gs=False#gameover check flag
	turn=np.random.randint(0,1)#random choice to decide who starts
	actions=range(9)

	
	while not gs:
		
		
		pdb.set_trace()
		a.printBoard()
		print "actions"
		print actions
		if turn==0:
			
			print 'x turn'
			"""state=getState()
			choice=values.item(state)#q val for all actions
			choice=[[choice[j],j] for j in range(len(choice))]
			choice.sort()
			j=len(choice-1)
			while actions[choice[j][1]]==-1:
				j-=1
			action=choice[j][1]
			state_a=state.insert(size*size,action)
			actions[action]=-1
			gs,r_key=gameOverCheck()
			values[state_a]=values[state_a]+alpha*(rewards[r_key]+)
			#q-learning generates action
			play(action,turn)
			turn=1
			"""
			action=random.choice(actions)
			
			while actions[action]==-1:
				action=random.choice(actions)#random agent generates action
			
			print 'action is:%d'%action
			a.play(action,turn)
			actions[action]=-1
			
			turn=1#change turn
			
			gs,r_key=a.gameOverCheck()
			print 'reward:%d'%r_key
			
			continue

		if turn==1:
			print 'o turn'
			action=random.choice(actions)
			
			while actions[action]==-1:
				action=random.choice(actions)#random agent generates action
			
			print 'action is:%d'%action
			a.play(action,turn)
			actions[action]=-1#remove the action from the action set	
			
			turn=0
			
			gs,r_key=a.gameOverCheck()#check if the game is over
			print 'reward:%d'%r_key
	i+=1
a.printBoard()
print "game over"