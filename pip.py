import pygame, sys


venta= pygame.display.set_mode((800,600))

game_over=False

while not False:
    for event in pygame.event.get():
        print (event)
        if event.type == pygame.QUIT:
            sys.exit()