import sys
import pygame 
from random import randint
from classes_e_funcoes import *
from funcoes_invaders_3 import *


# def carrega_mapa(nova_pos, offsetx, offsety, proximo_mapa):
#     camera_group.camera_check(offsetx, offsety)
#     proximo_mapa = proximo_mapa
#     contador_mapas = 0
#     nova_pos = nova_pos
#     return proximo_mapa, contador_mapas, nova_pos,

pygame.init()
tela = pygame.display.set_mode((1280,720))
superficie = pygame.display.get_surface()
gamemaps = GameMaps()
gamearea = " "
clock = pygame.time.Clock()
camera_group = CameraGroup()
player = Player((1035, 2120), camera_group)

#variaveis

contador_mapas = 0
mapa_definido = False
contador_terra2 = 0

delay_empurrar = 0
andado = 0
delay_trocar = 15
contador_verde = 0
venceu_cogu = False
esta_no_gelo = True


#variaveis Coletou emas
ColetouLuz = False
ColetouTerra = False
ColetouFogo = False
ColetouAgua = False
ColetouAr = False

#variaveis para colisao
contador_momento_colisao = 0
checkposx = "right"
checkposy = "up"
incapacitada = " "
checkpos = " "
x_antigo, y_antigo = 0, 0
colidindo = False
indice = 0
ult_checkpos = " "


#variaveis para carregar sprites
sprites_aguapuzzle = False
sprites_cogumelos = False
interagiu = 0
colisao = False
GemaFogo = False
GemaTerra = False
GemaLuz = False
GemaAgua = False
GemaAr = False
textbox_surgiu = False
gelo = False

#variaveis que verifica a coleta de paginas
p1 = False
p2 = False
p3 = False
p4 = False
p5 = False
p6 = False
p7 = False
p8 = False
p9 = False
p10 = False
p11 = False
p12 = False
p13 = False 


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ####################       ####################
    #################### LOBBY ####################
    ####################       ####################

    if gamemaps.map == "lobby":

        if ColetouLuz == False:
            camera_group.fade(1280, 720, 230)
        else:
            camera_group.fade(1280, 720, 10)

        if colisao == False:
            if ColetouAgua == False:
                colisao_lobby = gamemaps.Colisao_lobby((0,0), camera_group)
            if ColetouAgua == True:
                colisao_lobby.kill()
                colisao_lobby = gamemaps.Colisao_lobby_Sem_Agua((0,0), camera_group)
            colisao = True


        contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.lobby.limites, gamemaps.lobby.mapa, colisao_lobby, camera_group, colidindo, incapacitada)
        checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_lobby, indice, checkpos)

        #Carrega Luz    
        if player.rect.collidepoint(130, 1815):
            gamearea = "luz"
            gamemaps.map = "luz1"
            colisao, contador_mapas = troca_mapa(colisao_lobby, camera_group, 0, 0, 1032, 414, player)


        #Carrega Fogo
        elif player.rect.collidepoint(2330, 1820):
            colisao, contador_mapas = troca_mapa(colisao_lobby, camera_group, 25, 9425, 335, 9760, player)
            gamearea = "fogo"
            gamemaps.map = "fogo1"
        
        #carrega agua
        elif player.rect.collidepoint(1105, 175):
            colisao, contador_mapas = troca_mapa(colisao_lobby, camera_group, 203, 1004, 841, 1462, player)
            gamearea = "agua"
            gamemaps.map = "agua1"

        #carrega ar
        elif player.rect.collidepoint(250,360):
            colisao, contador_mapas = troca_mapa(colisao_lobby, camera_group, 0, 220, 840, 740, player)
            gamearea = "ar"
            gamemaps.map = "ar1"
        
        #carrega terra
        elif player.rect.collidepoint(2325, 675):
            colisao, contador_mapas = troca_mapa(colisao_lobby, camera_group, 0, 0, 200, 870, player)
            gamearea = "terra"
            gamemaps.map = "terra1"


    ####################          ####################
    #################### AREA LUZ ####################
    ####################          ####################

    if gamearea == "luz":

        #################### MAPA LUZ1 ####################
        if gamemaps.map == "luz1":

            if ColetouLuz == False:
                camera_group.fade(1280, 720, 215)
            else:
                camera_group.fade(1280, 720, 10)

            if colisao == False:
                colisao_luz1 = gamemaps.Colisao_luz1((0,0), camera_group)
                if p1 == False:
                    pagina1 = Pagina((112, 464), camera_group, 1)
                    textbox1 = Textbox( (-1000,- 1000), 0)
                colisao = True
        
            p1 = pagina1.interact(player, camera_group.hud_surf, p1)
            textbox_surgiu = textbox1.surgir(camera_group.hud_surf, textbox_surgiu)

            contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.luz1.limites, gamemaps.luz1.mapa, colisao_lobby, camera_group, colidindo, incapacitada)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_luz1, indice, checkpos)

                
            #luz1 para luz 2
            if player.rect.collidepoint(782, 44):
                gamemaps.map = "luz2"
                colisao, contador_mapas = troca_mapa(colisao_luz1, camera_group, 637, 880, 1315, 1450, player)
                pagina1.kill()

            #luz1 para luzup
            elif player.rect.collidepoint(527, 429):
                contador_check = camera_group.camera_check(2115, 40)
                gamemaps.map = "luzup"
                contador_mapas = 0
                
                player.rect.centerx = 3020
                player.rect.centery = 490
       
            #luz 1 para lobby
            elif player.rect.collidepoint(1107, 414):
                gamearea = "lobby"
                gamemaps.map = "lobby"
                colisao, contador_mapas = troca_mapa(colisao_luz1, camera_group, 15, 1000, 200, 1815, player)
                pagina1.kill()
                

        #################### MAPA LUZ2 ####################      
        elif gamemaps.map == "luz2":

            if ColetouLuz == False:
                camera_group.fade(1280, 720, 200)
            else:
                camera_group.fade(1280, 720, 10)

            if colisao == False:
                colisao_luz2 = gamemaps.Colisao_luz2((0,0), camera_group)
                if p2 == False:
                    pagina2 = Pagina((390, 1350), camera_group, 0)
                colisao = True

            contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.luz2.limites, gamemaps.luz2.mapa, colisao_luz2, camera_group, colidindo, incapacitada)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_luz2, indice, checkpos)

            p2 = pagina2.interact(player, camera_group.hud_surf, p2)

            #luz2 para luz3
            if player.rect.collidepoint(130, 355):
                colisao, contador_mapas = troca_mapa(colisao_luz2, camera_group, -5, 35, 775, 105, player)
                gamemaps.map = "luz3"
                pagina2.kill()

            #luz 2 para luz 1
            elif player.rect.collidepoint(1325, 1550):
                gamemaps.map = "luz1"
                colisao, contador_mapas = troca_mapa(colisao_luz2, camera_group, 5, 15, 782, 114, player)
                pagina2.kill()



        #################### MAPA LUZ UP ####################
        elif gamemaps.map == "luzup":
            contador_mapas = camera_group.custom_draw(tela, player, gamemaps.luzup.limites, gamemaps.luzup.mapa, contador_mapas)
            camera_group.update(incapacitada)
            pygame.display.update()

            #luz up para luz 1
            if player.rect.collidepoint(3020, 415):
                contador_check = camera_group.camera_check(5, 140)
                gamemaps.map = "luz1"
                
                contador_mapas = 0
                player.rect.centerx = 582
                player.rect.centery = 429
            
            #luz up para luz puzzle
            elif player.rect.collidepoint(400, 790):
                camera_group.camera_check(0, 0)
                gamemaps.map = "luzpuzzle"
                contador_mapas = 0
                player.rect.centerx = 0
                player.rect.centery = 0


        #################### MAPA LUZ 3 ####################
        elif gamemaps.map == "luz3":

            if ColetouLuz == False:
                camera_group.fade(1280, 720, 185)
            else:
                camera_group.fade(1280, 720, 10)

            if colisao == False:
                colisao_luz3 = gamemaps.Colisao_luz3((0,0), camera_group)
                if p3 == False:
                    pagina3 = Pagina((230, 605), camera_group, 0)
                colisao = True

            contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.luz3.limites, gamemaps.luz3.mapa, colisao_luz3, camera_group, colidindo, incapacitada)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_luz3, indice, checkpos)

            p3 = pagina3.interact(player, camera_group.hud_surf, p3)

            #luz3 para luzpuzzle
            if player.rect.collidepoint(780, 1130):
                colisao, contador_mapas = troca_mapa(colisao_luz3, camera_group, 0, 0, 655, 105, player)
                gamemaps.map = "luzpuzzle"

            #luz3 para luz2    
            elif player.rect.collidepoint(850, 105):
                colisao, contador_mapas = troca_mapa(colisao_luz3, camera_group, 10, 15, 180, 355, player)
                gamemaps.map = "luz2"


        #################### MAPA LUZ PUZZLE ####################
        elif gamemaps.map == "luzpuzzle":

            if ColetouLuz == False:
                camera_group.fade(1280, 720, 150)
            else:
                camera_group.fade(1280, 720, 10)

            if colisao == False:
                colisao_luzpuzzle = gamemaps.Colisao_luzpuzzle((0,0), camera_group)
                colisao = True

            contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.luzpuzzle.limites, gamemaps.luzpuzzle.mapa, colisao_luzpuzzle, camera_group, colidindo, incapacitada)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_luzpuzzle, indice, checkpos)

            
            if sprites_cogumelos == False:
                sprites_cogumelos = True
                cogumelo1a =  Cogumelo((440, 700), camera_group, "vermelho")
                cogumelo1b =  Cogumelo((640, 700), camera_group, "verde")
                cogumelo1c =  Cogumelo((840, 700), camera_group, "vermelho")
                cogumelo2a =  Cogumelo((440, 900), camera_group, "vermelho")
                cogumelo2b =  Cogumelo((640, 900), camera_group, "vermelho")
                cogumelo2c =  Cogumelo((840, 900), camera_group, "verde")
                cogumelo3a =  Cogumelo((440, 1100), camera_group, "verde")
                cogumelo3b =  Cogumelo((640, 1100), camera_group, "verde")
                cogumelo3c =  Cogumelo((840, 1100), camera_group, "vermelho")

            grupos_cogumelos = [[cogumelo1a, cogumelo1b, cogumelo2a], [cogumelo1b, cogumelo1a, cogumelo1c, cogumelo2b], 
            [cogumelo1c, cogumelo1b, cogumelo2c], [cogumelo2a, cogumelo1a, cogumelo2b, cogumelo3a], [cogumelo2b, cogumelo1b, cogumelo2a, cogumelo2c, cogumelo3b]
            , [cogumelo2c, cogumelo1c, cogumelo2b, cogumelo3c], [cogumelo3a, cogumelo2a, cogumelo3b], [cogumelo3b, cogumelo2b, cogumelo3a, cogumelo3c], 
            [cogumelo3c, cogumelo2c, cogumelo3b]]

            cogumelos = [cogumelo1a, cogumelo1b, cogumelo1c, cogumelo2a, cogumelo2b, cogumelo2c, cogumelo3a, cogumelo3b, cogumelo3c]

            if venceu_cogu == False:
                for i in range(len(grupos_cogumelos)):
                    for j in range(len(grupos_cogumelos[i])):
                        if player.rect.colliderect(grupos_cogumelos[i][0]) and player.interact() and delay_trocar > 20:
                            Cogumelo.trocar(grupos_cogumelos[i])
                            contador_verde, venceu_cogu = Cogumelo.check_cores(cogumelos, contador_verde, venceu_cogu)
                            delay_trocar = 0

                contador_verde = 0
                delay_trocar += 1

            elif venceu_cogu == True:

                if ColetouLuz == False:
                    camera_group.fade(1280, 720, 150)
                else:
                    camera_group.fade(1280, 720, 10)

                contador_mapas = 0
                cogumelo3b.kill() 
                cogumelos.remove(cogumelo3b)
                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.luzpuzzle.limites, gamemaps.luzpuzzle.mapa2, colisao_luzpuzzle, camera_group, colidindo, incapacitada)
                checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_luzpuzzle, indice, checkpos)
                gamemaps.map == "luzpuzzle2"

                #luz puzzle 2 para luzgema
                if player.rect.collidepoint(650, 1165):
                    colisao, contador_mapas = troca_mapa(colisao_luzpuzzle, camera_group, 15, 20, 655, 125, player)
                    gamemaps.map = "luzgema"

                    sprites_cogumelos == False
                    for cogumelo in cogumelos:
                        cogumelo.kill()

            #luz puzzle para luz 3
            if player.rect.collidepoint(650, 50):
                colisao, contador_mapas = troca_mapa(colisao_luzpuzzle, camera_group, 0, 555, 655, 125, player)
                gamemaps.map = "luz3"

                sprites_cogumelos == False
                for cogumelo in cogumelos:
                    cogumelo.kill()


        #################### MAPA LUZ GEMA ####################
        elif gamemaps.map == "luzgema":

            if ColetouLuz == False:
                camera_group.fade(1280, 720, 130)
            else:
                camera_group.fade(1280, 720, 10)

            if colisao == False:
                colisao_luzgema = gamemaps.Colisao_luzgema((0,0), camera_group)
                colisao = True

            if GemaLuz == False:
                GemaLuz = True
                gema_luz = Gema((635,470), camera_group, gamemaps.luzgema.gema)
            if player.rect.colliderect(gema_luz):
                # camera_group.fade_out(1280, 720)
                ColetouLuz = True
                gema_luz.kill()

            contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.luzgema.limites, gamemaps.luzgema.mapa, colisao_luzgema, camera_group, colidindo, incapacitada)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_luzgema, indice, checkpos)

            

    ####################           ####################
    #################### ÁREA FOGO ####################
    ####################           ####################

    elif gamearea == "fogo":


        #################### MAPA FOGO 1 ####################
        if gamemaps.map == "fogo1":
            if colisao == False:
                colisao_fogo1 = gamemaps.Colisao_fogo1((0,0), camera_group)
                pagina4 = Pagina((1880, 8520), camera_group, 0)
                pagina5 = Pagina((230, 645), camera_group, 0)
                pagina6 = Pagina((230, 645), camera_group, 0)
                pagina7 = Pagina((230, 645), camera_group, 0)
                colisao = True

            colidindo = player.anula_colisao(colidindo)
            contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.fogo1.limites, gamemaps.fogo1.mapa, colisao_fogo1, camera_group, colidindo, incapacitada)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_fogo1, indice, checkpos)

            #pagina2.interact(player, camera_group.hud_surf)
            
            #fogo1 para fogo2
            if player.rect.collidepoint(14155, 170):
                colisao, contador_mapas = troca_mapa(colisao_fogo1, camera_group, 15, 235, 655, 710, player)
                gamemaps.map = "fogo2"

            #fogo1 para lobby
            elif player.rect.collidepoint(265, 9760):
                colisao, contador_mapas = troca_mapa(colisao_fogo1, camera_group, 1205, 1460, 2260, 1820, player)
                gamearea = "lobby"
                gamemaps.map = "lobby"

        #################### MAPA FOGO 2 ####################   
        if gamemaps.map == "fogo2":
            if colisao == False:
                colisao_fogo2 = gamemaps.Colisao_fogo2((0,0), camera_group)
                colisao = True

            if GemaFogo == False:
                GemaFogo = True
                gema_fogo = Gema((662,459), camera_group, gamemaps.fogo2.gema)
            if player.rect.colliderect(gema_fogo.rect):
                ColetouFogo = True
                gema_fogo.kill()

            contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.fogo2.limites, gamemaps.fogo2.mapa, colisao_fogo2, camera_group, colidindo, incapacitada)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_fogo2, indice, checkpos)

            #fogo 2 para fogo 1
            if player.rect.collidepoint(650, 770):
                colisao, contador_mapas = troca_mapa(colisao_fogo2, camera_group, 13515, 80, 14155, 225, player)
                gamemaps.map = "fogo1"



    ####################            ####################
    #################### ÁREA AGUA ####################
    ####################            ####################

    elif gamearea == "agua":


        #################### MAPA AGUA 1 ####################   
        if gamemaps.map == "agua1":
            if colisao == False:
                colisao_agua1 = gamemaps.Colisao_agua1((0,0), camera_group)
                colisao = True

            contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player,  gamemaps.agua1.limites, gamemaps.agua1.mapa, colisao_agua1, camera_group, colidindo, incapacitada)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_agua1, indice, checkpos)

            #agua 1 para agua 2
            if player.rect.collidepoint(1281, 897):
                colisao, contador_mapas = troca_mapa(colisao_agua1, camera_group, 1045, 460, 1685, 820, player)
                gamemaps.map = "agua2"
            elif player.rect.collidepoint(411, 907):
                colisao, contador_mapas = troca_mapa(colisao_agua1, camera_group, 0, 460, 640, 820, player)
                gamemaps.map = "agua2"
            
            #agua 1 para lobby
            elif player.rect.collidepoint(841, 1552):
                colisao, contador_mapas = troca_mapa(colisao_agua1, camera_group, 465, 15, 1100, 230, player)
                gamearea = "lobby"
                gamemaps.map = "lobby"


        #################### MAPA AGUA 2 ####################  
        elif gamemaps.map == "agua2":
            if colisao == False:
                colisao_agua2 = gamemaps.Colisao_agua2((0,0), camera_group)
                colisao = True

            contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.agua2.limites, gamemaps.agua2.mapa, colisao_agua2, camera_group, colidindo, incapacitada)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_agua2, indice, checkpos)

            #agua 2 para agua 3a
            if player.rect.collidepoint(260, 350):
                colisao, contador_mapas = troca_mapa(colisao_agua2, camera_group, 55, 1200, 970, 1630, player)
                gamemaps.map = "agua3a"

            #agua 2 para agua 3b
            elif player.rect.collidepoint(2070, 350):
                colisao, contador_mapas = troca_mapa(colisao_agua2, camera_group, 10, 1200, 330, 1630, player)
                gamemaps.map = "agua3b"

            #agua 2 para agua 1
            elif player.rect.collidepoint(1615, 815):
                colisao, contador_mapas = troca_mapa(colisao_agua2, camera_group, 425, 545, 1195, 895, player)
                gamemaps.map = "agua1"
            
            elif player.rect.collidepoint(715, 815):
                colisao, contador_mapas = troca_mapa(colisao_agua2, camera_group, 10, 535, 480, 895, player)
                gamemaps.map = "agua1"

        
        #################### MAPA AGUA 3A ####################
        elif gamemaps.map == "agua3a":
            if colisao == False:
                colisao_agua3a = gamemaps.Colisao_agua3a((0,0), camera_group)
                colisao = True

            contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.agua3a.limites, gamemaps.agua3a.mapa, colisao_agua3a, camera_group, colidindo, incapacitada)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_agua3a, indice, checkpos)

            #agua 3a para agua puzzle
            if player.rect.collidepoint(525, 105):
                colisao, contador_mapas = troca_mapa(colisao_agua3a, camera_group, 0, 880, 205, 1315, player)
                gamemaps.map = "aguapuzzle"
            
            #agua 3a para agua 2
            elif player.rect.collidepoint(1050, 1630):
                colisao, contador_mapas = troca_mapa(colisao_agua3a, camera_group, 0, 0, 325, 355, player)
                gamemaps.map = "agua2"
                

        #################### MAPA AGUA 3B ####################
        elif gamemaps.map == "agua3b":
            if colisao == False:
                colisao_agua3b = gamemaps.Colisao_agua3b((0,0), camera_group)
                colisao = True

            contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.agua3b.limites, gamemaps.agua3b.mapa, colisao_agua3b, camera_group, colidindo, incapacitada)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_agua3b, indice, checkpos)
        
            #agua 3b para agua puzzle
            if player.rect.collidepoint(525, 105):
                colisao, contador_mapas = troca_mapa(colisao_agua3b, camera_group, 1075, 0, 1995, 350, player)
                gamemaps.map = "aguapuzzle"

            #agua 3b para agua 2
            elif player.rect.collidepoint(240, 1620):
                colisao, contador_mapas = troca_mapa(colisao_agua3b, camera_group, 1075, 0, 1995, 350, player)
                gamemaps.map = "agua2"
            

        #################### MAPA AGUA PUZZLE ####################
        elif gamemaps.map == "aguapuzzle":

            if colisao == False:
                colisao_aguapuzzle = gamemaps.Colisao_aguapuzzle((0,0), camera_group)
                colisao = True

            contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.aguapuzzle.limites, gamemaps.aguapuzzle.mapa, colisao_aguapuzzle, camera_group, colidindo, incapacitada)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_aguapuzzle, indice, checkpos)
            
            if sprites_aguapuzzle == False:
                pedra1a = Pedra((1237, 902), camera_group)
                pedra1b = Pedra((1292, 902), camera_group)
                pedra1c = Pedra((1347, 902), camera_group)
                pedra2a = Pedra((1182, 856), camera_group)
                pedra2b = Pedra((1402, 856), camera_group)
                pedra3a = Pedra((1237, 810), camera_group)
                pedra3b = Pedra((1292, 810), camera_group)
                pedra3c = Pedra((1347, 810), camera_group)
                pedra4a = Pedra((1182, 764), camera_group)
                pedra4b = Pedra((1237, 764), camera_group)
                pedra4c = Pedra((1347, 764), camera_group)
                pedra4d = Pedra((1402, 764), camera_group)
                sprites_aguapuzzle = True

            pedras = [pedra1a, pedra1b, pedra1c, pedra2a, pedra2b, pedra3a, pedra3b, pedra3c, pedra4a, pedra4b, pedra4c, pedra4d]

            ult_checkpos = Player.ultimo_checkpos(checkposx, checkposy, ult_checkpos)
            

            for pedra in pedras:
                offsetx = pedra.rect.centerx - player.rect.centerx
                offsety = pedra.rect.centery - player.rect.centery

                # if ult_checkpos != "up":
                #     if player.mask.overlap_area(pedra.mask, (offsetx, offsety)) > 200:
                #         colidindo = True
                #         x_antigo, y_antigo = player.ultima_pos(colidindo, x_antigo, y_antigo)
                #         if player.mask.overlap_area(pedra.mask, (offsetx, offsety)) > 100:
                #             player.rect.centerx = posx_backup_puzzle_agua
                #             player.rect.centery = posy_backup_puzzle_agua
                #     if player.mask.overlap_area(pedra.mask, (offsetx, offsety)) > 50:
                #         if delay_empurrar > 20:
                #             delay_empurrar = pedra.movimento(ult_checkpos, delay_empurrar)

                # elif ult_checkpos == "up":
                #     if player.mask.overlap_area(pedra.mask, (offsetx, offsety)) > 93:
                #         posx_backup_puzzle_agua = player.rect.centerx
                #         posy_backup_puzzle_agua = player.rect.centery
                #     if player.mask.overlap_area(pedra.mask, (offsetx, offsety)) > 200:
                #         colidindo = True
                #         x_antigo, y_antigo = player.ultima_pos(colidindo, x_antigo, y_antigo)
                #     if player.mask.overlap_area(pedra.mask, (offsetx, offsety)) > 50:
                #         if delay_empurrar > 20:
                #             delay_empurrar = pedra.movimento(ult_checkpos, delay_empurrar)


                if player.mask.overlap_area(pedra.mask, (offsetx, offsety)) > 250:
                        colidindo = True
                        x_antigo, y_antigo = player.ultima_pos(colidindo, x_antigo, y_antigo)
                        print("colidindo")
                if player.mask.overlap_area(pedra.mask, (offsetx, offsety)) > 0:
                    print("quase colidindo")
                    if delay_empurrar > 20:
                         delay_empurrar = pedra.movimento(ult_checkpos, delay_empurrar)
                
            delay_empurrar += 1   


            # if player.rect.collidepoint(115, 1305):
            #     camera_group.camera_check(0, 0)
            #     gamemaps.map = "agua3a"
            #     contador_mapas = 0
            #     player.rect.centerx = 525
            #     player.rect.centery = 170
            #     for i in range(len(pedras)):
            #         pedras[i].kill()
            #     sprites_aguapuzzle = False



    ####################          ####################
    #################### ÁREA AR  ####################
    ####################          ####################

    elif gamearea == "ar":
        
    
    #################### MAPA AR 1 ####################

        if gamemaps.map == "ar1":
            if colisao == False:
                colisao_ar1 = gamemaps.Colisao_ar1((0,0), camera_group)
                colisao = True

            contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.ar1.limites, gamemaps.ar1.mapa, colisao_ar1, camera_group, colidindo, incapacitada)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_ar1, indice, checkpos)
            
            #ar 1 para ar2
            if player.rect.collidepoint(330, 155):
                colisao, contador_mapas = troca_mapa(colisao_ar1, camera_group, 0, 560, 580, 1135, player)
                gamemaps.map = "ar2"
            
            #ar 1 para lobby
            if player.rect.collidepoint(925, 735):
                colisao, contador_mapas = troca_mapa(colisao_ar1, camera_group, 0, 15, 335, 365, player)
                gamearea = "lobby"
                gamemaps.map = "lobby"
            
     #################### MAPA AR 2 ####################
                
        elif gamemaps.map == "ar2":

            if colisao == False:
                colisao_ar2 = gamemaps.Colisao_ar2((0,0), camera_group)
                colisao = True

            contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.ar2.limites, gamemaps.ar2.mapa, colisao_ar2, camera_group, colidindo, incapacitada)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_ar2, indice, checkpos)

            #ar 2 para ar puzzle
            if player.rect.collidepoint(525, 30):
                colisao, contador_mapas = troca_mapa(colisao_ar2, camera_group, 230, 805, 875, 1290, player)
                gamemaps.map = "arpuzzle"

            #ar 2 para ar 1
            if player.rect.collidepoint(650, 1110):
                colisao, contador_mapas = troca_mapa(colisao_ar2, camera_group, 0, 15, 330, 245, player)
                gamemaps.map = "ar1"




    #################### MAPA AR PUZZLE ####################
                
        elif gamemaps.map == "arpuzzle":  

            if gelo == False:
                area_gelo = gamemaps.AreaGelo((0,0), camera_group)
                gelo = True

            if colisao == False:
                colisao_arpuzzle = gamemaps.Colisao_arpuzzle((0,0), camera_group)
                colisao = True
            

            contador_mapas, colidindo, esta_no_gelo = carrega_mapa_com_gelo(contador_mapas, tela, player, gamemaps.arpuzzle.limites, gamemaps.arpuzzle.mapa, colisao_arpuzzle, camera_group, colidindo, incapacitada, esta_no_gelo, area_gelo)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos, ult_checkpos, esta_no_gelo = player.update_no_gelo(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_arpuzzle, indice, checkpos, ult_checkpos, esta_no_gelo, area_gelo)

            ult_checkpos = Player.ultimo_checkpos(checkposx, checkposy, ult_checkpos)
        
            # print(ult_checkpos)
            #ar puzzle para ar gema
            if player.rect.collidepoint(1285, 175):
                colisao, contador_mapas = troca_mapa(colisao_arpuzzle, camera_group, 10, 245, 650, 780, player)
                gamemaps.map = "argema"
                area_gelo.kill()
                

            #ar puzzle para ar 2
            if player.rect.collidepoint(870, 1370):
                colisao, contador_mapas = troca_mapa(colisao_arpuzzle, camera_group, 0, 15, 530, 105, player)
                gamemaps.map = "ar2"


    #################### MAPA AR GEMA ####################
        elif gamemaps.map == "argema":
            if colisao == False:
                colisao_argema = gamemaps.Colisao_argema((0,0), camera_group)
                colisao = True

            if GemaAr == False:
                GemaAr = True
                gema_ar = Gema((662,459), camera_group, gamemaps.argema.gema)
            if player.rect.colliderect(gema_ar.rect):
                ColetouAr = True
                gema_ar.kill()

            contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.argema.limites, gamemaps.argema.mapa, colisao_argema, camera_group, colidindo, incapacitada)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_argema, indice, checkpos)
            

            

    ####################            ####################
    #################### ÁREA TERRA ####################
    ####################            ####################

    elif gamearea == "terra":

    #################### MAPA TERRA1 ####################

        if gamemaps.map == "terra1":
            if colisao == False:
                colisao_terra1 = gamemaps.Colisao_terra1((0,0), camera_group)
                colisao = True

            contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.terra1.limites, gamemaps.terra1.mapa, colisao_terra1, camera_group, colidindo, incapacitada)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_terra1, indice, checkpos)

            #terra 1 para cima
            if player.rect.collidepoint(975, 45):
                colisao, contador_mapas = troca_mapa(colisao_terra1, camera_group, 330, 1185, 976, 1646, player)
                gamemaps.map = "terra2"
                saida = "baixo"

            #terra 1 para direita
            elif player.rect.collidepoint(1805, 865):
                colisao, contador_mapas = troca_mapa(colisao_terra1, camera_group, 0, 515, 196, 866, player)
                gamemaps.map = "terra2"
                saida = "esquerda"
            
            #terra 1 para baixo
            elif player.rect.collidepoint(975, 1740):
                colisao, contador_mapas = troca_mapa(colisao_terra1, camera_group, 335, 5, 971, 106, player)
                gamemaps.map = "terra2"
                saida = "cima"

            #terra 1 para esquerda
            elif player.rect.collidepoint(135, 865):
                colisao, contador_mapas = troca_mapa(colisao_terra1, camera_group, 1195, 320, 2255, 680, player)
                gamemaps.map = "lobby"
                saida = "esquerda"
            
    #################### MAPA TERRA2 ####################

        elif gamemaps.map == "terra2":

            if mapa_definido == False:
                i = randint(0,9)
                mapa_terra = gamemaps.terra2.mapa[i]
                mapa_parede_terra =  gamemaps.terra2.mapa_colisao[i]
                mapa_definido = True

            if colisao == False:
                colisao_terra2 = gamemaps.Colisao_terra2((0,0), camera_group, mapa_parede_terra)
                colisao = True

            contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.terra2.limites, mapa_terra, colisao_terra2, camera_group, colidindo, incapacitada)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_terra2, indice, checkpos)

            #terra 2 para cima
            if player.rect.collidepoint(975, 45):
                if saida != "cima":
                    colisao, contador_mapas = troca_mapa(colisao_terra2, camera_group, 330, 1185, 976, 1646, player)
                    gamemaps.map = "terra2"
                    saida = "baixo"
                    mapa_definido = False
                    contador_terra2 += 1
                    if contador_terra2 >= 7:

                        carrega_gema_terra = jogo()
                        contador_terra2 = 0
                        colisao, contador_mapas = troca_mapa(colisao_terra2, camera_group, 12, 192, 648, 729, player)

                        gamemaps.map = "terragema"

                    elif randint(contador_terra2 - 3, 7) == 7:

                        carrega_gema_terra = jogo()
                        contador_terra2 = 0
                        colisao, contador_mapas = troca_mapa(colisao_terra2, camera_group, 12, 192, 648, 729, player)

                        gamemaps.map = "terragema"

                elif saida == "cima":
                    gamemaps.map = "terra1"
                    contador_terra2 = 0
                    mapa_definido = False
                    saida = " "
                    colisao, contador_mapas = troca_mapa(colisao_terra2, camera_group, 330, 1190, 970, 1635, player)


            #terra 2 para direita
            elif player.rect.collidepoint(1805, 865):
                if saida != "direita":
                    colisao, contador_mapas = troca_mapa(colisao_terra2, camera_group, 0, 515, 196, 866, player)
                    gamemaps.map = "terra2"
                    saida = "esquerda"
                    mapa_definido = False
                    contador_terra2 += 1

                elif saida == "direita":
                    gamemaps.map = "terra1"
                    contador_terra2 = 0
                    mapa_definido = False
                    saida = " "
                    colisao, contador_mapas = troca_mapa(colisao_terra2, camera_group, -5, 520, 215, 880, player)

            
            #terra 2 para baixo
            elif player.rect.collidepoint(975, 1740):
                if saida != "baixo":
                    colisao, contador_mapas = troca_mapa(colisao_terra2, camera_group, 335, 5, 971, 106, player)
                    gamemaps.map = "terra2"
                    saida = "cima"
                    mapa_definido = False
                    contador_terra2 += 1

                elif saida == "baixo":
                    gamemaps.map = "terra1"
                    contador_terra2 = 0
                    mapa_definido = False
                    saida = " "
                    colisao, contador_mapas = troca_mapa(colisao_terra2, camera_group, 330, 5, 970, 130, player)
                
            #terra 2 para esquerda
            elif player.rect.collidepoint(107, 856):
                if saida != "esquerda":
                    colisao, contador_mapas = troca_mapa(colisao_terra2, camera_group, 686, 496, 1731, 856, player)
                    gamemaps.map = "terra2"
                    saida = "direita"
                    mapa_definido = False
                    contador_terra2 += 1

                elif saida == "esquerda":
                    gamemaps.map = "terra1"
                    contador_terra2 = 0
                    mapa_definido = False
                    saida = " "
                    colisao, contador_mapas = troca_mapa(colisao_terra2, camera_group, 690, 510, 1735, 870, player)

        #################### MAPA TERRA2 ####################

        elif gamemaps.map == "terragema":

            if colisao == False:
                colisao_terragema = gamemaps.Colisao_terragema((0,0), camera_group)
                colisao = True

            if GemaTerra == False:
                GemaTerra = True
                gema_terra = Gema((662,459), camera_group, gamemaps.terragema.gema)

            if player.rect.colliderect(gema_terra.rect):
                ColetouTerra = True
                gema_terra.kill()

            contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.terragema.limites, gamemaps.terragema.mapa, colisao_terragema, camera_group, colidindo, incapacitada)
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_terragema, indice, checkpos)

    #print(clock)
    # print(player.rect.centerx, player.rect.centery, "###", player.rect.x, player.rect.y, "###", camera_group.offset.x, camera_group.offset.y, gamemaps.map)
    #clock.tick(60)
    print(ColetouLuz)