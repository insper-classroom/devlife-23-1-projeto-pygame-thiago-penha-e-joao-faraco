import pygame 
import random

window = pygame.display.set_mode((1000,409))      

class Bolinha(pygame.sprite.Sprite):   
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(pygame.image.load('docs/imagens/bolinha de neve.png'),(30,30)).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

class Planta(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(pygame.image.load('docs/imagens/Planta_neve.png'),(60,60)).convert_alpha()
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
    def __init__(self,x,y):
         pygame.sprite.Sprite.__init__(self)
         self.image=pygame.transform.scale(pygame.image.load('docs/imagens/chao inverno.png'),(50,50))
         self.rect=self.image.get_rect()
         self.rect.topleft=(x,y)

class Tela_Inverno():
    
    def __init__(self,fonte):
        self.imagem = pygame.transform.scale(pygame.image.load('docs/imagens/Inverno_att.png').convert_alpha(),(3000,410))
        self.next_level=pygame.transform.scale(pygame.image.load('docs/imagens/next_level.png'),(100,100)).convert_alpha()
        self.arvore=pygame.transform.scale(pygame.image.load('docs/imagens/Arvore_Inverno.png'),(100,100))
        self.moeda_contadora=pygame.transform.scale(pygame.image.load('docs/imagens/coin_2.png'),(50,50)).convert_alpha()
        self.image = pygame.transform.scale(pygame.image.load('docs/imagens/next_level.png'),(100,100)).convert_alpha()
        self.imprime_x=0   
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
        self.chaoGroup=pygame.sprite.Group()
        self.cria_arvore()
        self.cria_plat()
        self.cria_coin()
        self.cria_planta()
        self.cria_monstro()
        self.desenha_chao()
  
    def desenha_chao(self):
        for i in range(61):
            x= i*50
            y=360
            chao=Chao(x,y)
            self.chaoGroup.add(chao)
    
    def desenha_bolinha(self):
        self.frequenciadotiro+=0.5
        if self.frequenciadotiro%100==0:
            for planta in self.plantaGroup:
                bolinha=Bolinha(planta.rect.x,planta.rect.y+10)
                self.bolinhaGroup.add(bolinha)
        for bolinha in self.bolinhaGroup:
            bolinha.rect.x-=3
        self.bolinhaGroup.draw(window)

    def cria_monstro(self):
        i=0
        while i<5:
            posicao_x = random.randint(600, 2450)
            posicao_y = 310
            monstro=Monstro(posicao_x,posicao_y)
            if not pygame.sprite.spritecollide(monstro, self.grupo_monstro, False, pygame.sprite.collide_mask) :
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
            posicao_x = random.randint(600, 2450)
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
        self.imagem.blit(self.next_level,(2800,280))
    def desenha_personagens(self):
        self.plataformaGroup.draw(window)
        self.coinGroup.draw(window)
        self.plantaGroup.draw(window)
        self.grupo_monstro.draw(window)
        self.chaoGroup.draw(window)
        self.desenha_bolinha()

class Monstro(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('docs/imagens/monstroatt.png'),(50,50))
        self.rect = self.image.get_rect() 
        self.rect.topleft=(x,y)
