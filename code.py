import pygame
from vec2d import Vec2d as Vector2
import math as m
import numpy as np
from pid import Pid

class GameManager:
    
    def __init__(self):
    	
        #display attributes
        pygame.init()
    	self.size = (1024, 768)
        self.size_vec = Vector2(1024, 768)
    	self.screen = pygame.display.set_mode(self.size)
        self.colors = {'WHITE':(255,255,255), 'red': (255,0,0), 'blue': (0,0,255), 'black': (0,0,0)}
        
        #world attr
        self.g=980.0#cm/sec^2
        self.dt=0.005
        #peg-att
        #initial state: config
        self.peg=Vector2(512.0,100.0)
        self.peg_v=0.0
        self.peg_a=0.0
        
        #ball-att
        self.ball_length=100.0
        
        #initial state: config
        self.ball_theta=m.pi/2#[0,2*pi]
        self.ball_omega=0.0

        

        self.ball_alpha=self.g/self.ball_length*m.sin(self.ball_theta)+self.peg_a/self.ball_length*m.cos(self.ball_theta)
        
        self.ball=Vector2(self.polar_cart())
        #self.ball(x,y)
        """
        # Define the cart variables here
        self.cart = Vector2(500,100)
        self.cart_size = Vector2(50, 10)
        

        self.cart_v = Vector2(1,0)
        self.ball_v = Vector2(1,2)

        self.cart_a = Vector2(0,0)
        self.ball_a = Vector2(0,1)
        """
    def get_dt(self):
        return self.dt

    def getTheta(self):
        return self.ball_theta

    def polar_cart(self):
        x=int(self.peg.x-self.ball_length*m.sin(self.ball_theta))
        y=int(self.peg.y-self.ball_length*m.cos(self.ball_theta))
        return x,y

    def draw(self):
        pygame.draw.circle(self.screen, self.colors['blue'], (int(self.peg.x), int(self.peg.y)), 10)
        pygame.draw.circle(self.screen, self.colors['blue'], self.ball, 5)
        pygame.draw.line(self.screen, self.colors['blue'], self.peg, self.ball)
        """
        pygame.draw.circle(self.screen, self.colors['blue'], (int(self.ball.x), int(self.ball.y)), 10)
        pygame.draw.rect(self.screen, self.colors['red'], (self.cart.x, self.cart.y, 50, 10))
        pygame.draw.line(self.screen, self.colors['blue'], self.cart + self.cart_size/2, self.ball)
        """
    # All the physics code will be added here
    def update(self,accel):
        #higher order terms removed
        #alpha,accel fixed for this timestep->end of dt update alpha,accel
        dt=self.dt
        #define states at the current timestep
        x=np.array([[self.ball_theta],[self.ball_omega],[self.ball_alpha]])
        x_peg=np.array([[self.peg.x],[self.peg_v],[self.peg_a]])
        
        #states at end of current time step->update
        F=np.array([[1,dt,dt**2.0/2],[0,1,dt],[0,0,1]])
        y=np.dot(F,x)
        y_peg=np.dot(F,x_peg)


        #update theta and omega
        self.ball_theta=y[0][0]%(2*m.pi)
        self.ball_omega=y[1][0]
        #update v,a
        self.peg=Vector2(y_peg[0][0]%(self.size_vec.x),self.peg.y)
        self.peg_v=y_peg[1][0]
        
        #add our input to the sytem: accel->alpha(accel,theta)
        self.peg_a=accel 
        self.ball_alpha=self.g/self.ball_length*m.sin(self.ball_theta)+self.peg_a/self.ball_length*m.cos(self.ball_theta)
        
        self.ball=Vector2(self.polar_cart())
        """
        self.cart = (self.cart + self.cart_v) % self.size_vec
        self.ball = (self.ball + self.ball_v) % self.size_vec

        self.cart_v = self.cart_v + self.cart_a
        self.ball_v = self.ball_v + self.ball_a
        """
    def run(self,a):
        
        
        self.screen.fill(self.colors['black'])
        self.draw()
        pygame.display.flip()
        reward = self.update(10*a.controlSignal(self.getTheta()))

def main():
    gm = GameManager()
    a=Pid(0.1, 0.3, 0.001,gm.get_dt())
    for i in range(10000000):
        gm.run(a)
    pygame.quit()


if __name__ == "__main__":
    print 'too'
    main()
