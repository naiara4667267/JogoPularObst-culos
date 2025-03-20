import pygame

print("Setup Start")
# Começa o Pygame
pygame.init()

window = pygame.display.set_mode(size=(600, 480))
print("Setup End")

print("Loop Start")

while True:
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
         pygame.quit() #fecha a janela
         quit()  #finaliza o pygame





