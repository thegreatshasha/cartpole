from abstract import AbstractGame
#import os
#os.environ['SDL_VIDEODRIVER'] = 'dummy'
import pygame
from ..datastructures.vec2d import Vec2d as Vector2
import math as m

#import pygame
import numpy as np
import random
import time
from ..agents.random_a import RandomAgent
from ..agents.qlearning import QAgent
#from ..agents.qlearning import QAgent

class PuckWorld(AbstractGame):

    def __init__(self, config, Agent):

        self.size = config

        self.agent = {}
        self.predator = {}
        self.food = {}
        #initially predetor,agent and food anywhere on board
        self.predator['radius']=20
        self.predator['pos'] = np.array( [ np.random.random_sample()*self.size , np.random.random_sample()*self.size ] )
        self.predator['vel'] = np.array( [ np.random.random_sample()*self.size , np.random.random_sample()*self.size ] )

        self.agent['radius']=10
        self.agent['pos'] = np.array( [ np.random.random_sample()*self.size , np.random.random_sample()*self.size ] )
        self.agent['vel'] = np.array( [0.0,0.0] )

        self.food['radius']=10
        self.food['pos'] = np.array( [ np.random.random_sample()*self.size , np.random.random_sample()*self.size ] )

        # Game player #
        self.player = Agent(self.get_ranges())

        # Game statistics
        self.score = 0

        #display code
        pygame.init()
        self.size_vec = Vector2(self.size +100, self.size+100)
        self.screen = pygame.display.set_mode(self.size_vec)
        self.colors = {'white':(255,255,255), 'red': (255,0,0), 'blue': (0,0,255), 'black': (0,0,0), 'green':(0,255,0)}


    def get_state(self):
        #state is a np array with all state variable values
        state = []
        for i in [ self.predator['pos'] , self.food['pos'] , self.agent['pos'] , self.agent['vel'] ]:
            state.extend(i.tolist())
        return  np.asarray(state)


    def get_ranges(self):
        # Return state ranges for board and actions #
        #states 0,1,....size-1 for all posx,posy
        #states -10 to 10 for vx,vy of agent
        #actions 0,1,2,3 for agent
        return [ np.arange(0, self.size, 1) for _ in range(6) ] + [ np.arange(-10,12,2) for _ in range(2) ]\
        + [ np.arange(0, 5, 1) ]

    def getPossibleActions(self):
        return np.array([0, 1, 2, 3])


    def draw(self):
        self.screen.fill(self.colors['black'])
        pygame.draw.rect(self.screen, self.colors['white'], (0,0,self.size,self.size), 2)

        pygame.draw.circle(self.screen, self.colors['green'], (int(self.food['pos'][0]), int(self.food['pos'][1])), self.food['radius'])
        pygame.draw.circle(self.screen, self.colors['blue'], (int(self.agent['pos'][0]),int(self.agent['pos'][1])),self.agent['radius'])
        pygame.draw.circle(self.screen, self.colors['red'], (int(self.predator['pos'][0]), int(self.predator['pos'][1])),self.predator['radius'])
        pygame.display.flip()
        #import pdb;pdb.set_trace()
    def checkbounce(self,agent):


        if agent['pos'][0] > self.size:
            agent['pos'][0] = self.size
            agent['vel'][0]=-agent['vel'][0]
            #agent['vel']=np.array([0.0,0.0])

        elif agent['pos'][0]<0.0:
            agent['pos'][0] = 0.0
            agent['vel'][0]=-agent['vel'][0]
            #agent['vel']=np.array([0.0,0.0])

        if agent['pos'][1] >self.size:
            agent['pos'][1] = self.size
            agent['vel'][1]=-agent['vel'][1]

        elif agent['pos'][1] <0.0:
            agent['pos'][1] = 0.0
            agent['vel'][1]=-agent['vel'][1]



    def act(self, action):

        #update agent vel
        action_legend = { 0 : np.array( [1.0,0.0] ), 1 : np.array( [-1.0,0.0] ), 2 : np.array( [0.0,1.0] ), 3 : np.array( [0.0,-1.0] ) }
        action_constant=1.1
        #print 'action is:%d'%action
        self.agent['vel'] = self.agent['vel'] + action_legend[action]*action_constant
        #print "agent vel:"
        #print self.agent['vel']


        if self.agent['vel'][0]>5.0:
            self.agent['vel'][0]=5.0

        if self.agent['vel'][0]<-5.0:
            self.agent['vel'][0]=-5.0



        #update agent position
        self.agent['pos'] = self.agent['pos'] + self.agent['vel']

        #checked if at limits and position and velocity adjusted
        self.checkbounce(self.agent)

        #update predator vel
        predator_velocity_constant=1.0/self.size
        predator_to_agent=self.agent['pos']-self.predator['pos']
        self.predator['vel']=predator_velocity_constant*predator_to_agent

        #update predator pos
        self.predator['pos']=self.predator['pos']+self.predator['vel']


        #update food position
        food_rebirth_rate=np.random.random_sample()*5.0
        if(np.random.random_sample()*100.0<food_rebirth_rate):
            self.food['pos'] = np.array( [ np.random.random_sample()*self.size , np.random.random_sample()*self.size ] )

       #scoring
        reward,punishment=0.0,0.0
        p2a=np.sqrt(np.sum(np.square(predator_to_agent)))
        if p2a<self.predator['radius']:
            punishment=1.0/(p2a+1.0)*-1.0
        a2f= p2a=np.sqrt(np.sum(np.square(self.agent['pos']-self.food['pos'])))
        reward=1.0/(a2f+1.0)*1.0
        self.score+=reward+punishment

        return self.score,False

if __name__ == "__main__":
    db = PuckWorld(40, RandomAgent)
    db.run()
