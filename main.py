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


def Crypta():
    pygame.init()
    tela = pygame.display.set_mode((1280,720))
    superficie = pygame.display.get_surface()
    gamemaps = GameMaps()
    gamearea = " "
    # clock = pygame.time.Clock()
    camera_group = CameraGroup()
    player = Player((1000, 2000), camera_group)
    Tempo = 1
    Passado = 0
    Fade = False

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
    click = False
    click1 = False
    click2 = False
    presets = False


    #variaveis Coletou emas 
    ColetouLuz = True
    ColetouFogo = True
    ColetouTerra = True
    ColetouAgua = True
    ColetouAr = True

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
    p9b = False
    p10 = False
    p10b = False
    p11 = False
    p11b = False
    p12 = False
    p13 = False 
    p15 = False


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #################### MAPA FLORESTA ####################

        if gamemaps.map == "floresta":
            
            if presets == False:
                player.rect.x = 585
                player.rect.y = 2000
                camera_group.camera_check(0, 1468)
                presets = True
                
            if colisao == False:
                colisao_floresta = gamemaps.Colisao_floresta((0,0), camera_group)
                if p1 == False:
                    pagina1 = Pagina((959, 324), camera_group, 1)
                if ColetouAr:
                    lapide = Lapide((962,304), camera_group)
                    colisao_floresta_final = gamemaps.Colisao_floresta_final((0,0), camera_group)
                    pagina1.kill()
                colisao = True
        

            p1 = pagina1.interact(player, camera_group.hud_surf, p1)

            if ColetouAr == False:
                print("nao")
                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.floresta.limites, gamemaps.floresta.mapafinal, colisao_floresta, camera_group, colidindo, incapacitada)
            
            if ColetouAr:
                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.floresta.limites, gamemaps.floresta.mapafinal, colisao_floresta_final, camera_group, colidindo, incapacitada)
                
                if pygame.sprite.collide_mask(player, lapide):
                    break
            
            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_floresta, indice, checkpos)
            
            # FLORESTA PARA LOBBY #

            if player.rect.collidepoint(962, 210):
                    gamearea = "lobby"
                    gamemaps.map = "lobby"
                    colisao, contador_mapas = troca_mapa(colisao_floresta, camera_group, 5, 1800, 1035, 2155, player)
                    textbox_surgiu = False
                    pagina1.kill()


        ####################       ####################
        #################### LOBBY ####################
        ####################       ####################

        elif gamemaps.map == "lobby":

            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_z]:
                camera_group.limpa_superficie()

            if colisao == False:
                
                if ColetouLuz == False and ColetouAgua == False:
                    colisao_lobby = gamemaps.Colisao_lobby((0,0), camera_group)
                    agua = gamemaps.Colisao_lobby_agua((0,0), camera_group)
                    luz = False

                elif ColetouLuz and ColetouAgua == False:
                    agua.kill()
                    colisao_lobby.kill()
                    colisao_lobby = gamemaps.Colisao_lobby_claro((0,0), camera_group)
                    agua = gamemaps.Colisao_lobby_agua_claro((0,0), camera_group)
                    luz = True

                elif ColetouAgua:
                    agua.kill()
                    colisao_lobby.kill()
                    colisao_lobby = gamemaps.Colisao_lobby_Sem_Agua((0,0), camera_group)
                    agua = gamemaps.Colisao_lobby_agua_claro((0,0), camera_group)

                pedra0 = Pedra_lobby((1075, 250), camera_group, luz)
                arvore = Arvorezinha((2260, 680), camera_group, luz)
                colisao = True

            textboxescuridao = Textbox((0,0), 1)
            textboxesplanta = Textbox((0,0), 2)
            textboxpedra = Textbox((0,0), 3)
            textboxagua = Textbox((0,0), 4)

            ult_checkpos = Player.ultimo_checkpos(checkposx, checkposy, ult_checkpos)

            #Escuridao roadblock#
            if player.rect.collidepoint(2330, 1820) and ColetouLuz == False:
                click = True
                textboxescuridao.surgir_menu(camera_group.hud_surf, click)

            else:
                textboxescuridao.surgir_menu(camera_group.hud_surf, click)

            #Pedra roadblock#
            offset_pedra0_x = pedra0.rect.centerx - player.rect.centerx
            offset_pedra0_y = pedra0.rect.centery - player.rect.centery

            if player.mask.overlap_area(pedra0.mask, (offset_pedra0_x, offset_pedra0_y)) > 500:
                colidindo = True
                x_antigo, y_antigo = player.ultima_pos(colidindo, x_antigo, y_antigo)

            if player.mask.overlap_area(pedra0.mask, (offset_pedra0_x, offset_pedra0_y)) > 0 and delay_empurrar > 30 and ColetouTerra == True:
                delay_empurrar = pedra0.movimento_terra_lobby(ult_checkpos, delay_empurrar)


            if player.mask.overlap_area(pedra0.mask, (offset_pedra0_x, offset_pedra0_y)) > 0 and ColetouTerra == False:
                click1 = True
                textboxpedra.surgir_menu(camera_group.hud_surf, click1)

            else:
                click1 = False
                textboxpedra.surgir_menu(camera_group.hud_surf, click1)

            delay_empurrar += 1

            #arvore roadblock#
            offset_arvore_x = arvore.rect.centerx - player.rect.centerx
            offset_arvore_y = arvore.rect.centery - player.rect.centery

            if player.mask.overlap_area(arvore.mask, (offset_arvore_x, offset_arvore_y)) > 500:
                colidindo = True
                x_antigo, y_antigo = player.ultima_pos(colidindo, x_antigo, y_antigo)

            if player.mask.overlap_area(arvore.mask, (offset_arvore_x, offset_arvore_y)) > 0 and ColetouFogo == False:
                click2 = True
                textboxesplanta.surgir_menu(camera_group.hud_surf, click2)
                print("colidindo")
            
            else:
                click2 = False
                textboxesplanta.surgir_menu(camera_group.hud_surf, click2)

            if player.mask.overlap_area(arvore.mask, (offset_arvore_x, offset_arvore_y)) > 0 and ColetouFogo == True and keys[pygame.K_z]:
                arvore.kill()
                arvore.rect.center = (-2, -2)
            
            

            #agua roadblock#
            offset_agua_x = 0 - player.rect.centerx
            offset_agua_y = 0 - player.rect.centery

            if player.mask.overlap_area(agua.mask, (offset_agua_x, offset_agua_y)) > 500 and ColetouAgua == False:
                colidindo = True
                x_antigo, y_antigo = player.ultima_pos(colidindo, x_antigo, y_antigo)

            if player.mask.overlap_area(agua.mask, (offset_agua_x, offset_agua_y)) > 0 and ColetouAgua == False:
                click = True    
                textboxagua.surgir_menu(camera_group.hud_surf, click)

            if ColetouLuz == False:
                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.lobby.limites, gamemaps.lobby.mapa, colisao_lobby, camera_group, colidindo, incapacitada)

            elif ColetouLuz:
                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.lobby.limites, gamemaps.lobby.mapaclaro, colisao_lobby, camera_group, colidindo, incapacitada)

            checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_lobby, indice, checkpos)

            #Carrega floresta    
            if player.rect.collidepoint(1040, 2205):
                gamearea = " "
                gamemaps.map = "floresta"
                colisao, contador_mapas = troca_mapa(colisao_lobby, camera_group, 0, 0, 962, 274, player)
                pedra0.kill()
                arvore.kill()
                agua.kill()

            #Carrega Luz    
            if player.rect.collidepoint(130, 1815):
                gamearea = "luz"
                gamemaps.map = "luz1"
                colisao, contador_mapas = troca_mapa(colisao_lobby, camera_group, 0, 0, 1032, 414, player)
                pedra0.kill()
                arvore.kill()
                agua.kill()


            #Carrega Fogo
            elif player.rect.collidepoint(2330, 1820) and ColetouLuz == True:
                colisao, contador_mapas = troca_mapa(colisao_lobby, camera_group, 25, 9425, 335, 9760, player)
                gamearea = "fogo"
                gamemaps.map = "fogo1"
                pedra0.kill()
                arvore.kill()
                agua.kill()
            
            #carrega agua
            elif player.rect.collidepoint(1105, 175) and ColetouTerra == True:
                colisao, contador_mapas = troca_mapa(colisao_lobby, camera_group, 203, 1004, 841, 1462, player)
                gamearea = "agua"
                gamemaps.map = "agua1"
                pedra0.kill()
                arvore.kill()
                agua.kill()

            #carrega ar
            elif player.rect.collidepoint(250,360) and ColetouAgua == True:
                colisao, contador_mapas = troca_mapa(colisao_lobby, camera_group, 0, 220, 840, 740, player)
                gamearea = "ar"
                gamemaps.map = "ar1"
                pedra0.kill()
                arvore.kill()
                agua.kill()
            
            #carrega terra
            elif player.rect.collidepoint(2325, 675) and ColetouFogo == True:
                colisao, contador_mapas = troca_mapa(colisao_lobby, camera_group, 0, 0, 200, 870, player)
                gamearea = "terra"
                gamemaps.map = "terra1"
                pedra0.kill()
                arvore.kill()
                agua.kill()

            #carrega florestafinal
            elif player.rect.collidepoint(1425, 1130) and ColetouAr:
                gamearea = " "
                gamemaps.map = "floresta"
                colisao, contador_mapas = troca_mapa(colisao_lobby, camera_group, 0, 1468, 585, 2000, player)
                pedra0.kill()
                arvore.kill()
                agua.kill()

        ####################          ####################
        #################### AREA LUZ ####################
        ####################          ####################

        if gamearea == "luz":

            #################### MAPA LUZ1 ####################
            if gamemaps.map == "luz1":

                if ColetouLuz == False:
                    camera_group.fade(1280, 720, 215)

                if colisao == False:
                    colisao_luz1 = gamemaps.Colisao_luz1((0,0), camera_group)
                    if p2 == False:
                        pagina2 = Pagina((112, 464), camera_group, 2)
                    colisao = True
            
                p2 = pagina2.interact(player, camera_group.hud_surf, p2)

                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.luz1.limites, gamemaps.luz1.mapa, colisao_lobby, camera_group, colidindo, incapacitada)
                checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_luz1, indice, checkpos)

                    
                #luz1 para luz 2
                if player.rect.collidepoint(782, 44):
                    gamemaps.map = "luz2"
                    colisao, contador_mapas = troca_mapa(colisao_luz1, camera_group, 637, 880, 1315, 1450, player)
                    textbox_surgiu = False
                    pagina2.kill()

                #luz1 para luzup
                elif player.rect.collidepoint(527, 429):
                    colisao, contador_mapas = troca_mapa(colisao_luz1, camera_group, 637, 880, 2115, 40, player)
                    gamemaps.map = "luzup"     
                    player.rect.centerx = 3020
                    player.rect.centery = 490
        
                #luz 1 para lobby
                elif player.rect.collidepoint(1107, 414):
                    gamearea = "lobby"
                    gamemaps.map = "lobby"
                    colisao, contador_mapas = troca_mapa(colisao_luz1, camera_group, 15, 1000, 200, 1815, player)
                    textbox_surgiu = False
                    pagina2.kill()
                    

            #################### MAPA LUZ2 ####################      
            elif gamemaps.map == "luz2":

                if ColetouLuz == False:
                    camera_group.fade(1280, 720, 200)

                if colisao == False:
                    colisao_luz2 = gamemaps.Colisao_luz2((0,0), camera_group)
                    if p3 == False:
                        pagina3 = Pagina((390, 1350), camera_group, 3)
                    colisao = True

                p3 = pagina3.interact(player, camera_group.hud_surf, p3)

                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.luz2.limites, gamemaps.luz2.mapa, colisao_luz2, camera_group, colidindo, incapacitada)
                checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_luz2, indice, checkpos)


                #luz2 para luz3
                if player.rect.collidepoint(130, 355):
                    colisao, contador_mapas = troca_mapa(colisao_luz2, camera_group, -5, 35, 775, 105, player)
                    gamemaps.map = "luz3"
                    pagina3.kill()

                #luz 2 para luz 1
                elif player.rect.collidepoint(1325, 1550):
                    gamemaps.map = "luz1"
                    colisao, contador_mapas = troca_mapa(colisao_luz2, camera_group, 5, 15, 782, 114, player)
                    pagina3.kill()


            #################### MAPA LUZ UP ####################
            # elif gamemaps.map == "luzup":

            #     if colisao == False:
            #         colisao_up = gamemaps.Colisao_primaria((0,0), camera_group)
            #         colisao = True

            #     contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.luzup.limites, gamemaps.luzup.mapa, colisao_up, camera_group, colidindo, incapacitada)
            #     checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_up, indice, checkpos)

            #     #luz up para luz 1
            #     if player.rect.collidepoint(3020, 415):
            #         contador_check = camera_group.camera_check(5, 140)
            #         gamemaps.map = "luz1"
                    
            #         contador_mapas = 0
            #         player.rect.centerx = 582
            #         player.rect.centery = 429
                
            #     #luz up para luz puzzle
            #     elif player.rect.collidepoint(400, 790):
            #         camera_group.camera_check(0, 0)
            #         gamemaps.map = "luzpuzzle"
            #         contador_mapas = 0
            #         player.rect.centerx = 0
            #         player.rect.centery = 0


            #################### MAPA LUZ 3 ####################
            elif gamemaps.map == "luz3":

                if ColetouLuz == False:
                    camera_group.fade(1280, 720, 185)

                if colisao == False:
                    colisao_luz3 = gamemaps.Colisao_luz3((0,0), camera_group)
                    if p4 == False:
                        pagina4 = Pagina((230, 605), camera_group, 4)
                    colisao = True

                p4 = pagina4.interact(player, camera_group.hud_surf, p4)

                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.luz3.limites, gamemaps.luz3.mapa, colisao_luz3, camera_group, colidindo, incapacitada)
                checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_luz3, indice, checkpos)


                #luz3 para luzpuzzle
                if player.rect.collidepoint(780, 1130):
                    colisao, contador_mapas = troca_mapa(colisao_luz3, camera_group, 0, 0, 655, 105, player)
                    gamemaps.map = "luzpuzzle"
                    pagina4.kill()

                #luz3 para luz2    
                elif player.rect.collidepoint(850, 105):
                    colisao, contador_mapas = troca_mapa(colisao_luz3, camera_group, 10, 15, 180, 355, player)
                    gamemaps.map = "luz2"
                    pagina4.kill()


            #################### MAPA LUZ PUZZLE ####################
            elif gamemaps.map == "luzpuzzle":

                if ColetouLuz == False:
                    camera_group.fade(1280, 720, 150)

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
                        textbox_surgiu = False

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

                if colisao == False:
                    colisao_luzgema = gamemaps.Colisao_luzgema((0,0), camera_group)
                    textboxluzgema = Textbox((-10,-10), 5)
                    colisao = True

                if GemaLuz == False:
                    GemaLuz = True
                    gema_luz = Gema((635,470), camera_group, gamemaps.luzgema.gema)

                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.luzgema.limites, gamemaps.luzgema.mapa, colisao_luzgema, camera_group, colidindo, incapacitada)
                checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_luzgema, indice, checkpos)

                keys = pygame.key.get_pressed()


                if player.rect.colliderect(gema_luz):
                    textbox_surgiu = textboxluzgema.surgir(camera_group.hud_surf, textbox_surgiu)
                    gema_luz.kill()   
                    ColetouLuz = True

                if keys[pygame.K_z] and ColetouLuz:
                    gamearea = "lobby"
                    gamemaps.map = "lobby"
                    colisao, contador_mapas = troca_mapa(colisao_luzgema, camera_group, 5, 15, 1035, 2135, player)
                    textbox_surgiu = False


                

        ####################           ####################
        #################### ??REA FOGO ####################
        ####################           ####################

        elif gamearea == "fogo":


            #################### MAPA FOGO 1 ####################
            if gamemaps.map == "fogo1":
                if colisao == False:
                    colisao_fogo1 = gamemaps.Colisao_fogo1((0,0), camera_group)
                    pagina7 = Pagina((8060, 3890), camera_group, 7)
                    pagina6 = Pagina((4485, 5415), camera_group, 6)
                    pagina5 = Pagina((435, 9760), camera_group, 5)
                    colisao = True

                colidindo = player.anula_colisao(colidindo)
                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.fogo1.limites, gamemaps.fogo1.mapa, colisao_fogo1, camera_group, colidindo, incapacitada)
                checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_fogo1, indice, checkpos)

                p5 = pagina5.interact(player, camera_group.hud_surf, p5)
                p6 = pagina6.interact(player, camera_group.hud_surf, p6)
                p7 = pagina7.interact(player, camera_group.hud_surf, p7)
                
                #fogo1 para fogo2
                if player.rect.collidepoint(14155, 170):
                    colisao, contador_mapas = troca_mapa(colisao_fogo1, camera_group, 15, 235, 655, 710, player)
                    gamemaps.map = "fogo2"
                    pagina5.kill()
                    pagina6.kill()
                    pagina7.kill()

                #fogo1 para lobby
                elif player.rect.collidepoint(265, 9760):
                    colisao, contador_mapas = troca_mapa(colisao_fogo1, camera_group, 1205, 1460, 2260, 1820, player)
                    gamearea = "lobby"
                    gamemaps.map = "lobby"
                    pagina5.kill()
                    pagina6.kill()
                    pagina7.kill()

            #################### MAPA FOGO 2 ####################   
            if gamemaps.map == "fogo2":
                if colisao == False:
                    colisao_fogo2 = gamemaps.Colisao_fogo2((0,0), camera_group)
                    textboxfogogema = Textbox((-10,-10), 6)
                    colisao = True

                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.fogo2.limites, gamemaps.fogo2.mapa, colisao_fogo2, camera_group, colidindo, incapacitada)
                checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_fogo2, indice, checkpos)

                keys = pygame.key.get_pressed()


                if GemaFogo == False:
                    GemaFogo = True
                    gema_fogo = Gema((662,459), camera_group, gamemaps.fogo2.gema)

                if player.rect.colliderect(gema_fogo):
                    gema_fogo.kill()
                    ColetouFogo = True
                    textbox_surgiu =  textboxfogogema.surgir(camera_group.hud_surf, textbox_surgiu)

                if keys[pygame.K_z] and ColetouFogo:
                    gamearea = "lobby"
                    gamemaps.map = "lobby"
                    colisao, contador_mapas = troca_mapa(colisao_fogo2, camera_group, 5, 15, 1035, 2135, player)
                    textbox_surgiu = False

                #fogo 2 para fogo 1
                if player.rect.collidepoint(650, 770):
                    colisao, contador_mapas = troca_mapa(colisao_fogo2, camera_group, 13515, 80, 14155, 225, player)
                    gamemaps.map = "fogo1"



        ####################            ####################
        #################### ??REA AGUA ####################
        ####################            ####################

        elif gamearea == "agua":


            #################### MAPA AGUA 1 ####################   
            if gamemaps.map == "agua1":
                if colisao == False:
                    colisao_agua1 = gamemaps.Colisao_agua1((0,0), camera_group)
                    pagina9 = Pagina((841, 202), camera_group, 9)
                    colisao = True

                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player,  gamemaps.agua1.limites, gamemaps.agua1.mapa, colisao_agua1, camera_group, colidindo, incapacitada)
                checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_agua1, indice, checkpos)

                p9 = pagina9.interact(player, camera_group.hud_surf, p9)

                #agua 1 para agua 2
                if player.rect.collidepoint(1281, 897):
                    colisao, contador_mapas = troca_mapa(colisao_agua1, camera_group, 1045, 460, 1685, 820, player)
                    gamemaps.map = "agua2"
                    pagina9.kill()

                elif player.rect.collidepoint(411, 907):
                    colisao, contador_mapas = troca_mapa(colisao_agua1, camera_group, 0, 460, 640, 820, player)
                    gamemaps.map = "agua2"
                    pagina9.kill()
                
                #agua 1 para lobby
                elif player.rect.collidepoint(841, 1552):
                    colisao, contador_mapas = troca_mapa(colisao_agua1, camera_group, 465, 15, 1100, 230, player)
                    gamearea = "lobby"
                    gamemaps.map = "lobby"
                    pagina9.kill()


            #################### MAPA AGUA 2 ####################  
            elif gamemaps.map == "agua2":
                if colisao == False:
                    colisao_agua2 = gamemaps.Colisao_agua2((0,0), camera_group)
                    pagina10 = Pagina((835, 350), camera_group, 10)
                    pagina10b = Pagina((1475, 350), camera_group, 10)
                    colisao = True

                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.agua2.limites, gamemaps.agua2.mapa, colisao_agua2, camera_group, colidindo, incapacitada)
                checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_agua2, indice, checkpos)

                p10 = pagina10.interact(player, camera_group.hud_surf, p10)
                p10b = pagina10b.interact(player, camera_group.hud_surf, p10b)

                #agua 2 para agua 3a
                if player.rect.collidepoint(260, 350):
                    colisao, contador_mapas = troca_mapa(colisao_agua2, camera_group, 55, 1200, 970, 1630, player)
                    gamemaps.map = "agua3a"
                    pagina10.kill()
                    pagina10b.kill()

                #agua 2 para agua 3b
                elif player.rect.collidepoint(2070, 350):
                    colisao, contador_mapas = troca_mapa(colisao_agua2, camera_group, 10, 1200, 330, 1630, player)
                    gamemaps.map = "agua3b"
                    pagina10.kill()
                    pagina10b.kill()

                #agua 2 para agua 1
                elif player.rect.collidepoint(1615, 815):
                    colisao, contador_mapas = troca_mapa(colisao_agua2, camera_group, 425, 545, 1195, 895, player)
                    gamemaps.map = "agua1"
                    pagina10.kill()
                    pagina10b.kill()
                
                elif player.rect.collidepoint(715, 815):
                    colisao, contador_mapas = troca_mapa(colisao_agua2, camera_group, 10, 535, 480, 895, player)
                    gamemaps.map = "agua1"
                    pagina10.kill()
                    pagina10b.kill()

            
            #################### MAPA AGUA 3A ####################
            elif gamemaps.map == "agua3a":
                if colisao == False:
                    colisao_agua3a = gamemaps.Colisao_agua3a((0,0), camera_group)
                    pagina11 = Pagina((80, 235), camera_group, 11)
                    colisao = True

                p11 = pagina11.interact(player, camera_group.hud_surf, p11)

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
                    pagina11b = Pagina((1240, 235), camera_group, 11)
                    colisao = True

                p11b = pagina11b.interact(player, camera_group.hud_surf, p11b)

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


                    if player.mask.overlap_area(pedra.mask, (offsetx, offsety)) > 260:
                            colidindo = True
                            x_antigo, y_antigo = player.ultima_pos(colidindo, x_antigo, y_antigo)
                    if player.mask.overlap_area(pedra.mask, (offsetx, offsety)) > 0:
                        pode_empurrar = pedra.check_pos_futura(pedras, ult_checkpos)
                        if delay_empurrar > 20 and pode_empurrar:
                            delay_empurrar = pedra.movimento(ult_checkpos, delay_empurrar, player)
                    
                delay_empurrar += 1

                #agua puzzle para agua 3a
                if player.rect.collidepoint(115, 1305):
                    colisao, contador_mapas = troca_mapa(colisao_aguapuzzle, camera_group, 0, 0, 525, 170, player)
                    gamemaps.map = "agua3a"
                    for i in range(len(pedras)):
                        pedras[i].kill()
                    sprites_aguapuzzle = False

                #agua puzzle para agua gema
                if player.rect.collidepoint(1295, 45):
                    colisao, contador_mapas = troca_mapa(colisao_aguapuzzle, camera_group, 0, 180, 645, 750, player)
                    gamemaps.map = "aguagema"
                    for i in range(len(pedras)):
                        pedras[i].kill()
                    sprites_aguapuzzle = False
                    

        #################### MAPA AGUA GEMA ####################
            elif gamemaps.map == "aguagema":

                if colisao == False:
                        colisao_aguagema = gamemaps.Colisao_aguagema((0,0), camera_group)
                        textboxaguagema = Textbox((0,0), 8)
                        colisao = True

                keys = pygame.key.get_pressed()

                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.aguagema.limites, gamemaps.aguagema.mapa, colisao_aguagema, camera_group, colidindo, incapacitada)
                checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_aguagema, indice, checkpos)
                    
                if GemaAgua == False:
                    GemaAgua = True
                    gema_agua = Gema((662,459), camera_group, gamemaps.aguagema.gema)

                if player.rect.colliderect(gema_agua):
                    gema_agua.kill()
                    ColetouAgua = True
                    textbox_surgiu = textboxaguagema.surgir(camera_group.hud_surf, textbox_surgiu)

                if keys[pygame.K_z] and ColetouAgua:
                    gamearea = "lobby"
                    gamemaps.map = "lobby"
                    textbox_surgiu = False
                    colisao, contador_mapas = troca_mapa(colisao_aguagema, camera_group, 5, 15, 1035, 2135, player)


        ####################          ####################
        #################### ??REA AR  ####################
        ####################          ####################

        elif gamearea == "ar":
            
        
        #################### MAPA AR 1 #################### 
            if gamemaps.map == "ar1":
                if colisao == False:
                    colisao_ar1 = gamemaps.Colisao_ar1((0,0), camera_group)
                    pagina12 = Pagina((620, 190), camera_group, 13)
                    colisao = True

                p12 = pagina12.interact(player, camera_group.hud_surf, p12)

                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.ar1.limites, gamemaps.ar1.mapa, colisao_ar1, camera_group, colidindo, incapacitada)
                checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_ar1, indice, checkpos)
                
                #ar 1 para ar2
                if player.rect.collidepoint(330, 155):
                    colisao, contador_mapas = troca_mapa(colisao_ar1, camera_group, 0, 560, 580, 1135, player)
                    gamemaps.map = "ar2"
                    pagina12.kill()
                
                #ar 1 para lobby
                if player.rect.collidepoint(925, 735):
                    colisao, contador_mapas = troca_mapa(colisao_ar1, camera_group, 0, 15, 335, 365, player)
                    gamearea = "lobby"
                    gamemaps.map = "lobby"
                    pagina12.kill()
                
        #################### MAPA AR 2 ####################
                    
            elif gamemaps.map == "ar2":

                if colisao == False:
                    colisao_ar2 = gamemaps.Colisao_ar2((0,0), camera_group)
                    pagina13 = Pagina((720, 575), camera_group, 14)
                    colisao = True

                p13 = pagina13.interact(player, camera_group.hud_surf, p13)

                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.ar2.limites, gamemaps.ar2.mapa, colisao_ar2, camera_group, colidindo, incapacitada)
                checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_ar2, indice, checkpos)

                #ar 2 para ar puzzle
                if player.rect.collidepoint(525, 30):
                    colisao, contador_mapas = troca_mapa(colisao_ar2, camera_group, 230, 805, 875, 1290, player)
                    gamemaps.map = "arpuzzle"
                    pagina13.kill()

                #ar 2 para ar 1
                if player.rect.collidepoint(650, 1110):
                    colisao, contador_mapas = troca_mapa(colisao_ar2, camera_group, 0, 15, 330, 245, player)
                    gamemaps.map = "ar1"
                    pagina13.kill()



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
                    textboxargema = Textbox((0,0), 9)
                    colisao = True

                if GemaAr == False:
                    GemaAr = True
                    gema_ar = Gema((662,459), camera_group, gamemaps.argema.gema)

                keys = pygame.key.get_pressed()

                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.argema.limites, gamemaps.argema.mapa, colisao_argema, camera_group, colidindo, incapacitada)
                checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_argema, indice, checkpos)
                

                if player.rect.colliderect(gema_ar):
                    gema_ar.kill()
                    ColetouAr = True
                    textbox_surgiu = textboxargema.surgir(camera_group.hud_surf, textbox_surgiu)

                if keys[pygame.K_z] and ColetouAr:
                    gamearea = "lobby"
                    gamemaps.map = "lobby"
                    colisao, contador_mapas = troca_mapa(colisao_argema, camera_group, 5, 15, 1315, 1340, player)
                    textbox_surgiu = False


                

        ####################            ####################
        #################### ??REA TERRA ####################
        ####################            ####################

        elif gamearea == "terra":

        #################### MAPA TERRA1 ####################

            if gamemaps.map == "terra1":
                if colisao == False:
                    colisao_terra1 = gamemaps.Colisao_terra1((0,0), camera_group)
                    pagina8 = Pagina((980, 910), camera_group, 8)
                    colisao = True

                p8 = pagina8.interact(player, camera_group.hud_surf, p8)

                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.terra1.limites, gamemaps.terra1.mapa, colisao_terra1, camera_group, colidindo, incapacitada)
                checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_terra1, indice, checkpos)

                #terra 1 para cima
                if player.rect.collidepoint(975, 45):
                    colisao, contador_mapas = troca_mapa(colisao_terra1, camera_group, 330, 1185, 976, 1646, player)
                    gamemaps.map = "terra2"
                    saida = "baixo"
                    pagina8.kill()

                #terra 1 para direita
                elif player.rect.collidepoint(1805, 865):
                    colisao, contador_mapas = troca_mapa(colisao_terra1, camera_group, 0, 515, 196, 866, player)
                    gamemaps.map = "terra2"
                    saida = "esquerda"
                    pagina8.kill()
                
                #terra 1 para baixo
                elif player.rect.collidepoint(975, 1740):
                    colisao, contador_mapas = troca_mapa(colisao_terra1, camera_group, 335, 5, 971, 106, player)
                    gamemaps.map = "terra2"
                    saida = "cima"
                    pagina8.kill()

                #terra 1 para esquerda
                elif player.rect.collidepoint(135, 865):
                    colisao, contador_mapas = troca_mapa(colisao_terra1, camera_group, 1195, 320, 2255, 680, player)
                    gamemaps.map = "lobby"
                    saida = "esquerda"
                    pagina8.kill()
                
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


            #################### MAPA TERRA GEMA ####################

            elif gamemaps.map == "terragema":

                if colisao == False:
                    colisao_terragema = gamemaps.Colisao_terragema((0,0), camera_group)
                    textboxterragema = Textbox((0,0), 7)
                    colisao = True

                keys = pygame.key.get_pressed()

                contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.terragema.limites, gamemaps.terragema.mapa, colisao_terragema, camera_group, colidindo, incapacitada)
                checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_terragema, indice, checkpos)

                if GemaTerra == False:
                    GemaTerra = True
                    gema_terra = Gema((662,459), camera_group, gamemaps.terragema.gema)


                if player.rect.colliderect(gema_terra):
                    textbox_surgiu = textboxterragema.surgir(camera_group.hud_surf, textbox_surgiu)
                    gema_terra.kill()
                    ColetouTerra = True

                if keys[pygame.K_z] and ColetouTerra:
                    colisao, contador_mapas = troca_mapa(colisao_terragema, camera_group, 5, 15, 1035, 2135, player)
                    gamearea = "lobby"
                    gamemaps.map = "lobby"
                    textbox_surgiu = False


        # elif gamemaps.area == "florestafinal":
        #     if gamemaps.map == "florestafinal":

        #          if colisao == False:
        #             colisao_floresta = gamemaps.Colisao_floresta((0,0), camera_group)
        #             colisao_floresta = Textbox((0,0), 7)
        #             colisao = True
    
        #         contador_mapas, colidindo = carrega_mapa(contador_mapas, tela, player, gamemaps.floresta.limites, gamemaps.floresta.mapa, colisao_floresta, camera_group, colidindo, incapacitada)
        #         checkposx, checkposy, x_antigo, y_antigo, indice, checkpos = player.update(incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, colisao_floresta, indice, checkpos)


        #print(clock)
        #print(player.rect.centerx, player.rect.centery, "###", player.rect.x, player.rect.y, "###", camera_group.offset.x, camera_group.offset.y, gamemaps.map)
        # current_time = pygame.time.get_ticks()
        # current_second = int(current_time/1000)
        #if Tempo == current_second:
        #     Passado = Tempo
        #     Tempo = Tempo+1
        #     print(Tempo)
        #     print(Passado)
