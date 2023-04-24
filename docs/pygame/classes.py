import copy
import pygame
import random
class Plataforma(pygame.sprite.Sprite):
    def __init__(self,tela):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(pygame.image.load('docs/imagens/plataforma.png'),(150,50))
        self.plataforma_altura=self.image.get_height()
        self.plataforma_largura=self.image.get_width()
        self.tela=tela
        self.plataformas=[]
        self.group=pygame.sprite.Group()
        i=0
        while i <5:
            posicao_x = random.randint(0, 2450)
            posicao_y = random.randint(200, 309)
            self.rect = self.image.get_rect(topleft=(posicao_x, posicao_y))
            self.group.add(self)
            #if not pygame.sprite.spritecollide(self,self.group,False):
            self.plataformas.append([posicao_x, posicao_y])
            i+=1
        self.plataformas.append([50, 50])


    def desenha_plataforma(self):
        for plataforma in self.plataformas:
            self.tela.blit(self.image,(plataforma[0],plataforma[1]))                

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

class Tela_Inverno:
    def __init__(self,window):
        pygame.init()
        self.imagem = pygame.image.load('docs/imagens/Inverno_att.png')
        # self.imagem_zerada = pygame.transform.scale(pygame.image.load('docs/imagens/Inverno_att.png'),(3000,410))
        self.imagem= pygame.transform.scale(self.imagem,(3000,410))
        self.arvore=pygame.transform.scale(pygame.image.load('docs/imagens/Arvore_Inverno.png'),(100,100))
        self.imprime_x =0
        self.window=window
        self.arvores=[]      

        for i in range(10):
            posicao_x = random.randint(0, 2470)
            self.arvores.append([posicao_x,260])

    def desenha_tela(self):
        #self.imagem.blit(self.imagem_zerada,(self.imprime_x,0))
        # self.imagem.blit(self.imagem_zerada,(0,0))
        for arvore in self.arvores:
            self.imagem.blit(self.arvore,(arvore[0],arvore[1]))
        self.window.blit(self.imagem,(self.imprime_x,0))


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
        self.plataforma=Plataforma(self.tela)
    def desenha_jogador(self):
        self.gravidade+=0.05
        self.rect.y+=self.gravidade
        if self.rect.bottom>=360:
            self.rect.bottom=360
        for sprite in self.plataforma.group.sprites():
            if pygame.sprite.collide_rect(self,sprite):  
                print('colidiu')
                self.rect.bottom=sprite.rect.top
        self.window.blit(self.image,self.rect)
        
class Monstro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tick=0
        self.image = pygame.transform.scale(pygame.image.load('docs\imagens\monstroatt.png'),(50,50))
        self.rect = self.image.get_rect()
        self.rect.y = 310
        self.rect.x = random.randint(50,2950)

    def movimenta_monstro(self):
        self.tick+=1
        if self.tick%5==0:
            self.movimento = random.randint(0,2)
            if self.movimento == 1:
                # self.rect = self.rect.move(1,0)
                self.rect.update(self.rect.x - 2,self.rect.y,50,50)
                print(self.rect)
            elif self.movimento == 2:
                self.rect.update(self.rect.x - 2,self.rect.y,50,50)
                print(self.rect)
class Jogo:
    def __init__(self):
        self.window = pygame.display.set_mode((1000,409))
        self.window_largura=self.window.get_width()
        self.tela=Tela_Inverno(self.window)
        self.chao=Chao(self.tela.imagem)
        self.jogador = Personagem(self.window,self.tela)
        self.tela_inicio=Tela_Inicio(self.window)
        self.plataforma=Plataforma(self.tela.imagem)
        self.direção=0
        self.tela_atual=0
        self.grupo_monstro= pygame.sprite.Group()
        self.lista_monstro = []
        for i in range(1):
            self.grupo_monstro.add(Monstro())
            print('gerou')            
    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.jogador.velocidade_x +=2
                    self.direção='direita'
                elif event.key == pygame.K_LEFT:
                    self.jogador.velocidade_x-=2
                    self.direção='esquerda'
                elif event.key==pygame.K_SPACE and self.jogador.rect.bottom>=360:
                        self.jogador.gravidade=-4
                elif event.key==pygame.K_RETURN:
                    self.tela_atual=1
            elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.jogador.velocidade_x+=2
                    elif event.key == pygame.K_RIGHT:
                        self.jogador.velocidade_x -=2
            for monstro in self.grupo_monstro:
                monstro.rect.x -= self.jogador.velocidade_x
        if (self.tela.imprime_x<=-2000 and (self.direção=='direita' or self.jogador.rect.x>=self.window.get_width()//2)) or (self.tela.imprime_x>=0 and (self.direção=='esquerda' or self.jogador.rect.x<=self.window.get_width()//2 )):
            self.jogador.rect.x+=self.jogador.velocidade_x
        else:
            self.tela.imprime_x -= self.jogador.velocidade_x 
        for monstro in self.grupo_monstro:
            monstro.movimenta_monstro()
        return True

    def desenha_inicio(self):
        if self.tela_atual==1:
            self.tela.desenha_tela()
            self.chao.desenha_chao()
            self.plataforma.desenha_plataforma()
            self.jogador.desenha_jogador()
            self.grupo_monstro.draw(self.window)
        elif self.tela_atual==0:
           self.tela_inicio.desenha_Tela_Inicio()
        pygame.display.update()

    def loop(self):
        while self.atualiza_estado():
            self.desenha_inicio()            
        

    