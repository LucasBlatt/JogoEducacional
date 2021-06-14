import pygame

pygame.init()

largura = 800
altura = 600
display = pygame.display.set_mode((largura, altura))
fps = pygame.time.Clock()

while True:
    for evento in pygame.event():
        pygame.quit()
        quit()
    
    pygame.display.update()
    fps.tick(60)