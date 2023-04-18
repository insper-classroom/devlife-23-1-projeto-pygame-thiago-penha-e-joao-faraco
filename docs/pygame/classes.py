import pygame
import random
class Chao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.chao=pygame.transform.scale(pygame.image.load('docs/imagens/chao inverno.png'),(50,50))
        self.chao_rect=self.chao.get_rect()
        self.chao_largura=self.chao.get_width()
    def desenha_chao(self,window):
        quantidade= window.get_width()//self.chao_largura
        for i in range(quantidade+1):
            window.blit(self.chao,(i*self.chao_largura,360))

class Tela_Inverno:
    def __init__(self):
        pygame.init()
        self.imagem = pygame.image.load('docs/imagens/Inverno_att.png')
        self.imagem= pygame.transform.scale(self.imagem,(1313,409))
    
    def desenha_tela(self,window):
        window.blit(self.imagem,(0,0))
        pygame.display.update()
    
class Jogo:
    def __init__(self):
        self.window = pygame.display.set_mode((1313,409))
        self.window_largura=self.window.get_width()
        self.tela=Tela_Inverno()
        self.chao=Chao()
    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def desenha(self):
        self.tela.desenha_tela(self.window)
        self.chao.desenha_chao(self.window)
        pygame.display.update()
   
    def loop(self):
        while self.atualiza_estado():
            self.desenha()
        

    