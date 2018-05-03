import pygame
from random import *
from Species import *

class Animal:
    def __init__(self,species,x,y):
        self.species = species
        self.x = x
        self.y = y
        self.energy = species.energy
        self.health = species.health
        self.food = 0

    def eat(self):
        if self.energy >= self.species.eTE:
            self.energy -= 0#self.species.eTE
            if self.species.board[self.y][self.x].food > 0:
                self.food += self.species.board[self.y][self.x].food
                self.energy += self.species.board[self.y][self.x].food * self.species.eFromV
                self.species.board[self.y][self.x].food = 0
        if self.species.maxE < self.energy:
            self.energy = self.species.maxE

    def moveTowards(self,x,y):
        if self.x != x:
            if self.x > x:
                self.x -= 1
            else:
                self.x += 1
        if self.y != y:
            if self.y > y:
                self.y -= 1
            else:
                self.y += 1

    def hit(self,other):
        if self.energy >= self.species.eTH:
            self.energy -= self.species.eTH
            other.health -= self.damage
            if other.health <= 0:
                self.enegy += self.eFromA
                self.food += other.food + 1
                other.food = 0

    def closestFood(self):
        x = 0#randint(0,len(self.species.board)-1)
        y = 0#randint(0,len(self.species.board[0])-1)
        distance = ( ((abs(x-self.x))**2) + ((abs(y-self.y))**2) )**(1/2)
        ymin = self.y - 5
        ymax = self.y + 5
        if ymin < 0:
            ymin = 0
        if ymax >= len(self.species.board):
            ymax = len(self.species.board) - 1
        xmin = self.y - 5
        xmax = self.y + 5
        if xmin < 0:
            xmin = 0
        if xmax >= len(self.species.board[0]):
            xmax = len(self.species.board[0]) - 1
        for i in range (ymin, ymax):
            for j in range (xmin, xmax):
                if self.species.board[i][j].food > 0:
                    if (((abs(j-self.x))**2)+((abs(i-self.y))**2))**(1/2) <= distance:
                        x = j
                        y = i
                        distance = (((abs(x-self.x))**2)+((abs(y-self.y))**2))**(1/2)
        return self.species.board[y][x]
                        

    def draw(self,display,xsize,ysize):
        pygame.draw.rect( display, self.species.color,( (self.x)*(xsize), (self.y)*(ysize), xsize, ysize ) )
