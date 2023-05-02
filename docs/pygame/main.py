import pygame
import tela_inverno
from tela_inverno import window
from tela_inverno import Coin 
import tela_outono
import tela_verao        
import tela_primavera
import sys            

class Tela_Inicio:
    def __init__(self,jogo):

        '''
        cria um tela de inicio para o jogo
        a imagem possui um efeito pulsante que consiste em 2 imagens de tamanho diferente
        foi criado um botão de jogar e um de instruções
        quando uma colisão do clique com o botão é detectada a tela atual é trocada para a respectiva janela
        '''
        self.jogo = jogo
        self.imagem_fundo = pygame.transform.scale(pygame.image.load('docs/imagens/seasons.webp'),(1000,410))
        self.imagem_fundo_maior = pygame.transform.scale(pygame.image.load('docs/imagens/seasons.webp'),(1005,415))
        self.titulo = pygame.transform.scale(pygame.image.load('docs/imagens/otitulo.png'),(800,90))
        self.titulo_maior = pygame.transform.scale(pygame.image.load('docs/imagens/otitulo.png'),(805,95))
        self.jogar = pygame.transform.scale(pygame.image.load('docs/imagens/Jogar2.png'),(200,80))
        self.rect_inicio = pygame.Rect(400,250,200,80)
        self.jogar_maior = pygame.transform.scale(pygame.image.load('docs/imagens/Jogar2.png'),(205,85))
        self.rect_inicio_maior = pygame.Rect(400,250,205,85)
        self.como_jogar=pygame.transform.scale(pygame.image.load('docs/imagens/Como jogar.png'),(150,50))
        self.rect_instrucoes=pygame.Rect(420,340,150,50)
        self.como_jogar_maior=pygame.transform.scale(pygame.image.load('docs/imagens/Como jogar.png'),(155,55))
        self.rect_instrucoes_maior=pygame.Rect(420,340,155,55)
        self.contador=0 

    def atualiza_estado_inicio(self):
        for event in pygame.event.get():
            if event.type== pygame.MOUSEBUTTONDOWN:
                self.pos = pygame.mouse.get_pos()
                if self.rect_inicio.collidepoint(self.pos) or self.rect_inicio_maior.collidepoint(self.pos):
                    self.jogo.tela_atual=2
                elif  self.rect_instrucoes.collidepoint(self.pos) or self.rect_instrucoes_maior.collidepoint(self.pos):
                    self.jogo.tela_atual=1
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        return True
    def desenha_Tela_Inicio(self):
        self.contador+=0.1
        if self.contador>=20:
            window.blit(self.imagem_fundo_maior,(0,0))
            window.blit(self.titulo_maior,(100,1))
            pygame.draw.rect(window,(0,0,0),self.rect_inicio_maior)
            window.blit(self.jogar_maior,(400,250))
            window.blit(self.como_jogar_maior,(420,340))
        else:
            window.blit(self.imagem_fundo,(0,0))
            pygame.draw.rect(window,(0,0,0),self.rect_inicio)
            window.blit(self.jogar,(400,250))
            window.blit(self.titulo,(100,1))
            window.blit(self.como_jogar,(420,340))
        if self.contador>=40:
            self.contador=0

class Instrucao:

    '''
    cria uma tela de instruções que desenha um png das instruções do jogo
    há a detecção do clique na setinha para voltar à tela inicial
    '''
    def __init__(self,jogo):
        self.jogo=jogo
        self.image=pygame.transform.scale(pygame.image.load('docs/imagens/instruções.png'),(1000,410))
        self.voltar=pygame.transform.scale(pygame.image.load('docs/imagens/voltar.pnng.png'),(25,25))
        self.voltar=pygame.transform.flip(self.voltar, True, False)
        self.voltar_rect=pygame.Rect(5,0,40,40)
    def atualiza_instrucao(self):
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif  event.type== pygame.MOUSEBUTTONDOWN:
                self.pos = pygame.mouse.get_pos()
                if self.voltar_rect.collidepoint(self.pos):
                    self.jogo.tela_atual=0
        return True 
    def desenha_instrucao(self):
        window.blit(self.image,(0,0))
        window.blit(self.voltar,(5,0))

class Tela_Game_Over:

    '''
    Cria uma tela game over, toca a música de game over e reinicia o jogo quando a tecla ENTER é apertada
    '''
    def __init__(self,jogo):
        self.jogo = jogo
        self.game_over = pygame.transform.scale(pygame.image.load('docs/imagens/gameover.png'),(1000,205))
        self.recomecar = pygame.transform.scale(pygame.image.load('docs/imagens/Recomecar.png'),(800,205))
        self.music=pygame.mixer.Sound('docs/sons/game_over_bad_chest.wav')
        self.play=False 
    def atualiza_estado_over(self):
        pygame.mixer.music.stop()
        if not self.play:
            self.music.play()
            self.play=True
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.jogo.jogador.vidas <=0:
                    return False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        return True
    def desenha_game_over(self):
        window.fill((246,246,246))
        window.blit(self.game_over,(0,0))
        window.blit(self.recomecar,(100,206))

class Tela_ganhou:

    '''
    Cria uma tela ganhou que imprime a imagem 'you win' e toca a música de vitória
    '''
    def __init__(self,jogo):
        self.jogo = jogo
        self.image=pygame.transform.scale((pygame.image.load('docs/imagens/tela-vitoria.png')),(1000,410)).convert_alpha()
        self.music = pygame.mixer.Sound('docs\sons\Cant Stop Winning.mp3')
        self.play = False
    def atualiza_estado_ganhou(self):
        pygame.mixer.music.stop()
        if not self.play:
            self.music.play()
            self.play=True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        return True
    
    def desenha_ganhou(self):
        window.fill((0,0,0))
        window.blit(self.image,(0,0))


class Personagem(pygame.sprite.Sprite):
   
    '''
    cria o personagem do jogo, como um sprite,recebe a fonte que desenha o número de vidas e classe jogo
    possui os sons de pulo e pegar coin 
    '''

    def __init__(self,fonte,jogo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale((pygame.image.load('docs/imagens/personagem.png')),(50,50)).convert_alpha()
        self.velocidade_x = 0
        self.rect=self.image.get_rect(bottomright=(window.get_width()//2, 360))
        self.vidas =5
        self.jogo=jogo
        self.group=pygame.sprite.GroupSingle(self)
        self.font = pygame.font.Font('docs/fontes/PressStart2P.ttf', 20)
        self.colide=False 
        self.maximo=360
        self.gravidade=0
        self.fonte=fonte
        self.direcao=0
        self.pula= pygame.mixer.Sound('docs/sons/jump.wav')
        pygame.mixer.Sound.set_volume(self.pula,0.5)
        self.inverteu = False
        self.monstro_morre = pygame.mixer.Sound('docs/sons/MonstroMorre.wav')
        pygame.mixer.Sound.set_volume(self.monstro_morre,0.5)
        self.pega_coin= pygame.mixer.Sound('docs/sons/pegacoin.wav')
        pygame.mixer.Sound.set_volume(self.pega_coin,0.8)
        self.movimentação_monstro=0


    def movimenta_jogador(self,tela):

        '''
        recebe eventos enquanto o jogo está nas fases, faz a movimentação (andar para direita, esquerda e pular com funionalidade de gravidade).
        a váriavel inverteu serve para inverter a imagem do personagem, dando a impressão de que ele muda de direção. 
        '''
        clock = pygame.time.Clock()
        clock.tick(80)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_d, pygame.K_RIGHT):
                    self.velocidade_x +=8
                    self.direcao='direita'
                    if self.inverteu:
                        self.image = pygame.transform.flip(self.image, True, False)
                        self.inverteu = False
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    self.velocidade_x+= -8
                    self.direcao='esquerda'
                    if not self.inverteu:
                        self.image = pygame.transform.flip(self.image, True, False)
                        self.inverteu = True
                elif event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w) and (self.rect.bottom>=360 or self.colide==True):
                        self.gravidade=-15
                        self.pula.play()
                elif event.key == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    self.velocidade_x += 8
                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    self.velocidade_x += -8
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if (tela.imprime_x<=-2000 and (self.direcao=='direita' or self.rect.x>=window.get_width()//2)) or (tela.imprime_x>=0 and (self.direcao=='esquerda'or self.rect.x<=window.get_width()//2)):
            self.rect.x += self.velocidade_x
            '''
        quando o jogador chega nas extremidades da tela, o imprime_x se mantem fixo e o rect do personagem passa a mudar, isso evita que o jogo imprima uma parte da imagem que não
        existe.
            '''
        else:
            '''
            imprime_x é uma variável que altera a posição do blit da imagem de fundo do jogo e dá a impressão de que a tela anda em relação ao jogador.
            nesse caso, é necessário alterar a posição dos outros objetos, como por exemplo monstros, plataformas, bolinhas e plantas.
            os monstros também possuem uma movimentação independente do player.
            a colisão com monstros também foi adicionada, caso haja colisão o monstro morre e apenas quando a colisão é do topo do retangulo do monstro com a parte de baixo
            do retangulo do jogador, o personagem não perde vida (ou seja, para não perder vida é preciso pular em cima do monstro)
            quando o jogador sai pela direita da tela e possui as moedas necessárias para passar de nível a self.tela_atual e self.contador_tela são alterados.
            Tela atual é uma variável que diferencia as telas das fases para as telas de game over, início e vitória
            Contador tela é o índice da lista de telas
            Além da colisão com monstros, as colisões com bolinhas, plantas e coins são detectadas.
            '''
            tela.imprime_x -= self.velocidade_x
            for monstro in tela.grupo_monstro:
                monstro.rect.x -= self.velocidade_x
            for plataforma in tela.plataformaGroup:
                plataforma.rect.x-=self.velocidade_x
            for coin in tela.coinGroup:
                coin.rect.x-=self.velocidade_x
            for planta in tela.plantaGroup:
                planta.rect.x-=self.velocidade_x
            for bolinha in tela.bolinhaGroup:
                bolinha.rect.x-=self.velocidade_x
            for chao in tela.chaoGroup:
                chao.rect.x-=self.velocidade_x
        for monstro in tela.grupo_monstro:
            self.movimentação_monstro+=0.05
            if self.movimentação_monstro>=10:
                monstro.rect.x+=2
            else:
                monstro.rect.x-=2
            if self.movimentação_monstro>=20:
                self.movimentação_monstro=0
            if monstro.rect.colliderect(self.rect):
                self.vidas -= 1
                monstro.kill()
                self.monstro_morre.play()
                coin= Coin(monstro.rect.x,monstro.rect.y)
                tela.coinGroup.add(coin)
                if self.maximo <= monstro.rect.top :
                    self.vidas += 1
                    self.gravidade = -20
                    self.pula.play()
        
        for coin in tela.coinGroup:
            if coin.rect.colliderect(self.rect):
                self.pega_coin.play()
                tela.contador_coin+=1
                coin.kill()
        
        for bolinha in tela.bolinhaGroup:
            if bolinha.rect.colliderect(self.rect):
                bolinha.kill()
                self.vidas-=1
    
        for planta in tela.plantaGroup: 
            if planta.rect.colliderect(self.rect):
                if self.maximo <= planta.rect.top:
                    self.gravidade = -20
                    self.pula.play()
                    planta.kill()
        
        if self.rect.x>=1001 and tela.contador_coin>=10 and self.jogo.contador_tela == 0:
            self.jogo.contador_tela=1
            self.rect.x=0
        if self.rect.x >= 1001 and tela.contador_coin >= 15 and self.jogo.contador_tela == 1:
            self.jogo.contador_tela = 2
            self.rect.x = 0
        if self.rect.x >= 1001 and tela.contador_coin >= 20 and self.jogo.contador_tela == 2:
            self.jogo.contador_tela = 3
            self.rect.x = 0
        if self.rect.x >= 1001 and tela.contador_coin >= 25 and self.jogo.contador_tela == 3:
            self.jogo.tela_atual = 7
        return True
    
    def desenha_jogador(self,tela):
        self.coracao = self.fonte.render(chr(9829)*self.vidas,True,(255,0,0))
        window.blit(self.coracao,(0,0))
        self.gravidade+=0.8
        self.rect.y+=self.gravidade
        if self.rect.bottom>=360:
            self.rect.bottom=360
            self.maximo=360
        if self.rect.bottom<self.maximo:
            self.maximo=self.rect.bottom
        for plataforma in tela.plataformaGroup:
            '''
            quando o jogador pula e a altura da parte de baixo do seu retângulo é maior ou igual que a altura da plataforma ele para em cima dela
            '''
            plataforma_group= pygame.sprite.GroupSingle(plataforma)
            if pygame.sprite.spritecollide(self.group.sprite,plataforma_group,False,pygame.sprite.collide_mask) and self.gravidade>=0 and self.maximo<=plataforma.rect.top:
                self.rect.bottom=plataforma.rect.top+10
                self.maximo=plataforma.rect.top-10
                self.gravidade=0
                self.colide=True 
                break
            else:
                self.colide=False
        window.blit(self.image,self.rect)
        
class Jogo:
    '''
    classe jogo contém o game loop e chama as funções e métodos das telas do jogo. A classe inicializa o pygame, a fonte e toca a música principal
    cria uma lista de telas com as telas das diferentes fases
    '''
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Four Seasons Odyssey')
        self.tela_atual = 0
        self.telas=[]
        self.font = pygame.font.Font('docs/fontes/PressStart2P.ttf', 20)
        self.window_largura=window.get_width()
        self.telas.append(tela_inverno.Tela_Inverno(self.font))
        self.telas.append(tela_primavera.Tela_Primavera(self.font))
        self.telas.append(tela_verao.Tela_Verao(self.font))
        self.telas.append(tela_outono.Tela_Outono(self.font))
        self.jogador = Personagem(self.font,self)
        self.tela_inicio=Tela_Inicio(self)
        self.tela_game_over=Tela_Game_Over(self)
        self.tela_instrucao=Instrucao(self)
        self.tela_ganhou = Tela_ganhou(self)
        self.inverteu = False
        self.tocou = False
        self.fechou = False
        self.contador_tela=0
        pygame.mixer_music.load('docs/sons/game_music.wav')
        pygame.mixer_music.play(1000000000)

    def atualiza_estado(self): 
        '''
        Para cada tipo de tela há um atualiza estado, game over, início e ganhou possuem essas funções dentro da classe, mas para as fases do jogo, utiliza-se 
        o movimenta jogador da classe personagem
        '''
        if self.jogador.vidas <= 0:
            self.tela_atual = 6
        if self.tela_atual == 6:
            return self.tela_game_over.atualiza_estado_over()
        elif self.tela_atual==1:
            return self.tela_instrucao.atualiza_instrucao()
        elif self.tela_atual == 0:
            return self.tela_inicio.atualiza_estado_inicio()
        elif self.tela_atual == 2:
            return self.jogador.movimenta_jogador(self.telas[self.contador_tela])
        elif self.tela_atual == 7:
            return self.tela_ganhou.atualiza_estado_ganhou()
        

    def desenha_inicio(self):
        '''
        cada função possui a sua própria função 'desenha' e ela é chamada de acordo com a tela atual do jogo
        '''
        if self.tela_atual==2:
            self.telas[self.contador_tela].desenha_tela()
            self.telas[self.contador_tela].desenha_personagens()   
            self.jogador.desenha_jogador(  self.telas[self.contador_tela])
        elif self.tela_atual==0:
           self.tela_inicio.desenha_Tela_Inicio()
        elif self.tela_atual == 6:
            self.tela_game_over.desenha_game_over() 
        elif self.tela_atual==1:
            self.tela_instrucao.desenha_instrucao()
        elif self.tela_atual == 7:
            self.tela_ganhou.desenha_ganhou()
        pygame.display.update()

    def loop(self):
        '''
        loop chama atualiza estado e desenha enquanto atualiza estado não retornar False ou receber quit
        '''
        while self.atualiza_estado():
            self.desenha_inicio()
        
