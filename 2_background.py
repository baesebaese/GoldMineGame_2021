# 배경 이미지 설정

import pygame
import os

pygame.init()
screen_width = 1280
screen_hight = 720
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Gold Miner")
clock = pygame.time.Clock()

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
background = pygame.image.load(os.path.join(current_path, "background.png"))

running = True
while running:
    clock.tick(30) # FPS 값이 30으로 고정

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ruuning = False
    
    screen.blit(background, (0, 0))
    pygame.display.update()

pygame.quit()
