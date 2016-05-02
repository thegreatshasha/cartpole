from abstract import AbstractGame
#import os
#os.environ['SDL_VIDEODRIVER'] = 'dummy'
import pygame
#import pygame
import numpy as np
from vec2d import Vec2d as Vector2
import random
import time
from ..agents.random_a import RandomAgent
from ..agents.qlearning import QAgent

class GridWorld(AbstractGame):

    def __init__(self, config):
        #pygame.init()
        self.board= config['board']
        self.position=config['position']
        self.goal=config['goal']
        pygame.init()
        self.size_vec = Vector2(1024, 768)
        self.screen = pygame.display.set_mode(self.size_vec)
        # Game statistics
        self.score = 0

    def get_state(self):
        # Flatten board and return #
        #return self.board.flatten()
        return self.board

    def get_ranges(self):
        # Return state ranges for board and actions #
        return [np.arange(0, 2+1+1, 1) for el in self.board.flatten()] + [np.arange(0,3+1+1,1)]

    def getPossibleActions(self):
        return np.array([0,1,2,3])

    def draw(self):
        
        pass

    def act(self, action):
        # agent actions:right,left,up,down
        actions={0:np.array([0,1]), 1:np.array([0,-1]), 2:np.array([1,0]), 3:np.array([-1,0]) }
        
        #rewards 
        gameover_reward=-10#teminal state 
        survival_reward=-1#continue search
        goal_reward=0#reached goal
        
        #erase previous position on board
        self.board[self.position[0]][self.position[1]]=0
        
        #calc new position
        self.position+=action      
         
        #if falls of board end game
        if self.position[0] < 0 or self.position[0] >= self.board.shape[0] or self.position[1] < 0 or \
            self.position[1] >= self.board.shape[1]:
            self.score += gameover_reward
            return gameover_reward,True
        
        #reach the goal end game
        elif self.board[self.position[0]][self.position[1]] == 3:
            self.score += goal_reward
            return goal_reward,True
        
        else:
            #walk into obstacle->nothing happens(i.e return to previous position)
            if self.board[self.position[0]][self.position[1]] == 1:
                self.position -= action     
            
            #mark the new positon on board
            self.board[self.position[0]][self.position[1]]=2

            self.score+=survival_reward
            return survival_reward,False

    def reset(self):
        
        #board created
        self.board = np.array([[0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 3],
            [0, 0, 0, 0, 1, 0]])
        
        #goal and agent position randomized
        self.goal = np.array([np.random.randint(0,self.board.shape[0]),np.random.randint(0,self.board.shape[1])])
        self.position = np.array([np.random.randint(0,self.board.shape[0]),np.random.randint(0,self.board.shape[1])])
        
        while self.goal[0] == self.position[0] and self.goal[1] == self.position[1]:
            self.position = np.array([np.random.randint(0,self.board.shape[0]),np.random.randint(0,self.board.shape[1])])
        
        #agent and goal position marked
        self.board[self.position[0]][self.position[1]] = 2
        self.board[self.goal[0]][self.goal[1]] = 3

if __name__ == "__main__":
    db = GridWorld(40, RandomAgent)
    db.run()
