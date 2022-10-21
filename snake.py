import pygame
pygame.init()
class Snake :
    def __init__(self, x, y):
        self.score = 0
        self.x = x
        self.y = y
        self.speed = 0
        self.body = []
        self.to = "right"
        self.length = 1

    def Draw(self, ecran):
        for body in self.body:
                pygame.draw.rect(ecran,(0, 0, 255), pygame.Rect(body[0], body[1], 50, 50))

    def moove(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.to = "left"
                if event.key == pygame.K_RIGHT:
                    self.to = "right"
                if event.key == pygame.K_UP:
                    self.to = "up"
                if event.key == pygame.K_DOWN:
                    self.to = "down"

        if self.to == "left": # Take Speed
            self.x -= 20
        elif self.to == "right":
            self.x += 20
        elif self.to == "down":
            self.y += 20
        elif self.to == "up":
            self.y -= 20

        self.body.append([self.x,self.y])
        if len(self.body) > self.length:
            del self.body[0]
