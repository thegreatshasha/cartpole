from abstract import AbstractGame
#import os
#os.environ['SDL_VIDEODRIVER'] = 'dummy'

#import pygame
import numpy as np
import random
import time
from ..agents.random import RandomAgent
from ..agents.neural import NeuralLearner

class DodgeBrick(AbstractGame):

    def __init__(self, config, Agent):
        #pygame.init()
        self.size = config['size']
        #self.screen = pygame.display.set_mode(self.transformed_size)

        #Represent board by matrix of zeros. 1 denotes agent. 2 denotes enemy #
        self.board = np.zeros(self.size)

        # Physics variables. It will be interesting to note if the agent dodges a random agent #
        self.enemy = {}
        self.player = {}
        self.enemy['pos'] = np.array([0, np.random.choice(self.size[0])])
        self.enemy['vel'] = np.array([1, 0])

        self.player['pos'] = np.array([self.size[0]-1, np.random.choice(self.size[0])])
        self.player['vel'] = np.array([0, 0])

        # Game player #
        self.agent = Agent(self.get_ranges())

        # Game statistics
        self.score = 0

    def get_state(self):
        # Flatten board and return #
        return self.board.flatten()

    def get_ranges(self):
        # Return state ranges for board and actions #
        return [np.arange(0, 2+1+1, 1) for el in self.board.flatten()] + [np.arange(-1, 1+1+1, 1)]

    def draw(self):
        # Draw to the terminal here #
        #print(chr(27) + "[2J")
        #print self.board
        #print self.score
        pass

    def act(self, action):
        # Agent chooses the player's velocity
        self.player['vel'][1] = action

        # Erase previous position in board #
        self.board[tuple(self.player['pos'])] = 0
        self.board[tuple(self.enemy['pos'])] = 0

        # Update agent and enemy position via velocity. Detect collisions as well#
        self.player['pos'] = (self.player['pos'] + self.player['vel']) % self.size
        self.enemy['pos'] = (self.enemy['pos'] + self.enemy['vel']) % self.size

        # Write new position #
        self.board[tuple(self.player['pos'])] = 1
        self.board[tuple(self.enemy['pos'])] = 2
        #print self.player, self.enemy
        if np.array_equal(self.player['pos'], self.enemy['pos']):
            #print "Boom"
            self.score -= 30
            return -30, True
        else:
            self.score += 1
            return 1, False

if __name__ == "__main__":
    # Create the keras network here
