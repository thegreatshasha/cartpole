import numpy as np
import math as m

class TicTacToe:
    
    def __init__(self,size):
    	#values 0 and 1 represent x and o respectively and -1 for blank
    	self.size=size
    	self.board=np.zeros((self.size,self.size))
    	for row in self.board:
    		for col in row:
    			self.board[row][col]=2
 
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
    	
size=3
dim=[size]*(size*size)
dim.append(size*size)
values=np.zeros(shape=dim)
rewards={0:50.0,1:-50.0,3:5.0,4:1.0}
alpha=0.1
gamma=0.8
i=0

while i<10000
	a=TicTacToe(3)#create game
	gs=False#gameover check flag
	turn=random.randint(0,1)#random choice to decide who starts
	actions=range(9)

	
	while !gs:
		state=getState()
		if turn==0:
			choice=values.item(state)
			state.insert(,a.)
			#q-learning generates action
			play(action,turn)
			turn=1

		if turn==1:
			action=actions[np.random.randint(len(actions))]
			#random agent generates action
			play(action,turn)
			turn=1

		actions.remove(action)#remove the action from the action set	
		gs,r_key=gameOverCheck()#check if the game is over
		
