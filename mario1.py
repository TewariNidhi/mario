import pygame
import sys
pygame.init()
WINDOW_WIDTH=1200
WINDOW_HEIGHT=600
canvas=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
BLACK=(0,0,0)
def start_game():
    canvas.fill(BLACK)
    start_img=pygame.image.load('start.png')
    start_img_rect= start_img.get_rect()
    start_img_rect.center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2)
    canvas.blit(start_img, start_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                #game_loop()
        pygame.display.update()

start_game()