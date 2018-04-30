import pygame
import time
from random import *

pygame.init()
WIDTH = 600
HEIGHT = 600
display = pygame.display.set_mode((WIDTH,HEIGHT))
display.fill((255,255,255))
clock = pygame.time.Clock()

class Tile:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        foodChance = 30
        maxFood = 20
        minFood = 10
        r=randint(0,100)        
        if r < foodChance:
            self.food = randint(minFood,maxFood)
        else:
            self.food = 0
            
    def draw(self, xsize, ysize):
        if self.food != 0:
            pygame.draw.rect( display, (0,200,0),( (self.x)*(xsize), (self.y)*(ysize), xsize, ysize ) )
        else:
            pygame.draw.rect( display, (222,184,135),( (self.x)*(xsize), (self.y)*(ysize), xsize, ysize ) )

class Map:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.board = []
        for i in range(height):
            self.board += [[]]
            for j in range(width):
                self.board[i] += [Tile(j,i)]
    def draw(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j].draw(WIDTH/self.width,HEIGHT/self.height)

ma = Map(120,120)
ma.draw()

carryOn = True
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              carryOn = False

    pygame.display.update()
    clock.tick(30)
