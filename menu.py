from pygame import mixer
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.animation import *
from main import *


#musica do menu
p_musica = True
mixer.init()
mixer.music.load("assets_menu\menu.wav")
mixer.music.set_volume(0.5)
mixer.music.play(-1)

#dimensões
janela_largura = 1280
janela_altura = 720

#criando a janela
janelamenu = Window(janela_largura, janela_altura)
janelamenu.set_title("Crypto")

#pegando a entrada do usuário
teclado = janelamenu.get_keyboard()
click = janelamenu.get_mouse()

#fundo do menu
background = Sprite("assets_menu\Fundo.png")

#botao play
play = Sprite("assets_menu\playgab.png")
play.set_position(1280/2 - 120, 250)

fogueira = Sprite("assets_menu\Fogueira.png" , 10)
fogueira.set_total_duration(1000)
fogueira.set_position(600 - fogueira.width/2 , 470)

calefia = Sprite("assets_menu\calefianomenu.png")
calefia.set_position(705 - fogueira.width/2 , 445)

#botao exit
exit = Sprite("assets_menu\Botaoback.png")
exit.set_position(1280/2 - 120 , 350)


#########################################################################################################################################
############################################################ GAMELOOP ###################################################################
#########################################################################################################################################

while True:
    background.draw()
    play.draw()
    exit.draw()
    fogueira.update()
    fogueira.draw()
    calefia.draw()
    
    #botao play
    if click.is_over_object(play) and click.is_button_pressed(True):
        mixer.music.stop()
        jogo()
        
    #botao exit
    if click.is_over_object(exit) and click.is_button_pressed(True):
        janelamenu.close()

    janelamenu.update()