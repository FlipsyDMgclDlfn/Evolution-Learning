import pygame
from random import *

pygame.init()
display = pygame.display.set_mode((800,600))
display.fill((255,0,255))


class Tile:    
    def __init__(self,x,y):
        foodChance = 30
        maxFood = 20
        minFood = 10
        if randint(0,100) < foodChance: self.food = randint(minFood,maxFood)
        else: self.food = 0
        self.x = x
        self.y = y
        
class Land(Tile):
    def __init__(self,x,y):
        Tile.__init__(self,x,y)
        
class Water(Tile):
    def __init__(self,x,y):
        Tile.__init__(self,x,y)


class Map:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.board=[]
        for i in range(width):
            self.board+=[[]]
            for j in range(height):
                if randint(0,3) != 0: self.board[i] += [Land(i,j)]
                else: self.board[i] += [Water(i,j)]
    def draw(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] is Land:
                    pygame.draw.rect(display, (0,200,0),(i*(800/self.width),j*(600/self.width),(i+1)*(800/self.width),(j+1)*(600/self.width)))

ma = Map(40,30)
carryOn = True
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              carryOn = False
    ma.draw()
