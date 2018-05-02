import pygame
import time
from random import *

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
            
    def draw(self, display, xsize, ysize):
        if self.food != 0:
            pygame.draw.rect( display, (0,self.food*12,0),( (self.x)*(xsize), (self.y)*(ysize), xsize, ysize ) )
        else:
            pygame.draw.rect( display, (222,184,135),( (self.x)*(xsize), (self.y)*(ysize), xsize, ysize ) )

class Map:
    def __init__(self, width, height, display):
        self.width = width
        self.height = height
        self.display = display
        self.board = []
        for i in range(height):
            self.board += [[]]
            for j in range(width):
                self.board[i] += [Tile(j,i)]
    def draw(self):
        w, h = pygame.display.get_surface().get_size()
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j].draw(self.display, w/self.width, h/self.height)

