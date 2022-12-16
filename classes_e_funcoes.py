import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("sprites calefia\Baixo\B1.png").convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = pygame.math.Vector2()
        self.speed = 5

    def check_colisao(self, mapa_colisao):
        colidindo = False
        offsetx = 0 - self.rect.centerx
        offsety = 0 - self.rect.centery

        if self.mask.overlap_area(mapa_colisao.mask, (offsetx, offsety)) > 200:
            colidindo = True            
        return colidindo

    def check_colisao_gelo(self, area_gelo):
            esta_no_gelo = False
            offsetx = 0 - self.rect.centerx
            offsety = 0 - self.rect.centery

            if self.mask.overlap_area(area_gelo.mask, (offsetx, offsety)) > 200:
                # print("esta no gelo")
                esta_no_gelo = True
            return esta_no_gelo 

    def check_colisao2(self, mapa_colisao):
        colidindo = False
        offsetx = 0 - self.rect.centerx
        offsety = 0 - self.rect.centery

        if self.mask.overlap_area(mapa_colisao.mask, (offsetx, offsety)) > 100:
            colidindo = True            
        return colidindo


    def input(self, incapacitada, colidindo, checkposx, checkposy):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and incapacitada != "UP":
            self.direction.y = -1
            checkposy = "up"
            andando_vertical = True


        elif keys[pygame.K_DOWN] and incapacitada != "DOWN":
            self.direction.y = 1
            checkposy = "down"
            andando_vertical = True
        
        else:
            self.direction.y = 0
            checkposy = " "
            andando_vertical = False


        if keys[pygame.K_RIGHT] and incapacitada != "RIGHT":
            self.direction.x = 1
            checkposx = "right"
            andando_horizontal = True

        elif keys[pygame.K_LEFT] and incapacitada != "LEFT":
            self.direction.x = -1
            checkposx = "left"
            andando_horizontal = True
        
        else:
            self.direction.x = 0
            checkposx = " "
            andando_horizontal = False

        if keys[pygame.K_LSHIFT]:
            self.speed = 25
        else:
            self.speed = 10
        
        if keys[pygame.K_q]:
            print(self.rect.centerx, self.rect.centery, "###", self.rect.x, self.rect.y, "###")
        
        return checkposx, checkposy, andando_horizontal, andando_vertical
    
    def ultima_pos(self, colidindo, x_antigo, y_antigo):
        if colidindo == False:
            x_antigo = self.rect.centerx
            y_antigo = self.rect.centery
        else:
            self.rect.centerx = x_antigo
            self.rect.centery = y_antigo
        return x_antigo, y_antigo

    def troca_sprite(self, checkposx, checkposy, andando_horizontal, andando_vertical, indice):

        esquerda_animacao = ["Sprites Calefia\Esquerda\E1.png", "Sprites Calefia\Esquerda\E2.png", "Sprites Calefia\Esquerda\E3.png", 
        "Sprites Calefia\Esquerda\E4.png", "Sprites Calefia\Esquerda\E5.png", "Sprites Calefia\Esquerda\E6.png", 
        "Sprites Calefia\Esquerda\E7.png", "Sprites Calefia\Esquerda\E8.png", "Sprites Calefia\Esquerda\E9.png"]

        direita_animacao = ["Sprites Calefia\Direita\D1.png", "Sprites Calefia\Direita\D2.png", "Sprites Calefia\Direita\D3.png", 
        "Sprites Calefia\Direita\D4.png", "Sprites Calefia\Direita\D5.png", "Sprites Calefia\Direita\D6.png", 
        "Sprites Calefia\Direita\D7.png", "Sprites Calefia\Direita\D8.png", "Sprites Calefia\Direita\D9.png"]

        cima_animacao = ["Sprites Calefia\Cima\C1.png", "Sprites Calefia\Cima\C2.png", "Sprites Calefia\Cima\C3.png", 
        "Sprites Calefia\Cima\C4.png", "Sprites Calefia\Cima\C5.png", "Sprites Calefia\Cima\C6.png", 
        "Sprites Calefia\Cima\C7.png", "Sprites Calefia\Cima\C8.png", "Sprites Calefia\Cima\C9.png"]

        baixo_animacao = ["Sprites Calefia\Baixo\B1.png", "Sprites Calefia\Baixo\B2.png", "Sprites Calefia\Baixo\B3.png", 
        "Sprites Calefia\Baixo\B4.png", "Sprites Calefia\Baixo\B5.png", "Sprites Calefia\Baixo\B6.png", 
        "Sprites Calefia\Baixo\B7.png", "Sprites Calefia\Baixo\B8.png", "Sprites Calefia\Baixo\B9.png"]


        if andando_horizontal == False and andando_vertical == False:
            indice = 0

        elif andando_horizontal == True:
            if checkposx == "left":
                self.image = pygame.image.load(esquerda_animacao[indice]).convert_alpha()
                indice += 1
                if indice == 9:
                    indice = 0 
            
            elif checkposx == "right":
                self.image = pygame.image.load(direita_animacao[indice]).convert_alpha()
                indice += 1
                if indice == 9:
                    indice = 0
        
        if andando_vertical == False and andando_horizontal == False:
            indice = 0
            
        elif andando_vertical == True and andando_horizontal == False:
            if checkposy == "up":
                self.image = pygame.image.load(cima_animacao[indice]).convert_alpha()
                indice += 1
                if indice == 9:
                    indice = 0 
            elif checkposy == "down":
                self.image = pygame.image.load(baixo_animacao[indice]).convert_alpha()
                indice += 1
                if indice == 9:
                    indice = 0 

        return indice

    def ultimo_checkpos(checkposx, checkposy, ult_checkpos):
        if checkposx != " " and checkposy == " ":
            ult_checkpos = checkposx
            return ult_checkpos

        if checkposy != " " and checkposx == " ":
            ult_checkpos = checkposy
            return ult_checkpos
        
        return ult_checkpos

    def interact(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_z]:
            return True        

    def anula_colisao(self, colidindo):
        keys = pygame.key.get_pressed()

        colidindo = False
        return colidindo

    def update(self, incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, mapa_parede, indice, checkpos):
        
        colidindo = self.check_colisao(mapa_parede)
        checkposx, checkposy, andando_horizontal, andando_vertical = self.input(incapacitada, colidindo, checkposx, checkposy)
        x_antigo, y_antigo = self.ultima_pos(colidindo, x_antigo, y_antigo)
        indice = self.troca_sprite(checkposx, checkposy, andando_horizontal, andando_vertical, indice)
        self.rect.center += self.direction * self.speed


        return checkposx, checkposy, x_antigo, y_antigo, indice, checkpos


    def update_no_gelo(self, incapacitada, colidindo, x_antigo, y_antigo, checkposx, checkposy, mapa_parede, indice, checkpos, ult_checkpos, esta_no_gelo, area_gelo):
        
        colidindo = self.check_colisao2(mapa_parede)
        checkposx, checkposy, andando_horizontal, andando_vertical = self.input(incapacitada, colidindo, checkposx, checkposy)
        x_antigo, y_antigo = self.ultima_pos(colidindo, x_antigo, y_antigo)
        indice = self.troca_sprite(checkposx, checkposy, andando_horizontal, andando_vertical, indice)
        esta_no_gelo = self.check_colisao_gelo(area_gelo)

        if esta_no_gelo:
            self.speed = 15
            if ult_checkpos == "right":   
                self.direction.x = 1 
                self.rect.center += self.direction * self.speed

            if ult_checkpos == "left":   
                self.direction.x = -1
                self.rect.center += self.direction * self.speed

            if ult_checkpos == "up":
                self.direction.y = -1 
                self.rect.center += self.direction * self.speed

            if ult_checkpos == "down":    
                self.direction.y = 1
                self.rect.center += self.direction * self.speed
        else:
            self.rect.center += self.direction * self.speed

        return checkposx, checkposy, x_antigo, y_antigo, indice, checkpos, ult_checkpos, esta_no_gelo

    
class Pagina(pygame.sprite.Sprite):
    def __init__(self, pos, group, id):
        super().__init__(group)
        self.image = pygame.image.load("sprites\pagina.png").convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.id = id

        self.lista_paginas = ["sprites paginas\id 0.jpg", "sprites paginas\id 1.png"]
        self.pagina_aberta = pygame.image.load(self.lista_paginas[id]).convert_alpha()


    def interact(self, player, superficie, coletou):

        transparente = (0,0,0,0)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_e] and self.rect.colliderect(player.rect):
            self.kill()
            superficie.blit(self.pagina_aberta, (490, 150))
            coletou = True

        if keys[pygame.K_ESCAPE]:
            #Esteban, se você estiver lendo isso, sei que a lógica é nojenta, mas foi o que deu pra fazer :)
            superficie.fill(transparente)

        return coletou


class Textbox(pygame.sprite.Sprite):
    def __init__(self, pos, id):

        self.lista_caixas = ["sprites textbox\id0.png", "sprites textbox\TextBoxEscuro.png", "sprites textbox\TextBoxFogo.png", "sprites textbox\TextBoxPedras.png", 
        "sprites textbox\TextBoxAgua.png", "sprites textbox\TextBoxCristalLuz.png", "sprites textbox\TextBoxCristalFogo.png", "sprites textbox\TextBoxCristalTerra.png",
         "sprites textbox\TextBoxCristalAgua.png", "sprites textbox\TextBoxCristalAr.png"]
        self.caixa = pygame.image.load(self.lista_caixas[id]).convert_alpha()
        self.rect = self.caixa.get_rect(center = pos)
        self.id = id
        self.surgiu = False
        
    def surgir(self, superficie, textbox_surgiu):
        transparente = (0,0,0,0)
        keys = pygame.key.get_pressed()

        if textbox_surgiu == False:
            superficie.blit(self.caixa, (400, 500))

        if keys[pygame.K_z]:
            superficie.fill(transparente)
            textbox_surgiu = True
        
        return textbox_surgiu

    def surgir_menu(self, superficie, click):
        transparente = (0,0,0,0)
        keys = pygame.key.get_pressed()

        if self.surgiu == False and click:
            superficie.blit(self.caixa, (500, 500))

        elif click == False:
            superficie.fill(transparente)
            self.surgiu = True
        
class Pedra(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("sprites\pedra redonda.png").convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.pode_empurrar = True

    def movimento(self, checkpos, delay_empurrar, player):
        keys = pygame.key.get_pressed()

        if checkpos == "up" and keys[pygame.K_x] and self.rect.centery >= 764 and player.rect.centery > self.rect.centery:
            self.rect.centery -= 46
            delay_empurrar = 0
            self.direcao_pedra = "cima"


        elif checkpos == "down" and keys[pygame.K_x] and self.rect.centery <= 902 and player.rect.centery < self.rect.centery:
            self.rect.centery += 46
            delay_empurrar = 0
            self.direcao_pedra = "baixo"

        elif checkpos == "right" and keys[pygame.K_x] and self.rect.centerx > 1127 and player.rect.centerx < self.rect.centerx:
                self.rect.centerx += 55
                delay_empurrar = 0
                self.direcao_pedra = "direita"

        elif checkpos == "left" and keys[pygame.K_x] and self.rect.centerx < 1402 and player.rect.centerx > self.rect.centerx:
                self.rect.centerx -= 55
                delay_empurrar = 0
                self.direcao_pedra = "esquerda"

        return delay_empurrar



    def check_pos_futura(self, lista_pedras, checkpos):
        lista_pedras.remove(self)

        for outras_pedras in lista_pedras:

            if checkpos == "up":
                if self.rect.centery - 46 == outras_pedras.rect.centery and self.rect.centerx == outras_pedras.rect.centerx:
                    self.pode_empurrar = False
                    break
                else:
                    self.pode_empurrar = True

            elif checkpos == "down":
                if self.rect.centery + 46 == outras_pedras.rect.centery and self.rect.centerx == outras_pedras.rect.centerx:
                    self.pode_empurrar = False
                    break
                else:
                    self.pode_empurrar = True

            elif checkpos == "right":
                if self.rect.centerx  + 55 == outras_pedras.rect.centerx and self.rect.centery == outras_pedras.rect.centery:
                    self.pode_empurrar = False
                    break
                else:
                    self.pode_empurrar = True


            elif checkpos == "left":
                if self.rect.centerx - 55 == outras_pedras.rect.centerx and self.rect.centery == outras_pedras.rect.centery:
                    self.pode_empurrar = False
                    break
                else:
                    self.pode_empurrar = True

        lista_pedras.append(self)

        return self.pode_empurrar



class Pedra_lobby(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("sprites\pedra redonda do lobby.png").convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.pode_empurrar = True

    def movimento_terra_lobby(self, checkpos, delay_empurrar):
        keys = pygame.key.get_pressed()

        if checkpos == "up" and keys[pygame.K_x]:
            self.rect.centery -= 46
            delay_empurrar = 0


        elif checkpos == "down" and keys[pygame.K_x]:
            self.rect.centery += 46
            delay_empurrar = 0

        elif checkpos == "right" and keys[pygame.K_x]:
                self.rect.centerx += 55
                delay_empurrar = 0

        elif checkpos == "left" and keys[pygame.K_x]:
                self.rect.centerx -= 55
                delay_empurrar = 0


        return delay_empurrar

class Arvorezinha(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("sprites\Arvorezinha.png").convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.mask = pygame.mask.from_surface(self.image)



class Gema(pygame.sprite.Sprite):
    def __init__(self, pos, group, elemento):
        super().__init__(group)
        self.image = pygame.image.load(elemento).convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.mask = pygame.mask.from_surface(self.image)

class Cogumelo(pygame.sprite.Sprite):
    def __init__(self, pos, group, Cor):
            super().__init__(group)
            self.cor = Cor
            
            if self.cor == "vermelho":
                self.image = pygame.image.load("sprites\mushroom_vermelho.png").convert_alpha()
                self.rect = self.image.get_rect(center = pos)
            else:
                self.image = pygame.image.load("sprites\mushroom_verde.png").convert_alpha()
                self.rect = self.image.get_rect(center = pos)
            
    def trocar(grupos):
        
        for cogumelo in grupos:
            if cogumelo.cor == "verde":
                cogumelo.image = pygame.image.load("sprites\mushroom_vermelho.png").convert_alpha()
                cogumelo.cor = "vermelho"

            elif cogumelo.cor == "vermelho":
                cogumelo.image = pygame.image.load("sprites\mushroom_verde.png").convert_alpha()
                cogumelo.cor = "verde"
        delay_trocar = 0

        return delay_trocar
    
    def check_cores(cogumelos, contador, venceu):
        if venceu == False:
            venceu = False
            for cogumelo in cogumelos:
                if cogumelo.cor == "verde":
                    contador += 1
                if contador == 9:
                    venceu = True
            contador = 0
            return contador, venceu


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        self.display_surface = pygame.display.get_surface()

        #movimento da camera
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0]/2
        self.half_h = self.display_surface.get_size()[1]/2

        self.hud_surf = pygame.image.load("sprites\Adan.png")
        self.hud_rect = self.hud_surf.get_rect(topleft = (0, 0))

    def fade(self, width, height, alpha): 
        Fade = False
        ate = 0
        #self.hud_surf = pygame.Surface((width, height))
        self.hud_surf.fill((0,0,0))
        self.hud_surf.set_alpha(alpha)
        self.display_surface.blit(self.hud_surf, (0,0))
        for i in range(0, 1200):
            ate += 1
            if ate >= 1180:
                Fade = True

        return Fade, ate

    # def fade_out(self, width, height):
        
    #     fade.fill((0,0,0))
    #     for i in range(0, 100):
    #         fade.set_alpha(i)
    #         self.display_surface.blit(fade, (0,0))
    #         pygame.time.delay(20)
    #     return i
    

    def camera_centrada(self, target, limites):
        
        # limites = [x_menor, x_maior, y_menor, y_maior]

        if target.rect.x >= limites[0] and target.rect.x <= limites[1]:
            self.offset.x = target.rect.centerx - self.half_w
        if target.rect.y >= limites[2] and target.rect.y <= limites[3]:
            self.offset.y = target.rect.centery - self.half_h
        

    
    def camera_check(self, offx, offy):
        self.offset.x = offx
        self.offset.y = offy



    #nova função "draw" que desenha dinamicamente os objetos atras ou a frente do jogador e chama 
    #função da camera centrada
    def custom_draw(self, tela, player, limites, mapa, contador_mapas):

        if contador_mapas == 0:

            self.ground_surf = pygame.image.load(mapa)
            self.ground_rect = self.ground_surf.get_rect(center = (0,0))
            contador_mapas = contador_mapas + 1

        self.camera_centrada(player, limites)


        #desenha o chão antes de tudo
        ground_offset = self.ground_rect.center - self.offset
        tela.blit(self.ground_surf, ground_offset)
        
        #desenha outros sprites, se houverem
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.center - self.offset
            tela.blit(sprite.image, offset_pos)



        hud_offsetx = self.hud_rect.centerx - self.half_w
        hud_offsety = self.hud_rect.centery - self.half_h

        tela.blit(self.hud_surf, (hud_offsetx, hud_offsety))

        return contador_mapas


class GameMaps():
    def __init__(self):
        self.map = "floresta"
    
        # limites = [x_menor, x_maior, y_menor, y_maior]

    class Colisao_primaria(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("sprites\Adan.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)

    class floresta():
        limites = [626, 1055, 321, 1711]
        mapa = 'mapas_imagens aumentado\Floresta\MapaFloresta.png'

    class Colisao_floresta(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\Floresta\MapaFlorestaColisao.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)
    
    class lobby():
        limites = [622, 1828, 334, 2100]
        mapa = 'mapas_imagens aumentado\lobby\lobby completo.png'
        colisao = "mapas_imagens aumentado\lobby\colisao_lobby.png"

    class Colisao_lobby(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\lobby\lobby paredes_sem_agua.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)

    class Colisao_lobby_agua(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\lobby\lobby parede agua.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)


    class Colisao_lobby_Sem_Agua(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\lobby\lobby paredes_sem_agua.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)

    class luz1():
        limites = [618, 310, 335, 555]
        mapa = 'mapas_imagens aumentado\luz\luz 1.png'
        gema = "sprites\GemaAgua.png"

    class Colisao_luz1(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\luz\luz 1 parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)

    class luz2():
        limites = [630, 1240, 335, 1205]
        mapa = 'mapas_imagens aumentado\luz\luz 2.png'

    class Colisao_luz2(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\luz\luz 2 parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)

    class luz3():
        limites = [616, 616, 321, 876]
        mapa = 'mapas_imagens aumentado\luz\luz 3.png'

    class Colisao_luz3(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\luz\luz 3 parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)
    
    class luzup():
        limites = [645, 2740, 360, 1600]
        mapa = "mapas_imagens aumentado\luz\luz up.png"

    class Colisao_luzup(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)
    
    class luzpuzzle:
        limites = [626, 676, 331, 881]
        mapa = 'mapas_imagens aumentado\luz\luz puzzle 1.png'
        mapa2 = 'mapas_imagens aumentado\luz\luz puzzle 2.png'
    
    class Colisao_luzpuzzle(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\luz\luz puzzle 1 parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)
    
    class luzgema:
        limites = [621, 676, 321, 561]
        mapa = "mapas_imagens aumentado\luz\luz gema.png"
        gema = "sprites\LuzGema.png"

    class Colisao_luzgema(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\luz\luz gema parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)

    class fogo1():
        limites = [700, 14960, 400, 9910]
        mapa = 'mapas_imagens aumentado\Fogo\Fogo 1 remake.png'

    class Colisao_fogo1(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\Fogo\Fogo 1 parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)
    
    class fogo2():
        limites = [621, 681, 316, 556]
        mapa = "mapas_imagens aumentado\Fogo\Fogo puzzle remake.png"
        gema = "sprites\Gema_Fogo.png"

    class Colisao_fogo2(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\Fogo\Fogo gema parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)

    class agua1():
        limites = [630, 1056, 323, 1326]
        mapa = "mapas_imagens aumentado\Agua\Agua 1.png"

    class Colisao_agua1(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\Agua\Agua 1 parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)

    class agua2():
        limites = [621, 1701, 321, 881]
        mapa = "mapas_imagens aumentado\Agua\Agua 2.png"

    class Colisao_agua2(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\Agua\Agua 2 parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)

    class agua3a():
        limites = [631, 631, 321, 1521]
        mapa = "mapas_imagens aumentado\Agua\Agua 3a.png"

    class Colisao_agua3a(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\Agua\Agua 3b parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)

    class agua3b():
        limites = [686, 686, 321, 1521]
        mapa = "mapas_imagens aumentado\Agua\Agua 3b.png"

    class Colisao_agua3b(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\Agua\Agua 3a parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)
    
    class aguapuzzle():
        limites = [626, 1961, 316, 1201]
        mapa = "mapas_imagens aumentado\Agua\Agua puzzle.png"

    class Colisao_aguapuzzle(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\Agua\Agua 4 parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)
    
    class aguagema():
        limites = [621, 621, 326, 546]
        mapa = "mapas_imagens aumentado\Agua\Agua gema.png"
        gema = "sprites\GemaAgua.png"
    
    class Colisao_aguagema(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\Agua\Agua gema parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)

    
    class ar1():
        limites = [621, 621, 321, 556]
        mapa = "mapas_imagens aumentado\Ar\Ar 1.png"

    class Colisao_ar1(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\Ar\Ar 1 parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)

    class ar2():
        limites = [621, 621 , 321, 881]
        mapa = "mapas_imagens aumentado\Ar\Ar 2.png"

    class Colisao_ar2(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\Ar\Ar 2 parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)

    class AreaGelo(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\Ar\Ar puzzle (gelo).png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)
    
    class arpuzzle():
        limites = [626, 1901, 321, 1126]
        mapa = "mapas_imagens aumentado\Ar\Ar puzzle.png"

    class Colisao_arpuzzle(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\Ar\Ar puzzle parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)

    class argema():
        limites = [631, 631, 326, 566]
        mapa = "mapas_imagens aumentado\Ar\Ar gema.png"
        gema = "sprites\ArGema.png"

    class Colisao_argema(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\Ar\Ar gema parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)

    class terra1():
        limites = [616, 1321, 326, 1511]
        mapa = "mapas_imagens aumentado\Terra\Terra 1.png"

    class Colisao_terra1(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\Terra\Terra 1 parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)

    class terra2():
        limites = [616, 1321, 326, 1511]
        mapa = ["mapas_imagens aumentado\Terra\Terra 2.png", "mapas_imagens aumentado\Terra\Terra 3.png", "mapas_imagens aumentado\Terra\Terra 4.png",
             "mapas_imagens aumentado\Terra\Terra 5.png", "mapas_imagens aumentado\Terra\Terra 6.png", "mapas_imagens aumentado\Terra\Terra 7.png", 
              "mapas_imagens aumentado\Terra\Terra 8.png", "mapas_imagens aumentado\Terra\Terra 9.png", "mapas_imagens aumentado\Terra\Terra 10.png", 
              "mapas_imagens aumentado\Terra\Terra 11.png" ]

        mapa_colisao = ["mapas_imagens aumentado\Terra\Terra 2 parede.png", "mapas_imagens aumentado\Terra\Terra 3 parede.png", "mapas_imagens aumentado\Terra\Terra 4 parede.png", 
        "mapas_imagens aumentado\Terra\Terra 5 parede.png", "mapas_imagens aumentado\Terra\Terra 6 parede.png", "mapas_imagens aumentado\Terra\Terra 7 parede.png", 
        "mapas_imagens aumentado\Terra\Terra 8 parede.png", "mapas_imagens aumentado\Terra\Terra 9 parede.png", "mapas_imagens aumentado\Terra\Terra 10 parede.png",
         "mapas_imagens aumentado\Terra\Terra 11 parede.png"]

    class Colisao_terra2(pygame.sprite.Sprite):
        def __init__(self, pos, group, mapa):
            super().__init__(group)
            self.image = pygame.image.load(mapa).convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)


    class terragema():
        limites = [625, 680, 320, 501]
        mapa = "mapas_imagens aumentado\Terra\Terra gema.png"
        gema = "sprites\GemaTerra.png"

    class Colisao_terragema(pygame.sprite.Sprite):
        def __init__(self, pos, group):
            super().__init__(group)
            self.image = pygame.image.load("mapas_imagens aumentado\Terra\Terra gema parede.png").convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)

        
gamemaps = GameMaps()



def carrega_mapa(contador_mapas, tela, player, limites, mapa, mapa_parede, camera_group, colidindo, incapacitada):
    contador_mapas = camera_group.custom_draw(tela, player, limites, mapa, contador_mapas)

    colidindo = player.check_colisao(mapa_parede)
    pygame.display.update()

    return contador_mapas, colidindo

def troca_mapa(old_mapa_colisao, camera_group, camx, camy, posx, posy, player):
    colisao = False
    contador_mapas = 0
    old_mapa_colisao.kill()
    camera_group.camera_check(camx, camy)
    player.rect.center = (posx, posy)

    return colisao, contador_mapas

def carrega_mapa_com_gelo(contador_mapas, tela, player, limites, mapa, mapa_parede, camera_group, colidindo, incapacitada, esta_no_gelo, area_gelo):
    contador_mapas = camera_group.custom_draw(tela, player, limites, mapa, contador_mapas)
    colidindo = player.check_colisao(mapa_parede)
    esta_no_gelo = player.check_colisao_gelo(area_gelo)
    pygame.display.update()

    return contador_mapas, colidindo, esta_no_gelo


