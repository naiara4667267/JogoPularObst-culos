

import pygame


# Começa o Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))


while True:
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
         pygame.quit() #fecha a janela
         quit()  #finaliza o pygame





