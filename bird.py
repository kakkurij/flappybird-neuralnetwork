
from tkinter import PhotoImage
from perceptron import Perceptron
from random import random

class Bird():

    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        self.jumping = False
        self.jumpCount = 5
        self.brain = Perceptron(4)

        # genetic algorithm variables
        self.fittness = 0
        self.score = 0

    def update(self):
        self.score += 1
        if not self.jumping:
            self.y += 10+random()
        else:
            self.y -= 20
            self.jumpCount -= 1
            if self.jumpCount < 0:
                self.jumping = False
                

    def jump(self, event=None):
        self.jumping = True
        self.jumpCount = 5



    def getPos(self):
        return self.x, self.y

    def die(self):
        self.jumping = False
        self.jumpCount = 5
        
    def calculateFittness(self):
        self.fittness = self.score
        return self.fittness * self.score

    def predict(self, gapX, gapY, gapSize, height=700, width=550):
        inputs = [self.y/height, self.x/width - gapX/width, gapY/height, gapY/height+gapSize/height]
        output = self.brain.predict(inputs)
        return output

