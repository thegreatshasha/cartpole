from abstract import AbstractGame
#import os
#os.environ['SDL_VIDEODRIVER'] = 'dummy'

#import pygame
import numpy as np
import random
import time

class DodgeBrick(AbstractGame):

    def __init__(self, config, player):
        #pygame.init()
		self.size = (4,4)
		self.screen = pygame.display.set_mode(self.transformed_size)
		self.player = player

        """ Represent board by matrix of zeros. 1 denotes agent. 2 denotes enemy """
        self.board = np.zeros()

        """ Physics variables """
        self.velocity = 0 # Left right velocity, can be -1, 0, 1. Decided each turn

    def get_state(self):
        """ Flatten board and return """
        pass

    def get_ranges(self):
        """ Return state ranges for board and actions """
        pass

    def draw(self):
        """ Draw to the terminal here """
        pass

    def physics(self):
        """ Update agent and enemy position via velocity. Detect collisions as well"""
        pass

    def update(self):
        pass

    def run(self):
        pass

if __name__ == "__main__":
    db = DodgeBrick({}, {})
    db.get_state()
