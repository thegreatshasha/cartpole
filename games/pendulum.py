import pygame
from vec2d import Vec2d as Vector2
import math as m
import numpy as np
import random
from agent import QAgent

class GameManager:

    def __init__(self):

        #display attributes
        self.clock = pygame.time.Clock()
        pygame.init()
        self.font=pygame.font.Font(None,30)
    	self.size = (1024, 768)
        self.size_vec = Vector2(1024, 768)
    	self.screen = pygame.display.set_mode(self.size)
        self.colors = {'WHITE':(255,255,255), 'red': (255,0,0), 'blue': (0,0,255), 'black': (0,0,0)}

        #world attr
        self.g=980.0#cm/sec^2

        #peg-att
        self.peg=Vector2(512.0,100.0)

        #ball-att
        self.ball_length=100.0

        #initial state: config
        self.ball_theta=m.pi/2#[0,2*pi]
        self.ball_omega=0.0
        self.ball_alpha=self.g/self.ball_length*m.sin(self.ball_theta)

        self.ball_theta_min = 10000
        self.ball_theta_max = -10000

        self.ball_omega_min = 10000
        self.ball_omega_max = -10000

        self.ball=Vector2(self.polar_cart())
        #self.ball(x,y)

        self.player = QAgent(self.get_ranges())

    def polar_cart(self):
        x=int(self.peg.x-self.ball_length*m.sin(self.ball_theta))
        y=int(self.peg.y-self.ball_length*m.cos(self.ball_theta))
        return x,y

    def calculate_min_max(self):
        self.ball_theta_min = min(self.ball_theta_min, self.ball_theta)
        self.ball_theta_max = max(self.ball_theta_max, self.ball_theta)

        self.ball_omega_min = min(self.ball_omega_min, self.ball_omega)
        self.ball_omega_max = max(self.ball_omega_max, self.ball_omega)

    def draw_texts(self):
        scoretext=self.font.render("Theta: %f[%f-%f], Omega: %f[%f-%f], Alpha: %f" % (self.ball_theta, self.ball_theta_min, self.ball_theta_max, self.ball_omega, self.ball_omega_min, self.ball_omega_max, self.ball_alpha), 1,(255,255,255))
        self.screen.blit(scoretext, (0, 457))

    def draw(self):
        self.screen.fill(self.colors['black'])

        pygame.draw.circle(self.screen, self.colors['blue'], (int(self.peg.x), int(self.peg.y)), 10)
        pygame.draw.circle(self.screen, self.colors['blue'], self.ball, 5)
        pygame.draw.line(self.screen, self.colors['blue'], self.peg, self.ball)

        self.draw_texts()

    def get_state(self):
        return [self.ball_theta, self.ball_omega]

    def get_ranges(self):
        # Returns ranges for each state and last but not the least, action
        return [np.arange(0, m.pi*2, m.pi/64), np.arange(-100, 100, 10), np.arange(-10*self.g, 10*self.g, 1)]

    def tangential_force(self, f):
        self.ball_alpha = f/self.ball_length
        return self.ball_alpha

    # All the physics code will be added here
    def update(self, action):
        #higher order terms removed
        dt=0.01
        x=np.array([[self.ball_theta],[self.ball_omega],[self.ball_alpha]])
        F=np.array([[1.0,dt,dt*dt/2.0],[0.0,1.0,dt],[0.0,0.0,1.0]])
        #print x.shape, F.shape
        y = np.dot(F,x)
        self.ball_theta=y[0][0]%(2*m.pi)
        self.ball_omega=(y[1][0]%10)*(y[1][0]/abs(y[1][0]))

        # Apply
        self.tangential_force(100)
        #action = 0
        self.tangential_force(self.g*m.sin(self.ball_theta) + action)

        self.ball=Vector2(self.polar_cart())

        self.calculate_min_max()

    def run(self):
        # Core algorithm, everything happens here
        prev_state = self.get_state()
        action = self.player.choose_action(prev_state) # Decide best action according to the agent
        self.update(action) # Execute that action
        next_state = self.get_state() # Get next state
        reward = self.player.get_reward(prev_state, next_state, action)
        self.player.update_Qvalue(prev_state, action, next_state, reward)
        self.draw()

def main():
    gm = GameManager()

    for i in range(10000000):
        gm.run()
        gm.clock.tick(60)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    print 'too'
    main()
