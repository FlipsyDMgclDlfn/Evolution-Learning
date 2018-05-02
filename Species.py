from random import *
import pygame
from Animal import *
class Species:
    def __init__(self, name, color, board, display):
        self.display = display
        self.board = board
        self.animals = []
        self.name = name
        self.color = color
        self.size = 20
        self.maxE = 20
        self.energy = 10
        self.eFromV = 2
        self.eFromA = 0
        self.eTE = 1
        self.eTH = 2
        self.health = 10
        self.damage = 2
        
    def generateRandom(self,x):
        for i in range(x):
            self.animals += [Animal(self,randint(0,len(self.board)),randint(0,len(self.board[0])))]

    def draw(self):
        w, h = pygame.display.get_surface().get_size()
        for animal in self.animals:
            animal.draw(self.display, w/len(self.board), h/len(self.board[0]))
        
        
