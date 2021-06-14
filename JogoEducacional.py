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

personagemPosicaoX = 380
personagemPosicaoY = 405

movimentoX = 0
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                movimentoX = -5
            elif evento.key == pygame.K_RIGHT:
                movimentoX = 5
        if evento.type == pygame.KEYUP:
            movimento = 0                
    
    display.fill(branco)
    display.blit(fundo, (0,0))
    
    personagemPosicaoX = personagemPosicaoX + movimentoX
    if personagemPosicaoX < 0:
        personagemPosicaoX = 0
    elif personagemPosicaoX > 800:
        personagemPosicaoX = 800    
    display.blit(personagem, (personagemPosicaoX, personagemPosicaoY))

    pygame.display.update()
    fps.tick(60)