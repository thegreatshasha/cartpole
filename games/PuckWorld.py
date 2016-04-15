from abstract import AbstractGame
#import os
#os.environ['SDL_VIDEODRIVER'] = 'dummy'

#import pygame
import numpy as np
import random
import time
from ..agents.random import RandomAgent
from ..agents.qlearning import QAgent

class PuckWorld(AbstractGame):

    def __init__(self, config, Agent):
        
        self.size = config['size']
        
        self.agent = {}
        self.predator = {}
        self.food = {}
        #initially predetor,agent and food anywhere on board
        self.predator['radius']=40
        self.predator['pos'] = np.array( [ np.random.random_sample()*self.size , np.random.random_sample()*self.size ] )
        self.predator['vel'] = np.array( [ np.random.random_sample()*self.size , np.random.random_sample()*self.size ] )
        
        self.agent['radius']=10
        self.agent['pos'] = np.array( [ np.random.random_sample()*self.size , np.random.random_sample()*self.size ] )
        self.agent['vel'] = np.array( [0,0] )

        self.food['radius']=2
        self.food['pos'] = ( [ np.random.random_sample()*self.size , np.random.random_sample()*self.size ] )
        
        # Game player #
        self.player = Agent(self.get_ranges())

        # Game statistics
        self.score = 0


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
        return [ np.arange(0, size, 1) for _ in range(6) ] + [ np.arange(-10,12,2) for _ in range(2) ]\
        + [ np.arange(0, 4, 1) ]
        

    def draw(self):
        pass

    def checkbounce(self,agent):
        
        if agent['pos'][0] > size:
            agent['pos'][0] = size
            agent['vel'][0] = -1.0 * a['vel'][0]
        
        if agent['pos'][1] > size:
            agent['pos'][1] = size
            agent['vel'][1] = -1.0 * a['vel'][1]

       
    def physics(self, action):
        
        
        #update agent vel
        action_legend = { 0 : np.array( [1,0] ), 1 : np.array( [-1,0] ), 2 : np.array( [0,1] ), 3 : np.array( [0,-1] ) }  
        self.agent['vel'] = self.agent['vel'] + action_legend[action]
        
        #update agent position
        self.agent['pos'] = self.agent['pos'] + self.agent['vel']
        
        #checked if at limits and position and velocity adjusted
        self.checkbounce(self.agent)

        #update predator vel
        predator_to_agent=self.agent['pos']-self.agent['pos']
        self.predator['vel']=0.5*predator_to_agent
        
        #update predator pos
        self.predator['pos']=self.predator['pos']+self.predator['vel']

        #update food position
        food_rebirth_rate=np.random.random_sample()*5
        if(np.random.random_sample()*100<food_rebirth_rate):
            self.food['pos'] = ( [ np.random.random_sample()*self.size , np.random.random_sample()*self.size ] )

       #scoring
        reward,punishment=0.0,0.0
        p2a=np.sqrt(np.sum(np.square(predator_to_agent)))
        if p2a<self.predator['radius']:
            punishment=1.0/(p2a+1)*-1000.0
        a2f= p2a=np.sqrt(np.sum(np.square(self.agent['pos']-self.food['pos'])))
        reward=1.0/(a2f+1)*1.0
        score+=reward+punishment

        return score,False

    def update(self):
        self.draw()
        prev_state = self.get_state()
        action = self.player.choose_action(prev_state) # Decide best action according to the agent
        reward, terminal = self.physics(action) # Execute that action
        next_state = self.get_state() # Get next state
        self.agent.update_Qvalue(prev_state, action, next_state, reward, terminal)

    def run(self):
        for i in range(10000000):
            time.sleep(0.01)
            if i%200==0:
                print self.score, i
                self.score = 0
            #if i%2000 == 0:
            #    self.score = 0
            self.update()
            
            #self.agent.update_epsilon(i, 50000)

if __name__ == "__main__":
    db = PuckWorld({'size': (4,4)}, RandomAgent)
    db.run()
