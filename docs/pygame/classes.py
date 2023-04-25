import copy
import pygame
import random
class Plataforma(pygame.sprite.Sprite):
    def __init__(self,tela,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(pygame.image.load('docs/imagens/plataforma.png'),(150,50)).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.plataforma_altura=self.image.get_height()
        self.plataforma_largura=self.image.get_width()
        self.tela=tela

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
        self.imagem = pygame.image.load('docs/imagens/Inverno_att.png').convert_alpha()
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
        i=0
        while i<5:
            posicao_x = random.randint(0, 2450)
            posicao_y = random.randint(200,250)
            plataforma=Plataforma(self.imagem,posicao_x,posicao_y)
            if not pygame.sprite.spritecollide(plataforma, self.plataformaGroup, False, pygame.sprite.collide_mask):
                i+=1
                self.plataformaGroup.add(plataforma)

    def desenha_tela(self):
        self.window.blit(self.imagem,(self.imprime_x,0))
        for arvore in self.arvores:
            self.imagem.blit(self.arvore,(arvore[0],arvore[1]))
        self.plataformaGroup.draw(self.window)

class Personagem(pygame.sprite.Sprite):
   
    def __init__(self,window,tela):
        pygame.sprite.Sprite.__init__(self)
        self.platafroma_image=pygame.transform.scale(pygame.image.load('docs/imagens/plataforma.png'),(150,50)).convert_alpha()
        self.image = pygame.transform.scale((pygame.image.load('docs/imagens/personagem.png')),(50,50)).convert_alpha()
        self.velocidade_x = 0
        self.ajuste = 0
        self.window = window
        self.rect=self.image.get_rect(bottomright=(self.window.get_width()//2, 360))
        self.tela=tela
        self.vidas = 3
        self.group=pygame.sprite.GroupSingle(self)
        self.mask=pygame.mask.from_surface(self.image)
        self.font = pygame.font.Font('docs/imagens/PressStart2P.ttf', 20)
        self.colide=False 
        self.maximo=360
        self.gravidade=0
    def desenha_jogador(self):
        self.coracao = self.font.render(chr(9829)*self.vidas,True,(255,0,0))
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
            print(jogador.vidas)
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
        self.window_largura=self.window.get_width()
        self.tela=Tela_Inverno(self.window)
        self.chao=Chao(self.tela.imagem)
        self.jogador = Personagem(self.window,self.tela)
        self.tela_inicio=Tela_Inicio(self.window)
        self.direcao=0
        self.tela_atual=0
        self.grupo_monstro= pygame.sprite.Group()
        self.lista_monstro = []
        for i in range(5):
            self.grupo_monstro.add(Monstro())

    def atualiza_estado(self):
        clock = pygame.time.Clock()
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.jogador.velocidade_x +=8
                    self.direcao='direita'
                    # self.monstro.velocidade -= self.jogador.velocidade_x//2
                elif event.key == pygame.K_LEFT:
                    self.jogador.velocidade_x+= -8
                    self.direcao='esquerda'
                    # self.monstro.velocidade += self.jogador.velocidade_x//2
                elif event.key in (pygame.K_SPACE, pygame.K_UP) and self.jogador.rect.bottom>=360:
                        self.jogador.gravidade=-15
                elif event.key==pygame.K_RETURN:
                    self.tela_atual=1
            elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.jogador.velocidade_x+=8
                    elif event.key == pygame.K_RIGHT:
                        self.jogador.velocidade_x += -8
                        # self.monstro.velocidade += self.jogador.velocidade_x//2
        if (self.tela.imprime_x<=-2000 and (self.direcao=='direita' or self.jogador.rect.x>=self.window.get_width()//2)) or (self.tela.imprime_x>=0 and (self.direcao=='esquerda' or self.jogador.rect.x<=self.window.get_width()//2 )):
            self.jogador.rect.x+=self.jogador.velocidade_x
        else:
            self.tela.imprime_x -= self.jogador.velocidade_x
            for monstro in self.grupo_monstro:
                monstro.rect.x -= self.jogador.velocidade_x
            for plataforma in self.tela.plataformaGroup:
                plataforma.rect.x-=self.jogador.velocidade_x
        for monstro in self.grupo_monstro:
            if monstro.combate(self.jogador,self,self.tela,self.window, self.grupo_monstro):
                monstro.kill()
                if self.jogador.rect.bottom <= monstro.rect.top :
                    self.jogador.vidas += 1
                for monstrengo in self.grupo_monstro:
                    monstrengo.rect.x += self.jogador.velocidade_x
            # else: 
            #     print(monstro.rect)
        return True

    def desenha_inicio(self):
        if self.tela_atual==1:
            self.tela.desenha_tela()
            self.chao.desenha_chao()
            self.jogador.desenha_jogador()
            self.grupo_monstro.draw(self.window)
        elif self.tela_atual==0:
           self.tela_inicio.desenha_Tela_Inicio()
        pygame.display.update()

    def loop(self):
        while self.atualiza_estado():
            self.desenha_inicio()            
        

    