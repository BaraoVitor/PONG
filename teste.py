import pygame
import random

from pygame.display import set_mode
from pygame.examples.go_over_there import running, clock

#iniciar jogo
pygame.init()
#cores
black = (0,0,0)
white = (255,255,255)

# configuraçao de tela
WIDHT, HEIGHT = 800, 600
WIN = pygame.display,set_mode((WIDHT, HEIGHT))
pygame.display.set_caption('pong')

#variaveis do jogo
player_width, player_height = 10,100
bola_siza = 10
bola_speed_x = 3
bola_speed_y = 3
player_speed = 5

#posiçoes e velocidade inicial
player1x, player2x = 50, WIDHT - 50 - player_width
player1y, player2y = HEIGHT // 2, HEIGHT // 2
boladx = bola_speed_x * random.choice([1, -1])
bolady = bola_speed_y * random.choice([1, -1])

#pontuaçao
ponto1, ponto2 = 0, 0
font = pygame.font.Font(None, 36)

#Function para desenhar
def draw_objects():
    WIN.fill(black)
    pygame.draw.rect(WIN, white,(player1x, player1y, player_width, player_height))
    pygame.draw.rect(WIN, white, (player2x, player2y, player_width, player_height))
    pygame.draw.circle(WIN, white, (boladx, bolady), bola_siza )

#loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame .event.get():
        if event.type == pygame.QUIT:
            running = False
