import pygame
import time
from random import *
from MapGeneration import *
from Species import *
from Animal import *

pygame.init()
WIDTH = 600
HEIGHT = 600
display = pygame.display.set_mode((WIDTH,HEIGHT))
display.fill((255,255,255))
clock = pygame.time.Clock()

m = Map(120,120,display)
m.draw()
s = [Species("Bunny",(255,255,255),m.board,display)]
for species in s:
    species.generateRandom(10)
    species.draw()

run = True
while run:
    pygame.event.pump()
    m.draw()
    for species in s:
        for animal in species.animals:
            animal.moveTowards(animal.closestFood().x,animal.closestFood().y)
            animal.eat()
            animal.closestFood()
        species.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              run = False
    
    pygame.display.update()
    clock.tick(30)
