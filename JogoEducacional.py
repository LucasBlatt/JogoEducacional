from funcoesDoJogo import textos, pontuacao, criaLog
import pygame
import random
import time
import os

pygame.init()

somDosPontos = pygame.mixer.Sound("assets/pontos.wav")
icone = pygame.image.load("assets/icone.png")
pygame.display.set_caption("Junk Food Runner")
pygame.display.set_icon(icone)
largura = 800
altura = 600
display = pygame.display.set_mode((largura, altura))
fps = pygame.time.Clock()
fundo = pygame.image.load("assets/fundo.png")
personagem = pygame.image.load("assets/personagem.png")
porcarias = [pygame.image.load("assets/porcaria_1.png"), pygame.image.load("assets/porcaria_2.png"), pygame.image.load("assets/porcaria_3.png"), pygame.image.load("assets/porcaria_4.png"), pygame.image.load("assets/porcaria_5.png")]
porcariasRandom = random.choice(porcarias)
branco = (255, 255, 255)
preto = (0, 0, 0)

def mensagensNoDisplay(text):
    fonte = pygame.font.Font("assets/fonte.ttf", 40)
    TextSurf, TextRect = textos(text, fonte, preto)
    TextRect.center = ((largura / 2), ((altura / 2) - 20))
    display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    jogo()

def morte(pontos):
    pygame.mixer.music.load("assets/morreu.wav")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()
    mensagensNoDisplay("GAME OVER! Você tinha:" + str(pontos) +" Ponto(s)")  

def jogo():
    pygame.mixer.music.load("assets/fundo.wav")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    
    personagemPosicaoX = 380
    personagemPosicaoY = 405
    personagemLargura = 110
    movimentoX = 0
    porcariasPosicaoX = 380
    porcariasPosicaoY = -220
    porcariasLargura = 1
    porcariasAltura = 1
    porcariasVelocidade = 5
    pontos = 0

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
            pygame.mixer.Sound.play(somDosPontos)
            porcariasPosicaoY = -220
            porcariasVelocidade += 1
            porcariasPosicaoX = random.randrange(0,largura - 50)
            pontos += 1

        if personagemPosicaoY < porcariasPosicaoY + porcariasAltura:
            if personagemPosicaoX < porcariasPosicaoX and personagemPosicaoX + personagemLargura > porcariasPosicaoX or porcariasPosicaoX + porcariasLargura > personagemPosicaoX and porcariasPosicaoX + porcariasLargura < personagemPosicaoX + personagemLargura:
                morte(pontos)

        pontuacao(pontos, branco)
        pygame.display.update()
        fps.tick(60)
        
os.system("cls")

'''while True:
    nome = input("Insira seu nome: ")
    email = input("Insira seu email: ") 
    if not nome or not email: 
        print("Não deixe os campos em branco!")  
    else:
        break    
    
criaLog(nome, email)'''
jogo()