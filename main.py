import pygame
import time
from random import *
from MapGeneration import *

pygame.init()
WIDTH = 600
HEIGHT = 600
display = pygame.display.set_mode((WIDTH,HEIGHT))
display.fill((255,255,255))
clock = pygame.time.Clock()

ma = Map(120,120)
ma.draw(display)

run = True
while run:
    pygame.event.pump()
    display.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              run = False
    ma = Map(120,120)
    ma.draw(display)
    
    pygame.display.update()
    clock.tick(30)
