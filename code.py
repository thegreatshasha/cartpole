import pygame
from vec2d import Vec2d as Vector2
import math as m
import numpy as np

class GameManager:

    def __init__(self):

        #display attributes
        self.clock = pygame.time.Clock()
        pygame.init()
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
    def update(self):
        #higher order terms removed
        dt=0.0001
        x=np.array([[self.ball_theta],[self.ball_omega],[self.ball_alpha]])
        F=np.array([[1.0,dt,dt*dt/2.0],[0.0,1.0,dt],[0.0,0.0,1.0]])
        #print x.shape, F.shape
        y=np.dot(F,x)
        self.ball_theta=y[0][0]%(2*m.pi)
        self.ball_omega=y[1][0]
        self.ball_alpha=self.g/self.ball_length*m.sin(self.ball_theta)
        self.ball=Vector2(self.polar_cart())
        """
        self.cart = (self.cart + self.cart_v) % self.size_vec
        self.ball = (self.ball + self.ball_v) % self.size_vec

        self.cart_v = self.cart_v + self.cart_a
        self.ball_v = self.ball_v + self.ball_a
        """
    def run(self):
        self.screen.fill(self.colors['black'])
        self.draw()
        self.update()

def main():
    gm = GameManager()

    for i in range(10000000):
        for i in range(100):
            gm.run()
        gm.clock.tick(60)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    print 'too'
    main()
