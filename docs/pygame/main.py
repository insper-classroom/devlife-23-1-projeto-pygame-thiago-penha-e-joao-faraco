import pygame
import tela_inverno
from tela_inverno import window
from tela_inverno import Coin 
tela=tela_inverno                      

class Tela_Inicio:
    def __init__(self,jogo):
        self.jogo = jogo
        self.imagem_fundo = pygame.transform.scale(pygame.image.load('docs/imagens/seasons.webp'),(1000,410))
        self.imagem_fundo_maior = pygame.transform.scale(pygame.image.load('docs/imagens/seasons.webp'),(1005,415))
        self.titulo = pygame.transform.scale(pygame.image.load('docs/imagens/otitulo.png'),(800,90))
        self.titulo_maior = pygame.transform.scale(pygame.image.load('docs/imagens/otitulo.png'),(805,95))
        self.jogar = pygame.transform.scale(pygame.image.load('docs/imagens/Jogar2.png'),(200,80))
        self.rect_inicio = pygame.Rect(400,250,200,80)
        self.jogar_maior = pygame.transform.scale(pygame.image.load('docs/imagens/Jogar2.png'),(205,85))
        self.rect_inicio_maior = pygame.Rect(400,250,205,85)
        self.contador=0 
        self.saiu_no_inicio = False

    def atualiza_estado_inicio(self):
        for event in pygame.event.get():
            if event.type== pygame.MOUSEBUTTONDOWN:
                self.pos = pygame.mouse.get_pos()
                if self.rect_inicio.collidepoint(self.pos) or self.rect_inicio_maior.collidepoint(self.pos):
                    self.jogo.tela_atual=1
            if event.type == pygame.QUIT:
                    pygame.quit()
                    self.saiu_no_inicio = True
                    return False
        return True
    def desenha_Tela_Inicio(self):
        self.contador+=0.1
        if self.contador>=20:
            window.blit(self.imagem_fundo_maior,(0,0))
            window.blit(self.titulo_maior,(100,1))
            pygame.draw.rect(window,(0,0,0),self.rect_inicio_maior)
            window.blit(self.jogar_maior,(400,250))
        else:
            window.blit(self.imagem_fundo,(0,0))
            pygame.draw.rect(window,(0,0,0),self.rect_inicio)
            window.blit(self.jogar,(400,250))
            window.blit(self.titulo,(100,1))
        if self.contador>=40:
            self.contador=0

class Tela_Game_Over:
    def __init__(self,jogo):
        self.jogo = jogo
        self.game_over = pygame.transform.scale(pygame.image.load('docs/imagens/gameover.png'),(1000,205))
        self.recomecar = pygame.transform.scale(pygame.image.load('docs/imagens/Recomecar.png'),(800,205))
        # self.fechou_over = False
        self.music=pygame.mixer.Sound('docs/sons/game_over_bad_chest.wav')
        self.play=False 
    def atualiza_estado_over(self):
        pygame.mixer.music.stop()
        if not self.play:
            self.music.play()
            self.play=True
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.jogo.jogador.vidas <=0:
                    return False
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
        return True
    def desenha_game_over(self):
        window.fill((246,246,246))
        window.blit(self.game_over,(0,0))
        window.blit(self.recomecar,(100,206))

class Personagem(pygame.sprite.Sprite):
   
    def __init__(self,tela,fonte,jogo):
        pygame.sprite.Sprite.__init__(self)
        self.platafroma_image=pygame.transform.scale(pygame.image.load('docs/imagens/plataforma.png'),(150,50)).convert_alpha()
        self.image = pygame.transform.scale((pygame.image.load('docs/imagens/personagem.png')),(50,50)).convert_alpha()
        self.mask=pygame.mask.from_surface(self.image)
        self.velocidade_x = 0
        self.ajuste = 0
        self.rect=self.image.get_rect(bottomright=(window.get_width()//2, 360))
        self.tela=tela
        self.vidas = 3
        self.jogo=jogo
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
        self.movimentação_monstro=0

    def movimenta_jogador(self,tela):
        clock = pygame.time.Clock()
        clock.tick(80)
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
            if event.type == pygame.QUIT:
                pygame.quit()
                self.fechou_no_jogo = True
                return False
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
            self.movimentação_monstro+=0.05
            if self.movimentação_monstro>=10:
                monstro.rect.x+=2
            else:
                monstro.rect.x-=2
            if self.movimentação_monstro>=20:
                self.movimentação_monstro=0
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

        return True
    
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
        
class Jogo:

    global tela 
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Four Seasons Odyssey')
        self.tela_atual = 0
        self.font = pygame.font.Font('docs/fontes/PressStart2P.ttf', 20)
        self.window_largura=window.get_width()
        self.tela=tela.Tela_Inverno(self.font)
        self.chao=tela.Chao(self.tela.imagem)
        self.jogador = Personagem(self.tela,self.font,self)
        self.tela_inicio=Tela_Inicio(self)
        self.tela_game_over=Tela_Game_Over(self)
        self.inverteu = False
        self.tocou = False
        self.fechou = False
        self.tela_outono=False 
        pygame.mixer_music.load('docs/sons/game_music.wav')
        pygame.mixer_music.play(1000000000)

    def atualiza_estado(self): 
        if self.jogador.vidas <= 0:
            self.tela_atual = 2
        if self.tela_atual == 0:
            return self.tela_inicio.atualiza_estado_inicio()
        if self.tela_atual == 2:
            return self.tela_game_over.atualiza_estado_over()
        if self.tela_atual == 1 or self.tela_atual==3:
            return self.jogador.movimenta_jogador(self.tela)

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
        