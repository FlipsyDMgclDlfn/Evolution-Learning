import pygame
import time
from random import *
import MapGeneration

pygame.init()
WIDTH = 600
HEIGHT = 600
display = pygame.display.set_mode((WIDTH,HEIGHT))
display.fill((255,255,255))
clock = pygame.time.Clock()

ma = Map(120,120)
ma.draw(display)

carryOn = True
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              carryOn = False

    pygame.display.update()
    clock.tick(30)
