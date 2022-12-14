from math import ceil
import pygame
from pygame import mixer
from PPlay import sprite
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *
from ctypes.wintypes import RGB
from funcoes_invaders_2 import *
import funcoes_invade
from PPlay.collision import *


def jogo():

    #dimensões
    janela3_largura = 1280
    janela3_altura = 768

    bateu = False
    vely = 200
    velx = 200
    vel = 1
    lista = []
    lista2 = []
    contador = 0
    cooldown = 0
    score = 0
    contador_mortes = 21
    contador_total = 63
    jogo = True

    #criando a janela
    janela3 = Window(janela3_largura, janela3_altura)
    janela3.set_title("Space Invaders")

    #pegando a entrada do usuário
    teclado = janela3.get_keyboard()

    #colocando um fundo ao jogo
    fundo_jogo = Sprite("assets\Terra space.png")

    #sprite da nave e tiro
    nave = Sprite("assets\C1.png" ,1)
    nave.set_position(janela3_largura/2 - 30 , 620)

    clock = pygame.time.Clock()

    #Up
    calefia_up = Sprite("assets_game\calefiawalkup.png", 9)
    calefia_up_stop = Sprite("assets_game\calefia_stop_up.png")
    calefia_up.set_position(janela3_largura/2,janela3_altura/2)
    calefia_up_stop.set_position(janela3_largura/2 + 20, 570)
    calefia_up.set_total_duration(1000)

    #Down
    calefia_down = Sprite("assets_game\calefiawalkdown.png", 9)
    calefia_down_stop = Sprite("assets_game\calefia_stop_down.png")
    calefia_down.set_position(janela3_largura/2,janela3_altura/2)
    calefia_down_stop.set_position(janela3_largura/2,janela3_altura/2)
    calefia_down.set_total_duration(1000)

    #Left
    calefia_left = Sprite("assets_game\calefiawalkleft.png" , 9)
    calefia_left_stop = Sprite("assets_game\calefia_stop_left.png")
    calefia_left.set_position(janela3_largura/2,janela3_altura/2)
    calefia_left_stop.set_position(janela3_largura/2,janela3_altura/2)
    calefia_left.set_total_duration(1000)

    #right
    calefia_right = Sprite("assets_game\calefiawalkright.png", 9)
    calefia_right_stop = Sprite("assets_game\calefia_stop_right.png")
    calefia_right.set_position(janela3_largura/2,janela3_altura/2)
    calefia_right_stop.set_position(janela3_largura/2,janela3_altura/2)
    calefia_right.set_total_duration(1000)

    #Controlador de posições 
    calefia = calefia_up_stop
    checkpos = "UP"

    contador = 0
    colide = False

    while True:
        fundo_jogo.draw()
        calefia.draw()
        clock.tick()

        #movimentação do calefia
        
        checkpos = funcoes_invade.walk(janela3, teclado, checkpos, calefia, velx, vely, contador_total) 

        velx = 200
        vely = 200

        if checkpos == "UP":
            if teclado.key_pressed("UP"):
                calefia = funcoes_invade.posicao(calefia,calefia_up)
                calefia.update() 
            else:
                calefia = funcoes_invade.posicao(calefia,calefia_up_stop)
        elif checkpos == "LEFT":
            if teclado.key_pressed("LEFT"):
                calefia = funcoes_invade.posicao(calefia,calefia_left)
                calefia.update()
            else:
                calefia = funcoes_invade.posicao(calefia,calefia_left_stop)
        elif checkpos == "DOWN":
            if teclado.key_pressed("DOWN"):
                calefia = funcoes_invade.posicao(calefia,calefia_down)
                calefia.update()
            else:
                calefia = funcoes_invade.posicao(calefia,calefia_down_stop) 
        elif checkpos == "RIGHT":
            if teclado.key_pressed("RIGHT"):
                calefia = funcoes_invade.posicao(calefia,calefia_right)
                calefia.update()
            else:
                calefia = funcoes_invade.posicao(calefia,calefia_right_stop)

        cooldown, jogo = atirar(calefia, janela3, teclado, vely, lista, cooldown, jogo)

        contador = desenhainimigo(lista2,contador)

        vel, bateu = inimigoandando(lista2, janela3, vel, bateu, calefia)

        score, vel, contador_mortes, contador_total = monstromorre(lista2, lista, score, vel, contador_mortes, contador_total)


        if contador_mortes == 0:
            contador_mortes = 21
            vel += vel
            contador = 0
            if contador_total == 0:
                contador = 1
                jogo = False

        if calefia.rect.collidepoint(665, 86.1):
            carrega_gema_terra = True
            break

        if bateu == True:
            break

        janela3.update()
    return carrega_gema_terra 

            

    