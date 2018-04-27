import pygame
import time
from random import *

pygame.init()
display = pygame.display.set_mode((600,600))
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
            self.food = int(randint(minFood,maxFood))
        else:
            self.food = int(0)
        
    def draw(self):
        if int(self.food) != int(0):
            pygame.draw.rect( display, (0,200,0),( (self.x)*(20), (self.y)*(20), (self.x+1)*(20), (self.y+1)*(20) ) )


class Map:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.board=[]
        for i in range(width):
            self.board+=[[]]
            for j in range(height):
                self.board[i] += [Tile(i,j)]
    def draw(self):
        for i in range(self.width):
            for j in range(self.height):
                self.board[i][j].draw()

ma = Map(30,30)
ma.draw()
print(a,b)
carryOn = True
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              carryOn = False

    pygame.display.update()
    clock.tick(30)
