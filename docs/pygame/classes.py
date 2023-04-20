import pygame
import random
class Plataforma(pygame.sprite.Sprite):
    def __init__(self,tela,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(pygame.image.load('docs/imagens/plataforma.png'),(150,50))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.plataforma_altura=self.image.get_height()
        self.plataforma_largura=self.image.get_width()
        self.tela=tela
        self.mask = pygame.mask.from_surface(self.image)

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
    def desenha_Tela_Inicio(self):
        self.window.fill((0,0,0))

class Tela_Inverno(pygame.sprite.Sprite):
    
    def __init__(self,window):
        pygame.sprite.Sprite.__init__(self)
        self.imagem = pygame.image.load('docs/imagens/Inverno_att.png')
        self.imagem= pygame.transform.scale(self.imagem,(3000,410))
        self.arvore=pygame.transform.scale(pygame.image.load('docs/imagens/Arvore_Inverno.png'),(100,100))
        self.imprime_x =0
        self.window=window
        self.arvores=[]       
        self.plataformaGroup=pygame.sprite.Group()
        self.posicao_plat=[]
        for i in range(10):
            posicao_x = random.randint(0, 2470)
            self.arvores.append([posicao_x,260])
        for i in range(5):
            posicao_x = random.randint(0, 2450)
            posicao_y = random.randint(200, 250)
            plataforma=Plataforma(self.imagem,posicao_x,posicao_y)
            for sprite in self.plataformaGroup:
                if pygame.sprite.collide_mask(sprite,plataforma) == None:
                    self.plataformaGroup.add(plataforma)
            if len(self.plataformaGroup)==0:
                self.plataformaGroup.add(plataforma)
    
    def desenha_tela(self):
        self.window.blit(self.imagem,(self.imprime_x,0))
        for arvore in self.arvores:
            self.imagem.blit(self.arvore,(arvore[0],arvore[1]))
        self.plataformaGroup.draw(self.imagem)

class Personagem(pygame.sprite.Sprite):
   
    def __init__(self,window,tela):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale((pygame.image.load('docs/imagens/personagem.png')),(50,50))
        self.velocidade_x = 0
        self.ajuste = 0
        self.window = window
        self.rect=self.image.get_rect(bottomright=(self.window.get_width()//2, 360))
        self.gravidade=0
        self.tela=tela
        self.inverno=Tela_Inverno(self.window)
        #self.plataforma=Plataforma(self.tela)
        self.mask=pygame.mask.from_surface(self.image)

    def desenha_jogador(self):
        self.gravidade+=0.8
        self.rect.y+=self.gravidade
        if self.rect.bottom>=360:
            self.rect.bottom=360
        #for sprite in self.inverno.plataformaGroup.sprites():
            #if pygame.sprite.collide_mask(self,sprite)!=None:  
             #   self.rect.bottom=sprite.rect.top
        self.window.blit(self.image,self.rect)
        
class Jogo:
    
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1000,409))
        self.window_largura=self.window.get_width()
        self.tela=Tela_Inverno(self.window)
        self.chao=Chao(self.tela.imagem)
        self.jogador = Personagem(self.window,self.tela)
        self.tela_inicio=Tela_Inicio(self.window)
        self.direção=0
        self.tela_atual=0
        
    
    def atualiza_estado(self):
        clock = pygame.time.Clock()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.jogador.velocidade_x +=10
                    self.direção='direita'
                elif event.key == pygame.K_LEFT:
                    self.jogador.velocidade_x-=10
                    self.direção='esquerda'
                elif event.key==pygame.K_SPACE and self.jogador.rect.bottom>=360:
                        self.jogador.gravidade=-15
                elif event.key==pygame.K_RETURN:
                    self.tela_atual=1
            elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.jogador.velocidade_x+=10
                    elif event.key == pygame.K_RIGHT:
                        self.jogador.velocidade_x -=10
        if (self.tela.imprime_x<=-2000 and (self.direção=='direita' or self.jogador.rect.x>=self.window.get_width()//2)) or (self.tela.imprime_x>=0 and (self.direção=='esquerda' or self.jogador.rect.x<=self.window.get_width()//2 )):
            self.jogador.rect.x+=self.jogador.velocidade_x
        else:
            self.tela.imprime_x -= self.jogador.velocidade_x 
        clock.tick(80)
        return True

    def desenha_inicio(self):
        if self.tela_atual==1:
            self.tela.desenha_tela()
            self.chao.desenha_chao()
            self.jogador.desenha_jogador()
        elif self.tela_atual==0:
           self.tela_inicio.desenha_Tela_Inicio()
        pygame.display.update()

    def loop(self):
        while self.atualiza_estado():
            self.desenha_inicio()
        

    