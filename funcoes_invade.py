from pygame import mixer
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
import pygame
from PPlay.collision import *

from PPlay.sprite import *
from PPlay.collision import *

janela_largura = 1280
janela_altura = 768

def posicao(sprite_atual, sprite_desejado): 
    calefia = sprite_desejado 
    calefia.x = sprite_atual.x
    calefia.y = sprite_atual.y
    return calefia

def walk(janela, teclado, checkpos, calefia, velx, vely, contador_total):

    if contador_total == 0:
        if teclado.key_pressed("UP") and calefia.y >=0 and calefia.y > 21.4:
            calefia.y = calefia.y - (vely * janela.delta_time())
            checkpos = "UP"
    if contador_total == 0:
        if teclado.key_pressed("DOWN") and calefia.y < 645.5:
            calefia.y = calefia.y + (vely * janela.delta_time())
            checkpos = "DOWN"
    if teclado.key_pressed("LEFT") and calefia.x > 310.4:
        calefia.x = calefia.x - (velx * janela.delta_time())
        checkpos = "LEFT"

    if teclado.key_pressed("RIGHT") and calefia.x < 988.3:
        calefia.x = calefia.x + (velx * janela.delta_time())
        checkpos = "RIGHT"

    return checkpos  
