import pygame

pygame.init()

largura = 800
altura = 600
display = pygame.display.set_mode((largura, altura))
fps = pygame.time.Clock()

fundo = pygame.image.load("assets/fundo.png")
personagem = pygame.image.load("assets/personagem.png")

preto = (0, 0, 0)
branco = (255, 255, 255)

while True:
    #for evento in pygame.event.get():
        #pygame.quit()
        #quit()
    
    pygame.display.update()
    fps.tick(60)
    display.fill(branco)
    display.blit(fundo, (0,0))
    display.blit(personagem, (380, 400))