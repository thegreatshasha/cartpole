import pygame
from pygame.math import Vector2

class GameManager:
    def __init__(self):
    	pygame.init()
    	self.size = (1024, 768)
    	self.screen = pygame.display.set_mode(self.size)

        self.colors = {'WHITE':(255,255,255), 'red': (255,0,0), 'blue': (0,0,255), 'black': (0,0,0)}

        # Define the cart variables here
        self.cart = Vector2(500,100)
        self.ball = Vector2(100, 100)

    def draw(self):
        pygame.draw.circle(self.screen, self.colors['blue'], (int(self.ball.x), int(self.ball.y)), 10)
    	pygame.draw.rect(self.screen, self.colors['red'], (self.cart.x, self.cart.y, 100, 20))
        pygame.draw.line(self.screen, self.colors['blue'], (self.cart.x, self.cart.y), (self.ball.x, self.ball.y))

    # All the physics code will be added here
    def update(self):
        self.cart = self.cart + Vector2(1, 0)

        self.ball = self.ball + Vector2(1,1)

    def run(self):
        self.screen.fill(self.colors['black'])

    	reward = self.update()

    	self.draw()

    	pygame.display.flip()

def main():
    gm = GameManager()

    for i in range(10000):
        gm.run()

if __name__ == "__main__":
    main()
