import pygame
from pygame.math import Vector2

class GameManager:
    def __init__(self):
    	pygame.init()
    	self.size = (500, 500)
    	self.screen = pygame.display.set_mode(self.size)

        self.colors = {'WHITE':(255,255,255), 'blue': (0,0,255), 'black': (0,0,0)}

        # Define the cart variables here
        self.cart = Vector2(0,0)

    def draw(self):
    	pygame.draw.rect(self.screen, self.colors['blue'], (self.cart.x, self.cart.y, self.cart.x+100, self.cart.y+100))

    # All the physics code will be added here
    def update(self):
        self.cart = self.cart + Vector2(1, 1)

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
