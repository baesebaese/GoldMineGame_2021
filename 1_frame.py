#기본 뼈대 생성

import pygame

pygame.init()
screen_width = 1280
screen_hight = 720
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Gold Miner")

ruuning = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ruuning = False
    
pygame.quit()
