import pygame
import random
class Chao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.chao=pygame.transform.scale(pygame.image.load('docs/imagens/chao inverno.png'),(50,50))
        self.chao_rect=self.chao.get_rect()
        self.chao_altura=self.chao.get_height()
        self.chao_largura=self.chao.get_width()
        self.pontos={}
        self.quantidade=0
    def desenha_chao(self,window):
        self.quantidade+= window.get_width()//self.chao_largura
        for i in range(self.quantidade+1):
            window.blit(self.chao,(i*self.chao_largura,360))
            self.pontos[i]=(i*self.chao_largura,360)
    def desenha_plataforma(self,window,quantidade):
        i=0
        while  i <=1 :
            posicao_x=random.randint(0,1263)
            posicao_y=random.randint(200,361-50)
            for ponto in self.pontos.items():
                out = True
                if (posicao_x>=ponto[1][0] and posicao_x<=ponto[1][0]+self.chao_largura and posicao_y>=ponto[1][1] and posicao_y<=ponto[1][1]+self.chao_altura):
                    out = False
                    break
            if out:
                for j in range(5):
                    window.blit(self.chao,(posicao_x+(j*self.chao_largura),posicao_y))
                    self.pontos[quantidade+1+i]=(posicao_x+(j*self.chao_largura),posicao_y)
                i+=1
                              
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
        self.chao=Chao()
        self.jogador = Personagem(self.window)
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
        self.chao.desenha_chao(self.window)
        pygame.display.update()

    def loop(self):
        while self.atualiza_estado():
            self.desenha_inicio()
        

    