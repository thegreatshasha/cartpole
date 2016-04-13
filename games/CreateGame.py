import numpy as np
import math as m
import pdb
import random
import matplotlib.pyplot as plt
from TicTacToe import ticTacToe


def createGame(size):
	game = ticTacToe(size)
	game.setBoard()
	gs = False
	turn = np.random.randint(0,2)
	Qagent_played=False
	return game,turn,gs,Qagent_played
