from PPlay.sprite import *
from PPlay.collision import *

janela_largura = 1280
janela_altura = 768

def atirar(nave, janela, teclado, vely, lista, cooldown, jogo):
    if jogo == True:
        if teclado.key_pressed("SPACE") and cooldown == 0:
            criar_shoot(lista, nave)
            cooldown = 30
        if len(lista) > 0:
            for shoot in lista:
                shoot.draw()
                shoot.y -= 800 * janela.delta_time()
                if shoot.y < -10:
                    lista.remove(shoot)
        if cooldown > 0:
            cooldown -= 1
    return cooldown, jogo    

def monstromorre(matriz_inimigos, lista, score, vel, contador_mortes, contador_total):
    for i,lista_inimigos in enumerate(matriz_inimigos):
        for j,alien in enumerate(lista_inimigos):
            for k,tiro in enumerate(lista):
                if tiro.collided(alien):
                    if tiro.collided_perfect(alien):
                        lista.pop(k)
                        lista_inimigos.pop(j)
                        score += 50
                        vel *= 1.02
                        contador_mortes -= 1
                        contador_total -= 1

    return score, vel, contador_mortes, contador_total

def criar_shoot(lista,nave):
    tiro = Sprite("assets\Tiro.png")
    tiro.x = nave.x + 2
    tiro.y = nave.y - 30
    lista.append(tiro)

def inimigoandando(matriz_inimigos, janela, vel, bateu, nave):
    colide = False
    for i in matriz_inimigos:
        for j in i:
            j.x += vel
            if j.x >= janela_largura - 100  or j.x <= 0:
                colide = True   
            if j.collided(nave) or j.y >= nave.y:
                bateu = True
    if colide == True:
        vel = vel*(-1) 
        for i in matriz_inimigos:
            for j in i:
                j.x += vel
                j.y += 20
    return vel, bateu

def desenhainimigo(matriz_inimigos,contador):
    criainimigo(matriz_inimigos,contador)
    for i in matriz_inimigos:
        for j in i:
            j.draw()

def criainimigo(matriz_inimigos, num_matriz):
    if num_matriz == 0:
        for linha in range(2, -1, -1):  #Checa a matriz de baixo pra cima, otimizando o numero de vezes que ela é checada
            l = []
            for coluna in range(7):
                    inimigo = Sprite("assets\inimigo.png")
                    inimigo.x = (35 + inimigo.width)*(coluna)
                    inimigo.y = (150 - inimigo.height)*(linha)
                    l.append(inimigo)
            matriz_inimigos.append(l)
        num_matriz += 1
    return num_matriz