import pygame
import random

largura = 800
altura = 600
display = pygame.display.set_mode((largura, altura))
preto = (0, 0, 0)

def textos(texto, fonte, cor):
    textSurface = fonte.render(texto, True, cor)
    return textSurface, textSurface.get_rect()

def pontuacao(escrita, pontos, cor, x, y):
    font = pygame.font.Font("assets/fonte.ttf", 25)
    texto = font.render(escrita + str(pontos), True, cor)
    display.blit(texto, (x, y))
    pygame.display.update()

def criaLog(nome, email):
    arquivo = open("log.txt", "w")
    arquivo.write("Nome: ")
    arquivo.write(nome)
    arquivo.write("\nEmail: ")
    arquivo.write(email)