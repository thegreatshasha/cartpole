import pygame

def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((500,400),0,32)

    WHITE=(255,255,255)
    blue=(0,0,255)

    DISPLAY.fill(WHITE)

    pygame.draw.rect(DISPLAY,blue,(200,150,100,50))

    while True:
        pygame.display.update()

if __name__ == "__main__":
    main()
