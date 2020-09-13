import pygame, sys
def Screen():
    pygame.init()
    WHITE=(255,255,255)
    GREEN=(0,255,0)
    size=(800,500) # 800 de ancho 500 de largo
    # crearventana
    screen=pygame.display.set_mode(size)
    while True:
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
              sys.exit()
        screen.fill(WHITE)
    
        pygame.draw.line(screen,GREEN,[0,100],[100,100],5)

        pygame.display.flip()

BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,250)
Screen()