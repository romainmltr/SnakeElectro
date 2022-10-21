import pygame
from score import Score
from snake import Snake
from stawberry import Stawberry
from math import *
from mixer import music
import random

pygame.init()
score = Score()
score.TotalScore

stawberry = Stawberry(2,6)
stawberry.get_random_location(750,750)

snake = Snake(3,5)
font = pygame.font.SysFont('Arial', 40)

ecran = pygame.display.set_mode((800,800))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
music("./music.wav",0.5)
clock = pygame.time.Clock()

SnakeGame = True
i = 0

def AcidTechno():
    colour_r = random.randint(0,255)
    colour_g = random.randint(0,255)
    colour_b = random.randint(0,255)
    return (colour_r,colour_g,colour_b)
counter = 0

while SnakeGame:
    ecran.fill((AcidTechno()))
    snake.moove()
    counter += 1
    d = sqrt((snake.x - stawberry.x) **2 + (snake.y - stawberry.y)**2)

    """for j in snake.body:
        z = sqrt((snake.x - j[0]) ** 2 + (snake.y - j[1]) ** 2)
                                                                            Partie de la  collision 
    ##if z <= 25:
    ##print(z)
    ##SnakeGame = False* """

    if d < 50 :
        ## Touche
        stawberry.Draw(ecran)
        score.TotalScore += 1
        stawberry.get_random_location(800, 800)
        snake.body.append([snake.x, snake.y])
        snake.length += 1
        print(score.TotalScore)
        print(snake.x)

    ## collision avec la frontiere
    if snake.x >= 750 or snake.x <=0:
        SnakeGame = False
    if snake.y >= 750 or snake.y <=0:
        SnakeGame = False

    if counter > 3:
        colour = AcidTechno()
        counter = 0

    snake.Draw(ecran)
    stawberry.Draw(ecran)
    variable1 = font.render(str(score.TotalScore), False, (255, 255, 255))
    ecran.blit(variable1, (60,0))
    pygame.display.flip()
    clock.tick(30)

pygame.quit()


#EDTA
