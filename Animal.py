import pygame
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

    def draw(self,display,xsize,ysize):
        pygame.draw.rect( display, self.species.color,( (self.x)*(xsize), (self.y)*(ysize), xsize, ysize ) )
