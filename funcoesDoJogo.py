from JogoEducacional import jogo

import pygame
import time

largura = 800
altura = 600
display = pygame.display.set_mode((largura, altura))
preto = (0, 0, 0)

def textos(texto, fonte):
    textSurface = fonte.render(texto, True, preto)
    return textSurface, textSurface.get_rect()

def mensagensNoDisplay(text):
    fonte = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = textos(text, fonte)
    TextRect.center = ((largura / 2), (altura / 2))
    display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    jogo()

def morte():
    mensagensNoDisplay("Você Morreu!")          