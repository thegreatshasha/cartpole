import numpy as np

#To create a new game you should specify the size of the board
class ticTacToe:
    
    def __init__(self, size):
    	#values 0 and 1 represent x and o respectively and 2 for blank
        #game specific
        self.size = size
    	self.board = np.zeros((size,size))
        self.board.fill(2)
        self.actions = range(size * size)

    #def setBoard(self):
    	#sets board to empty
    	#for i in range(len(self.board)):
    		#for j in range(len(self.board[0])):
    		#	self.board[i][j] = 2

    def play(self,action,player):
    	#action is a valid action , player 0->'x', 1->'o'
    	i = action / self.size
    	j = action % self.size
    	self.board[i][j] = player
        self.actions[action]=-1

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
    	#checks if a seq is complete
    	val = seq[0]
    	if val == 2:
    		return 0
    	for i in seq:
    		if i!= val:
    			return 0
    	return 1

    def getState(self):
    	#returns state of the board as list
    	return tuple(x for x in np.reshape(self.board,self.size*self.size))

    def gameOverCheck(self):
 		s = self.size
 		A = self.board
		for row in A:
			if(self.seqCheck(row)):
				return True,row[0]

		for col in A.transpose():
			if(self.seqCheck(col)):
				return True,col[0]

		d1=[A[i][i] for i in range(s)]
		d2=[A[s-1-i][s-1-i] for i in range(s)]
		if self.seqCheck(d1):
			return True,d1[0]
		if self.seqCheck(d2):
			return True,d2[0]

		for row in A:
			for col in row:
				if col==2:
					return False,4
		return True,3#tie
    
    def getActions(self):
        return self.actions



