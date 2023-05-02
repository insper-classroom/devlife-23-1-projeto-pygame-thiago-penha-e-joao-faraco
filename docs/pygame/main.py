import pygame
import tela_inverno
from tela_inverno import window
from tela_inverno import Coin 
import tela_outono
import tela_verao        
import tela_primavera            

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
        self.como_jogar=pygame.transform.scale(pygame.image.load('docs/imagens/Como jogar.png'),(150,50))
        self.rect_instrucoes=pygame.Rect(420,340,150,50)
        self.como_jogar_maior=pygame.transform.scale(pygame.image.load('docs/imagens/Como jogar.png'),(155,55))
        self.rect_instrucoes_maior=pygame.Rect(420,340,155,55)
        self.contador=0 
        self.saiu_no_inicio = False

    def atualiza_estado_inicio(self):
        for event in pygame.event.get():
            if event.type== pygame.MOUSEBUTTONDOWN:
                self.pos = pygame.mouse.get_pos()
                if self.rect_inicio.collidepoint(self.pos) or self.rect_inicio_maior.collidepoint(self.pos):
                    self.jogo.tela_atual=2
                elif  self.rect_instrucoes.collidepoint(self.pos) or self.rect_instrucoes_maior.collidepoint(self.pos):
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
            window.blit(self.como_jogar_maior,(420,340))
        else:
            window.blit(self.imagem_fundo,(0,0))
            pygame.draw.rect(window,(0,0,0),self.rect_inicio)
            window.blit(self.jogar,(400,250))
            window.blit(self.titulo,(100,1))
            window.blit(self.como_jogar,(420,340))
        if self.contador>=40:
            self.contador=0

class Instrucao:
    def __init__(self,jogo):
        self.jogo=jogo
        self.image=pygame.transform.scale(pygame.image.load('docs/imagens/instruções.png'),(1000,410))
        self.voltar=pygame.transform.scale(pygame.image.load('docs/imagens/voltar.pnng.png'),(25,25))
        self.voltar=pygame.transform.flip(self.voltar, True, False)
        self.voltar_rect=pygame.Rect(5,0,40,40)
    def atualiza_instrucao(self):
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.saiu_no_inicio = True
                return False
            elif  event.type== pygame.MOUSEBUTTONDOWN:
                self.pos = pygame.mouse.get_pos()
                if self.voltar_rect.collidepoint(self.pos):
                    self.jogo.tela_atual=0
        return True 
    def desenha_instrucao(self):
        window.blit(self.image,(0,0))
        window.blit(self.voltar,(5,0))

class Tela_Game_Over:
    def __init__(self,jogo):
        self.jogo = jogo
        self.game_over = pygame.transform.scale(pygame.image.load('docs/imagens/gameover.png'),(1000,205))
        self.recomecar = pygame.transform.scale(pygame.image.load('docs/imagens/Recomecar.png'),(800,205))
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

class Tela_ganhou:
    def __init__(self,jogo):
        self.jogo = jogo
        self.image=pygame.transform.scale((pygame.image.load('docs/imagens/tela-vitoria.png')),(1000,410)).convert_alpha()
        self.contador=0
        self.music = pygame.mixer.Sound('docs/sons/Cant Stop Winning.mp3')
        self.play = False
    def atualiza_estado_ganhou(self):
        pygame.mixer.music.stop()
        if not self.play:
            self.music.play()
            self.play=True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
        return True
    
    def desenha_ganhou(self):
        self.contador+=0.1
        window.fill((0,0,0))
        window.blit(self.image,(0,0))


class Personagem(pygame.sprite.Sprite):
   
    def __init__(self,fonte,jogo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale((pygame.image.load('docs/imagens/personagem.png')),(50,50)).convert_alpha()
        self.velocidade_x = 0
        self.ajuste = 0
        self.rect=self.image.get_rect(bottomright=(window.get_width()//2, 360))
        self.vidas =5
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
        if (tela.imprime_x<=-2000 and (self.direcao=='direita' or self.rect.x>=window.get_width()//2)) or (tela.imprime_x>=0 and (self.direcao=='esquerda'or self.rect.x<=window.get_width()//2)):
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
            for chao in tela.chaoGroup:
                chao.rect.x-=self.velocidade_x
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
        
        if self.rect.x>=1001 and tela.contador_coin>=10 and self.jogo.tela_atual == 2:
            self.jogo.tela_atual=3
            self.jogo.contador_tela=1
            self.rect.x=0
        if self.rect.x >= 1001 and tela.contador_coin >= 15 and self.jogo.tela_atual == 3:
            self.jogo.tela_atual = 4
            self.jogo.contador_tela = 2
            self.rect.x = 0
        if self.rect.x >= 1001 and tela.contador_coin >= 20 and self.jogo.tela_atual == 4:
            self.jogo.tela_atual = 5
            self.jogo.contador_tela = 3
            self.rect.x = 0
        if self.rect.x >= 1001 and tela.contador_coin >= 25 and self.jogo.tela_atual == 5:
            self.jogo.tela_atual = 7
        return True
    
    def desenha_jogador(self,tela):
        self.coracao = self.fonte.render(chr(9829)*self.vidas,True,(255,0,0))
        window.blit(self.coracao,(0,0))
        self.gravidade+=0.8
        self.rect.y+=self.gravidade
        if self.rect.bottom>=360:
            self.rect.bottom=360
            self.maximo=360
        if self.rect.bottom<self.maximo:
            self.maximo=self.rect.bottom
        for plataforma in tela.plataformaGroup:
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

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Four Seasons Odyssey')
        self.tela_atual = 0
        self.telas=[]
        self.font = pygame.font.Font('docs/fontes/PressStart2P.ttf', 20)
        self.window_largura=window.get_width()
        self.telas.append(tela_inverno.Tela_Inverno(self.font))
        self.telas.append(tela_primavera.Tela_Primavera(self.font))
        self.telas.append(tela_verao.Tela_Verao(self.font))
        self.telas.append(tela_outono.Tela_Outono(self.font))
        self.jogador = Personagem(self.font,self)
        self.tela_inicio=Tela_Inicio(self)
        self.tela_game_over=Tela_Game_Over(self)
        self.tela_instrucao=Instrucao(self)
        self.tela_ganhou = Tela_ganhou(self)
        self.inverteu = False
        self.tocou = False
        self.contador=0
        self.fechou = False
        self.tela_outono=False 
        self.contador_tela=0
        pygame.mixer_music.load('docs/sons/game_music.wav')
        pygame.mixer_music.play(1000000000)

    def atualiza_estado(self): 
        if self.jogador.vidas <= 0:
            self.tela_atual = 6
        if self.tela_atual == 6:
            return self.tela_game_over.atualiza_estado_over()
        elif self.tela_atual==1:
            return self.tela_instrucao.atualiza_instrucao()
        elif self.tela_atual == 0:
            return self.tela_inicio.atualiza_estado_inicio()
        elif self.tela_atual == 2 or self.tela_atual==3 or self.tela_atual == 4 or self.tela_atual == 5:
            return self.jogador.movimenta_jogador(self.telas[self.contador_tela])
        elif self.tela_atual == 7:
            return self.tela_ganhou.atualiza_estado_ganhou()
        

    def desenha_inicio(self):
        if self.tela_atual==2 or self.tela_atual==3 or self.tela_atual == 4 or self.tela_atual == 5:
            self.telas[self.contador_tela].desenha_tela()
            self.telas[self.contador_tela].desenha_personagens()   
            self.jogador.desenha_jogador(  self.telas[self.contador_tela])
        elif self.tela_atual==0:
           self.tela_inicio.desenha_Tela_Inicio()
        elif self.tela_atual == 6:
            self.tela_game_over.desenha_game_over() 
        elif self.tela_atual==1:
            self.tela_instrucao.desenha_instrucao()
        elif self.tela_atual == 7:
            self.tela_ganhou.desenha_ganhou()
        pygame.display.update()

    def loop(self):
        while self.atualiza_estado():
            self.desenha_inicio()
        
