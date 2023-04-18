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
    def desenha_chao(self,window):
        quantidade= window.get_width()//self.chao_largura
        for i in range(quantidade+1):
            window.blit(self.chao,(i*self.chao_largura,360))
            self.pontos[i]=(i*self.chao_largura,360)
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
        self.imagem= pygame.transform.scale(self.imagem,(1313,409))
    
    def desenha_tela(self,window):
        window.blit(self.imagem,(0,0))
    
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

    def desenha_inicio(self):
        self.tela.desenha_tela(self.window)
        self.chao.desenha_chao(self.window)
        pygame.display.update()
   
    def loop(self):
        self.desenha_inicio()
        while self.atualiza_estado():
            pass
        

    