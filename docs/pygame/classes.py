import pygame
import random

window = pygame.display.set_mode((1000,409))

class Bolinha(pygame.sprite.Sprite):   
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(pygame.image.load('docs/imagens/bolinha.png'),(20,20)).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

class Planta(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(pygame.image.load('docs/imagens/Planta.png'),(50,50)).convert_alpha()
        self.image=pygame.transform.flip(self.image, True, False)
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

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
        window=window
        self.imagem_fundo = pygame.transform.scale(pygame.image.load('docs/imagens/seasons.webp'),(1000,410))
        self.titulo = pygame.transform.scale(pygame.image.load('docs/imagens/otitulo.png'),(800,90))
        self.jogar = pygame.transform.scale(pygame.image.load('docs/imagens/Jogar2.png'),(200,80))
        self.rect_inicio = pygame.Rect(400,250,200,80)
    def desenha_Tela_Inicio(self):
        window.blit(self.imagem_fundo,(0,0))
        window.blit(self.titulo,(100,10))
        # pygame.draw.rect(window,(255,255,255),self.rect_inicio)
        window.blit(self.jogar,(400,250))

class Tela_Game_Over:
    def __init__(self,window):
        window = window
        self.game_over = pygame.transform.scale(pygame.image.load('docs/imagens/gameover.png'),(1000,205))
        self.recomecar = pygame.transform.scale(pygame.image.load('docs/imagens/Recomecar.png'),(800,205))
    def desenha_game_over(self):
        window.fill((246,246,246))
        window.blit(self.game_over,(0,0))
        window.blit(self.recomecar,(100,206))

class Tela_Inverno(pygame.sprite.Sprite):
    
    def __init__(self,window,fonte):
        pygame.sprite.Sprite.__init__(self)
        
        self.imagem = pygame.transform.scale(pygame.image.load('docs/imagens/Inverno_att.png').convert_alpha(),(3000,410))
        self.arvore=pygame.transform.scale(pygame.image.load('docs/imagens/Arvore_Inverno.png'),(100,100))
        self.moeda_contadora=pygame.transform.scale(pygame.image.load('docs/imagens/coin_2.png'),(50,50)).convert_alpha()
        self.imprime_x=0
        window=window    
        self.arvores=[]       
        self.posicao_plat=[]
        self.fonte=fonte
        self.contador_coin=0
        self.frequenciadotiro=0
        self.plataformaGroup=pygame.sprite.Group()
        self.coinGroup=pygame.sprite.Group()
        self.grupo_monstro= pygame.sprite.Group()
        self.plantaGroup=pygame.sprite.Group()
        self.bolinhaGroup=pygame.sprite.Group()
        self.cria_arvore()
        self.cria_plat()
        self.cria_coin()
        self.cria_planta()
        self.cria_monstro()
    
    def desenha_bolinha(self):
        self.frequenciadotiro+=0.5
        if self.frequenciadotiro%50==0:
            for planta in self.plantaGroup:
                bolinha=Bolinha(planta.rect.x,planta.rect.y)
                self.bolinhaGroup.add(bolinha)
        for bolinha in self.bolinhaGroup:
            bolinha.rect.x-=3
        self.bolinhaGroup.draw(window)

    def cria_monstro(self):
        i=0
        while i<5:
            posicao_x = random.randint(0, 2450)
            posicao_y = 310
            monstro=Monstro(posicao_x,posicao_y)
            if not pygame.sprite.spritecollide(monstro, self.grupo_monstro, False, pygame.sprite.collide_mask):
                i+=1
                self.grupo_monstro.add(monstro)

    def cria_arvore(self):
        for i in range(10):
            posicao_x = random.randint(0, 2470)
            self.arvores.append([posicao_x,260])
    
    def cria_plat(self):
        i=0
        while i<8:
            posicao_x = random.randint(0, 2450)
            posicao_y = random.randint(150,250)
            plataforma=Plataforma(posicao_x,posicao_y)
            if not pygame.sprite.spritecollide(plataforma, self.plataformaGroup, False, pygame.sprite.collide_mask):
                i+=1
                self.plataformaGroup.add(plataforma)
    
    def cria_coin(self):
        j=0
        while j<10:
            posicao_x = random.randint(0, 2450)
            posicao_y = random.randint(100,330)
            coin=Coin(posicao_x,posicao_y)
            if not pygame.sprite.spritecollide(coin, self.coinGroup, False, pygame.sprite.collide_mask) and not pygame.sprite.spritecollide(coin, self.plataformaGroup, False, pygame.sprite.collide_mask):
                j+=1
                self.coinGroup.add(coin)

    def cria_planta(self):
         j=0
         while j<2:
            posicao_x = random.randint(1500, 2450)
            posicao_y = 310
            planta=Planta(posicao_x,posicao_y)
            if not pygame.sprite.spritecollide(planta, self.plantaGroup, False, pygame.sprite.collide_mask):
                self.plantaGroup.add(planta)
                j+=1


    def desenha_tela(self):
        window.blit(self.imagem,(self.imprime_x,0))
        for arvore in self.arvores:
            self.imagem.blit(self.arvore,(arvore[0],arvore[1]))
        window.blit(self.moeda_contadora,(900,20))
        self.contador_imagem=self.fonte.render(str(self.contador_coin),True,(0,0,0))
        window.blit(self.contador_imagem,(960,35))
    
    def desenha_personagens(self):
        self.plataformaGroup.draw(window)
        self.coinGroup.draw(window)
        self.plantaGroup.draw(window)
        self.grupo_monstro.draw(window)
        self.desenha_bolinha()
class Personagem(pygame.sprite.Sprite):
   
    def __init__(self,window,tela,fonte):
        pygame.sprite.Sprite.__init__(self)
        self.platafroma_image=pygame.transform.scale(pygame.image.load('docs/imagens/plataforma.png'),(150,50)).convert_alpha()
        self.image = pygame.transform.scale((pygame.image.load('docs/imagens/personagem.png')),(50,50)).convert_alpha()
        self.mask=pygame.mask.from_surface(self.image)
        self.velocidade_x = 0
        self.ajuste = 0
        window = window
        self.rect=self.image.get_rect(bottomright=(window.get_width()//2, 360))
        self.tela=tela
        self.vidas = 3
        self.group=pygame.sprite.GroupSingle(self)
        self.mask=pygame.mask.from_surface(self.image)
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
        self.fechou_no_jogo = False


    def movimenta_jogador(self,tela):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.velocidade_x +=8
                    self.direcao='direita'
                    if self.inverteu:
                        self.image = pygame.transform.flip(self.image, True, False)
                        self.inverteu = False
                elif event.key == pygame.K_LEFT:
                    self.velocidade_x+= -8
                    self.direcao='esquerda'
                    if not self.inverteu:
                        self.image = pygame.transform.flip(self.image, True, False)
                        self.inverteu = True
                elif event.key in (pygame.K_SPACE, pygame.K_UP) and (self.rect.bottom>=360 or self.colide==True):
                        self.gravidade=-15
                        self.pula.play()
                elif event.key == pygame.QUIT:
                    pygame.quit()
                    self.fechou_no_jogo = True
                    return False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.velocidade_x += 8
                elif event.key == pygame.K_RIGHT:
                    self.velocidade_x += -8
        if (tela.imprime_x<=-2000 and (self.direcao=='direita' or self.rect.x>=window.get_width()//2)) or (tela.imprime_x>=0 and (self.direcao=='esquerda' or self.rect.x<=window.get_width()//2 )):
            self.rect.x += self.velocidade_x
            
        else:
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
        
        for monstro in tela.grupo_monstro:
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
        if self.vidas <= 0:
            return 2
        return 1

    
    def desenha_jogador(self):
        self.coracao = self.fonte.render(chr(9829)*self.vidas,True,(255,0,0))
        window.blit(self.coracao,(0,0))
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
        window.blit(self.image,self.rect)
        
class Monstro(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.tick=0
        self.image = pygame.transform.scale(pygame.image.load('docs/imagens/monstroatt.png'),(50,50))
        self.rect = self.image.get_rect() 
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

class Jogo:
    global window
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Four Seasons Odyssey')
        self.font = pygame.font.Font('docs/fontes/PressStart2P.ttf', 20)
        self.window_largura=window.get_width()
        self.tela=Tela_Inverno(window,self.font)
        self.chao=Chao(self.tela.imagem)
        self.jogador = Personagem(window,self.tela,self.font)
        self.tela_inicio=Tela_Inicio(window)
        self.tela_game_over=Tela_Game_Over(window)
        self.tela_atual=0
        self.tocou = False
        self.fechou = False
        pygame.mixer_music.load('docs/sons/game_music.wav')
        pygame.mixer_music.play(1000000000)

    def atualiza_estado(self):
        clock = pygame.time.Clock()
        clock.tick(80)
 
        if self.tela_atual == 1:
            self.tela_atual = self.jogador.movimenta_jogador(self.tela)
            if self.tela_atual == False:
                pygame.quit()
                self.fechou = True
                return False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.fechou = True
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.jogador.vidas <=0:
                    return False
            if event.type== pygame.MOUSEBUTTONDOWN and self.tela_atual == 0:
                self.pos = pygame.mouse.get_pos()
                if self.tela_inicio.rect_inicio.collidepoint(self.pos):
                    self.tela_atual=1
        return True

    def desenha_inicio(self):
        if self.tela_atual==1:
            self.tela.desenha_tela()
            self.chao.desenha_chao()
            self.tela.desenha_personagens()   
            self.jogador.desenha_jogador()
        elif self.tela_atual==0:
           self.tela_inicio.desenha_Tela_Inicio()
        elif self.tela_atual == 2:
            self.tela_game_over.desenha_game_over()
        pygame.display.update()

    def loop(self):
        while self.atualiza_estado():
            self.desenha_inicio()
        

