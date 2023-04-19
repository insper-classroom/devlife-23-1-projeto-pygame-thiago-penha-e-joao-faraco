import pygame
import random
class Plataforma(pygame.sprite.Sprite):
    def __init__(self,window):
        pygame.sprite.Sprite.__init__(self)
        self.plataforma=pygame.transform.scale(pygame.image.load('docs/imagens/plataforma.png'),(100,50))
        self.plataforma_rect=self.plataforma.get_rect()
        self.plataforma_altura=self.plataforma.get_height()
        self.plataforma_largura=self.plataforma.get_width()
        self.window=window
        self.plataformas=[]
        for i in range(5):
            posicao_x=random.randint(0,2450)
            posicao_y=random.randint(200,309)
            self.plataformas.append([posicao_x,posicao_y])

    def desenha_plataforma(self):
            for plataforma in self.plataformas:
                self.window.blit(self.plataforma,(plataforma[0],plataforma[1]))

class Chao(pygame.sprite.Sprite):
    def __init__(self,window):
        pygame.sprite.Sprite.__init__(self)
        self.chao=pygame.transform.scale(pygame.image.load('docs/imagens/chao inverno.png'),(50,50))
        self.chao_rect=self.chao.get_rect()
        self.chao_altura=self.chao.get_height()
        self.chao_largura=self.chao.get_width()
        self.pontos={}
        self.quantidade=0
        self.quantidade+= window.get_width()//self.chao_largura
        self.window=window 
    def desenha_chao(self):
        for i in range(self.quantidade+1):
            self.window.blit(self.chao,(i*self.chao_largura,360))
        for posicao in self.pontos.items():
            self.window.blit(self.chao,(posicao[1][0],posicao[1][1]))
                          
class Tela_Inverno:
    def __init__(self):
        pygame.init()
        self.imagem = pygame.image.load('docs/imagens/Inverno_att.png')
        self.imagem= pygame.transform.scale(self.imagem,(2500,409))
        self.imprime_x = -500

    
    def desenha_tela(self,window):
        window.blit(self.imagem,(self.imprime_x,0))

class Personagem():
    def __init__(self,window):
        self.posicao_jogador = [window.get_width()//2, 309]
        self.jogador = pygame.transform.scale((pygame.image.load('docs/imagens/personagem.png')),(50,50))
        self.velocidade_x = 0
        self.ajuste = 0
        self.window = window
    def desenha_jogador(self):
        self.window.blit(self.jogador,(self.posicao_jogador[0],self.posicao_jogador[1]))
        

class Jogo:
    def __init__(self):
        self.window = pygame.display.set_mode((1000,409))
        self.window_largura=self.window.get_width()
        self.tela=Tela_Inverno()
        self.chao=Chao(self.tela.imagem)
        self.jogador = Personagem(self.window)
        self.plataforma=Plataforma(self.tela.imagem)
    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if self.tela.imprime_x > -1500 and self.tela.imprime_x < 0:
                self.jogador.ajuste = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.jogador.velocidade_x -= 5
                    if event.key == pygame.K_LEFT:
                        self.jogador.velocidade_x += 5 
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.jogador.velocidade_x -= 5
                    if event.key == pygame.K_RIGHT:
                        self.jogador.velocidade_x += 5
            if self.tela.imprime_x <= -1500:
                self.tela.imprime_x = -1500
                self.jogador.velocidade_x = 0
            if self.tela.imprime_x >= 0:
                self.tela.imprime_x = 0
                self.jogador.velocidade_x = 0
            if self.tela.imprime_x <= -1500:
                self.jogador.velocidade_x = 0
                if self.jogador.ajuste >= 0 and self.jogador.ajuste < 500:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            self.jogador.ajuste += 5
                        if event.key == pygame.K_LEFT:
                            self.jogador.ajuste -= 5
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            self.jogador.ajuste += 5
                        if event.key == pygame.K_RIGHT:
                            self.jogador.ajuste -= 5
                if self.jogador.ajuste < 0:
                    self.jogador.ajuste = 0
                if self.jogador.ajuste > 500:
                    self.jogador.ajuste = 500
            if self.tela.imprime_x >= 0:
                if self.jogador.ajuste <= -500 and self.jogador.ajuste >= 0:
                    self.jogador.velocidade_x = 0
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            self.jogador.ajuste += 5
                        if event.key == pygame.K_LEFT:
                            self.jogador.ajuste -= 5
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            self.jogador.ajuste += 5
                        if event.key == pygame.K_RIGHT:
                            self.jogador.ajuste -= 5
                if self.jogador.ajuste > 0:
                    self.jogador.ajuste = 0
                if self.jogador.ajuste < -500:
                    self.jogador.ajuste = -500
        self.jogador.posicao_jogador[0] += self.jogador.ajuste
        self.tela.imprime_x += self.jogador.velocidade_x

        return True

    def desenha_inicio(self):
        self.tela.desenha_tela(self.window)
        self.jogador.desenha_jogador()
        self.chao.desenha_chao()
        self.plataforma.desenha_plataforma()
        pygame.display.update()

    def loop(self):
        while self.atualiza_estado():
            self.desenha_inicio()
        

    