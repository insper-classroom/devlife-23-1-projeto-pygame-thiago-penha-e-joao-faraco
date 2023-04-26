import copy
import pygame
import random

class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(pygame.image.load('docs/imagens/coin_2.png'),(25,25)).convert_alpha()
        self.contador=pygame.transform.scale(pygame.image.load('docs/imagens/coin_2.png'),(50,50)).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
    
class Plataforma(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(pygame.image.load('docs/imagens/plataforma.png'),(150,50)).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

class Chao(pygame.sprite.Sprite):
    def __init__(self,tela):
        pygame.sprite.Sprite.__init__(self)
        self.chao=pygame.transform.scale(pygame.image.load('docs/imagens/chao inverno.png'),(50,50))
        self.chao_rect=self.chao.get_rect()
        self.chao_altura=self.chao.get_height()
        self.chao_largura=self.chao.get_width()
        self.quantidade= tela.get_width()//self.chao_largura
        self.tela=tela 
    def desenha_chao(self):
        for i in range(self.quantidade+1):
            self.tela.blit(self.chao,(i*self.chao_largura,360))
                          
class Tela_Inicio:
    def __init__(self,window):
        self.window=window
        self.imagem_fundo = pygame.transform.scale(pygame.image.load('docs\imagens\seasons.webp'),(1000,410))
        self.titulo = pygame.transform.scale(pygame.image.load('docs\imagens\otitulo.png'),(800,90))
        self.jogar = pygame.transform.scale(pygame.image.load('docs\imagens\Jogar2.png'),(200,80))
        self.rect_inicio = pygame.Rect(400,250,200,80)
    def desenha_Tela_Inicio(self):
        self.window.blit(self.imagem_fundo,(0,0))
        self.window.blit(self.titulo,(100,10))
        # pygame.draw.rect(self.window,(255,255,255),self.rect_inicio)
        self.window.blit(self.jogar,(400,250))

class Tela_Game_Over:
    def __init__(self,window):
        self.window = window
        self.game_over = pygame.transform.scale(pygame.image.load('docs\imagens\gameover.png'),(1000,205))
        self.recomecar = pygame.transform.scale(pygame.image.load('docs\imagens\Recomecar.png'),(800,205))
    def desenha_game_over(self):
        self.window.fill((246,246,246))
        self.window.blit(self.game_over,(0,0))
        self.window.blit(self.recomecar,(100,206))

class Tela_Inverno(pygame.sprite.Sprite):
    
    def __init__(self,window,fonte):
        pygame.sprite.Sprite.__init__(self)
        
        self.imagem = pygame.image.load('docs/imagens/Inverno_att.png').convert_alpha()
        self.imagem= pygame.transform.scale(self.imagem,(3000,410))
        self.arvore=pygame.transform.scale(pygame.image.load('docs/imagens/Arvore_Inverno.png'),(100,100))
        self.moeda_contadora=pygame.transform.scale(pygame.image.load('docs/imagens/coin_2.png'),(50,50)).convert_alpha()
        self.imprime_x =0
        self.window=window    
        self.arvores=[]       
        self.plataformaGroup=pygame.sprite.Group()
        self.posicao_plat=[]
        self.coinGroup=pygame.sprite.Group()
        self.fonte=fonte
        self.contador=0
        for i in range(10):
            posicao_x = random.randint(0, 2470)
            self.arvores.append([posicao_x,260])
        i=0
        while i<8:
            posicao_x = random.randint(0, 2450)
            posicao_y = random.randint(150,250)
            plataforma=Plataforma(posicao_x,posicao_y)
            if not pygame.sprite.spritecollide(plataforma, self.plataformaGroup, False, pygame.sprite.collide_mask):
                i+=1
                self.plataformaGroup.add(plataforma)
        j=0
        while j<10:
            posicao_x = random.randint(0, 2450)
            posicao_y = random.randint(100,330)
            coin=Coin(posicao_x,posicao_y)
            if not pygame.sprite.spritecollide(coin, self.coinGroup, False, pygame.sprite.collide_mask) and not pygame.sprite.spritecollide(coin, self.plataformaGroup, False, pygame.sprite.collide_mask):
                j+=1
                self.coinGroup.add(coin)

    def desenha_tela(self):
        self.window.blit(self.imagem,(self.imprime_x,0))
        for arvore in self.arvores:
            self.imagem.blit(self.arvore,(arvore[0],arvore[1]))
        self.plataformaGroup.draw(self.window)
        self.coinGroup.draw(self.window)
        self.window.blit(self.moeda_contadora,(900,20))
        self.contador_imagem=self.fonte.render(str(self.contador),True,(0,0,0))
        self.window.blit(self.contador_imagem,(960,35))
class Personagem(pygame.sprite.Sprite):
   
    def __init__(self,window,tela,fonte):
        pygame.sprite.Sprite.__init__(self)
        self.platafroma_image=pygame.transform.scale(pygame.image.load('docs/imagens/plataforma.png'),(150,50)).convert_alpha()
        self.image = pygame.transform.scale((pygame.image.load('docs/imagens/personagem.png')),(50,50)).convert_alpha()
        self.mask=pygame.mask.from_surface(self.image)
        self.velocidade_x = 0
        self.ajuste = 0
        self.window = window
        self.rect=self.image.get_rect(bottomright=(self.window.get_width()//2, 360))
        self.tela=tela
        self.vidas = 3
        self.group=pygame.sprite.GroupSingle(self)
        self.mask=pygame.mask.from_surface(self.image)
        self.font = pygame.font.Font('docs/fontes/PressStart2P.ttf', 20)
        self.colide=False 
        self.maximo=360
        self.gravidade=0
        self.fonte=fonte
    def desenha_jogador(self):
        self.coracao = self.fonte.render(chr(9829)*self.vidas,True,(255,0,0))
        self.window.blit(self.coracao,(0,0))
        self.gravidade+=0.8
        self.rect.y+=self.gravidade
        if self.rect.bottom>=360:
            self.rect.bottom=360
            self.maximo=360
        if self.rect.bottom<self.maximo:
            self.maximo=self.rect.bottom
        for plataforma in self.tela.plataformaGroup:
            plataforma_mask=pygame.mask.from_surface(self.platafroma_image)
            plataforma_group= pygame.sprite.GroupSingle(plataforma)
            if pygame.sprite.spritecollide(self.group.sprite,plataforma_group,False,pygame.sprite.collide_mask) and self.gravidade>=0 and self.maximo<=plataforma.rect.top:
                self.rect.bottom=plataforma.rect.top+10
                self.maximo=plataforma.rect.top-10
                self.gravidade=0
                self.colide=True 
                break
            else:
                self.colide=False
        self.window.blit(self.image,self.rect)
        
class Monstro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tick=0
        self.image = pygame.transform.scale(pygame.image.load('docs/imagens/monstroatt.png'),(50,50))
        self.rect = self.image.get_rect()
        self.rect.y = 310
        self.rect.x = random.randint(50,2950)
        
    def combate(self,jogador, jogo,tela,window,grupo_monstro):
        if self.rect.colliderect(jogador.rect):
            # if jogador.vidas>0:
            jogador.vidas -= 1
            if (tela.imprime_x<=-2000 and (jogo.direcao=='direita' or jogador.rect.x>=window.get_width()//2)) or (tela.imprime_x>=0 and (jogo.direcao=='esquerda' or jogador.rect.x<=window.get_width()//2 )):
                jogador.rect.x -= jogador.velocidade_x 
                for monstrin in grupo_monstro:
                    monstrin.rect.x -= jogador.velocidade_x
            else:
                tela.imprime_x += jogador.velocidade_x
            return True
        return False

class Jogo:
    
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1000,409))
        pygame.display.set_caption('JOGO DO JUCA JUCA JUCA JUCA JUCA JUCA JUCA')

        self.font = pygame.font.Font('docs/fontes/PressStart2P.ttf', 20)
        self.window_largura=self.window.get_width()
        self.tela=Tela_Inverno(self.window,self.font)
        self.chao=Chao(self.tela.imagem)
        self.jogador = Personagem(self.window,self.tela,self.font)
        self.tela_inicio=Tela_Inicio(self.window)
        self.direcao=0
        self.tela_atual=0
        self.grupo_monstro= pygame.sprite.Group()
        self.lista_monstro = []
        self.inverteu = False
        self.tocou = False
        self.tela_game_over = Tela_Game_Over(self.window)
        self.game_over = False
        self.monstro_morre = pygame.mixer.Sound('docs\sons\MonstroMorre.wav')
        for i in range(5):
            self.grupo_monstro.add(Monstro())
        pygame.mixer_music.load('docs\sons\game_music.wav')
        pygame.mixer_music.set_volume(0.2)
        pygame.mixer_music.play(1000000000)

    def atualiza_estado(self):
        clock = pygame.time.Clock()
        clock.tick(80)
        if self.jogador.vidas <= 0:
            self.tela_atual = 2
            self.game_over = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.jogador.velocidade_x +=8
                    self.direcao='direita'
                    if self.inverteu:
                        self.jogador.image = pygame.transform.flip(self.jogador.image, True, False)
                        self.inverteu = False
                elif event.key == pygame.K_LEFT:
                    self.jogador.velocidade_x+= -8
                    self.direcao='esquerda'
                    if not self.inverteu:
                        self.jogador.image = pygame.transform.flip(self.jogador.image, True, False)
                        self.inverteu = True
                elif event.key == pygame.K_RETURN and self.game_over:
                    self.tela_atual = 1
                    self.game_over = False
                    self.jogador.vidas = 3
                    game = Jogo()
                elif event.key in (pygame.K_SPACE, pygame.K_UP) and (self.jogador.rect.bottom>=360 or self.jogador.colide==True):
                        self.jogador.gravidade=-15
            elif event.type== pygame.MOUSEBUTTONDOWN:
                self.pos = pygame.mouse.get_pos()
                if self.tela_inicio.rect_inicio.collidepoint(self.pos):
                    self.tela_atual=1
            elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.jogador.velocidade_x+=8
                    elif event.key == pygame.K_RIGHT:
                        self.jogador.velocidade_x += -8
        if (self.tela.imprime_x<=-2000 and (self.direcao=='direita' or self.jogador.rect.x>=self.window.get_width()//2)) or (self.tela.imprime_x>=0 and (self.direcao=='esquerda' or self.jogador.rect.x<=self.window.get_width()//2 )):
            self.jogador.rect.x+=self.jogador.velocidade_x
        else:
            self.tela.imprime_x -= self.jogador.velocidade_x
            for monstro in self.grupo_monstro:
                monstro.rect.x -= self.jogador.velocidade_x
            for plataforma in self.tela.plataformaGroup:
                plataforma.rect.x-=self.jogador.velocidade_x
            for coin in self.tela.coinGroup:
                coin.rect.x-=self.jogador.velocidade_x
        
        for monstro in self.grupo_monstro:
            if monstro.combate(self.jogador,self,self.tela,self.window, self.grupo_monstro):
                coin= Coin(monstro.rect.x,monstro.rect.y)
                monstro.kill()
                self.monstro_morre.play()
                self.tela.coinGroup.add(coin)
                if self.jogador.maximo <= monstro.rect.top :
                    self.jogador.vidas += 1
                    self.jogador.gravidade = -20
                for monstrengo in self.grupo_monstro:
                    monstrengo.rect.x += self.jogador.velocidade_x
        for coin in self.tela.coinGroup:
            if coin.rect.colliderect(self.jogador.rect):
                self.tela.contador+=1
                coin.kill()
        return True

    def desenha_inicio(self):
        if self.tela_atual==1:
            self.tela.desenha_tela()
            self.chao.desenha_chao()
            self.jogador.desenha_jogador()
            self.grupo_monstro.draw(self.window)     
        elif self.tela_atual==0:
           self.tela_inicio.desenha_Tela_Inicio()
        elif self.tela_atual == 2:
            self.tela_game_over.desenha_game_over()
        pygame.display.update()

    def loop(self):
        while self.atualiza_estado():
            self.desenha_inicio()
        

