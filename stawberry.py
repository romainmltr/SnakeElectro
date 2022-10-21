import pygame
import random

i = 0
class Stawberry:
    def __init__(self, x, y):
        self.speed =+ 5
        self.x = x
        self.y = y
    def Draw(self, ecran):
        pygame.draw.rect(ecran, (250, 0, 0), pygame.Rect(self.x, self.y, 50, 50))
    def get_random_location(self,width,height):
        self.x , self.y = random.randrange(40, width - 40),random.randrange(40, height - 40)
