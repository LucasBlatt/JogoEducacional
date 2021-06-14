from funcoesDoJogo import textos, mensagensNoDisplay, morte

import pygame
import random
import time

pygame.init()

icone = pygame.image.load("assets/icone.png")
pygame.display.set_caption("Junk Food Runner")
pygame.display.set_icon(icone)

largura = 800
altura = 600
display = pygame.display.set_mode((largura, altura))
fps = pygame.time.Clock()

fundo = pygame.image.load("assets/fundo.png")
personagem = pygame.image.load("assets/personagem.png")
porcarias = [pygame.image.load("assets/food1.png"), pygame.image.load("assets/food2.png"),
    pygame.image.load("assets/food3.png"), pygame.image.load("assets/food4.png"),
        pygame.image.load("assets/food5.png")]
porcariasRandom = random.choice(porcarias)

branco = (255, 255, 255)

def jogo():
    personagemPosicaoX = 380
    personagemPosicaoY = 405
    personagemLargura = 110
    movimentoX = 0
    porcariasPosicaoX = 380
    porcariasPosicaoY = -220
    porcariasLargura = 50
    porcariasAltura = 22
    porcariasVelocidade = 5
    desvios = 0

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
                movimentoX = 0                
        
        display.fill(branco)
        display.blit(fundo, (0,0))
        
        personagemPosicaoX = personagemPosicaoX + movimentoX
        if personagemPosicaoX < 0:
            personagemPosicaoX = 0
        elif personagemPosicaoX > 760:
            personagemPosicaoX = 760    
        display.blit(personagem, (personagemPosicaoX, personagemPosicaoY))

        display.blit(porcariasRandom, (porcariasPosicaoX, porcariasPosicaoY))
        porcariasPosicaoY = porcariasPosicaoY + porcariasVelocidade
        if porcariasPosicaoY > altura:
            porcariasPosicaoY = -220
            porcariasVelocidade += 1
            porcariasPosicaoX = random.randrange(0,largura - 50)
            desvios += 1

        if personagemPosicaoY < porcariasPosicaoY + porcariasAltura:
            if personagemPosicaoX < porcariasPosicaoX and personagemPosicaoX + personagemLargura > porcariasPosicaoX or porcariasPosicaoX + porcariasLargura > personagemPosicaoX and porcariasPosicaoX + porcariasLargura < personagemPosicaoX + personagemLargura:
                morte()

        
        pygame.display.update()
        fps.tick(60)

jogo()