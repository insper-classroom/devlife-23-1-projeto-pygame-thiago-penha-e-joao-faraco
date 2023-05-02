import pygame 
import random
from tela_inverno import window 

 
class Bolinha(pygame.sprite.Sprite):   
    '''
    
Define a classe Bolinha, que é uma subclasse de pygame.sprite.Sprite.

A classe Bolinha representa uma bolinha em um jogo. Ela é utilizada para criar instâncias de bolinhas, que podem ser adicionadas a um grupo de sprites.

Atributos:

image: uma superfície que representa a imagem da bolinha
rect: um retângulo que representa a posição e o tamanho da bolinha na tela
Métodos:

init(self,x,y): inicializa uma nova instância da classe Bolinha, definindo sua posição inicial na tela

    '''
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(pygame.image.load('docs/imagens/bolinha.png'),(25,25)).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

class Planta(pygame.sprite.Sprite):
    '''
    Classe que define uma planta para um jogo pygame.

    Atributos:
        image (pygame.Surface): uma superfície que representa a imagem da planta.
        rect (pygame.Rect): um retângulo que define a posição e o tamanho da imagem da planta na tela.

    Parâmetros:
        x (int): coordenada x do canto superior esquerdo da imagem da planta.
        y (int): coordenada y do canto superior esquerdo da imagem da planta.
    
    Métodos:
        Nenhum método além do construtor é definido nesta classe.
    '''    
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(pygame.image.load('docs/imagens/Planta.png'),(60,60)).convert_alpha()
        self.image=pygame.transform.flip(self.image, True, False)
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

class Coin(pygame.sprite.Sprite):
    '''
    
A classe Coin representa uma moeda que pode ser coletada pelo jogador em um jogo implementado com a biblioteca pygame.

Atributos:

image: uma imagem de uma moeda carregada a partir de um arquivo de imagem e redimensionada para o tamanho de 25x25 pixels.
contador: uma outra imagem de uma moeda carregada a partir de um arquivo de imagem e redimensionada para o tamanho de 50x50 pixels. É usada para exibir o contador de moedas coletadas.
rect: um retângulo que envolve a imagem da moeda.
topleft: um par de coordenadas (x,y) que define a posição da moeda na tela.
Métodos:

__init__: o construtor da classe. Define a imagem, o contador, o retângulo e a posição inicial da moeda.
O código utiliza a herança de pygame.sprite.Sprite para criar uma classe de sprites de moedas que pode ser adicionada a um grupo de sprites.
    '''
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(pygame.image.load('docs/imagens/coin_2.png'),(25,25)).convert_alpha()
        self.contador=pygame.transform.scale(pygame.image.load('docs/imagens/coin_2.png'),(50,50)).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

class Plataforma(pygame.sprite.Sprite):
    '''
    Classe que define uma plataforma para um jogo pygame.

    Atributos:
        image (pygame.Surface): uma superfície que representa a imagem da plataforma.
        rect (pygame.Rect): um retângulo que define a posição e o tamanho da imagem da plataforma na tela.

    Parâmetros:
        x (int): coordenada x do canto superior esquerdo da imagem da plataforma.
        y (int): coordenada y do canto superior esquerdo da imagem da plataforma.
    
    Métodos:
        Nenhum método além do construtor é definido nesta classe.
    '''
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(pygame.image.load('docs/imagens/plat-outono.png'),(150,50)).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

class Chao(pygame.sprite.Sprite):
    '''

    Classe que define um chão para um jogo pygame.

    Atributos:
        image (pygame.Surface): uma superfície que representa a imagem do chão.
        rect (pygame.Rect): um retângulo que define a posição e o tamanho da imagem do chão na tela.

    Parâmetros:
        x (int): coordenada x do canto superior esquerdo da imagem do chão.
        y (int): coordenada y do canto superior esquerdo da imagem do chão.
    
    Métodos:
        Nenhum método além do construtor é definido nesta classe.
    
    '''
    def __init__(self,x,y):
         pygame.sprite.Sprite.__init__(self)
         self.image=pygame.transform.scale(pygame.image.load('docs/imagens/chao-outono.png'),(50,50))
         self.rect=self.image.get_rect()
         self.rect.topleft=(x,y)

class Monstro(pygame.sprite.Sprite):
    '''

    Classe que define um monstro para um jogo pygame.

    Atributos:
        image (pygame.Surface): uma superfície que representa a imagem do monstro.
        rect (pygame.Rect): um retângulo que define a posição e o tamanho da imagem do monstro na tela.

    Parâmetros:
        x (int): coordenada x do canto superior esquerdo da imagem do monstro.
        y (int): coordenada y do canto superior esquerdo da imagem do monstro.
    
    Métodos:
        Nenhum método além do construtor é definido nesta classe.
    '''
    def __init__(self,x,y):
        super().__init__()
        self.tick=0
        self.image = pygame.transform.scale(pygame.image.load('docs/imagens/monstroatt.png'),(50,50))
        self.rect = self.image.get_rect() 
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

class Tela_Outono():
    '''
    A classe Tela_Outono representa a tela do jogo correspondente à fase de primavera. Ela possui diversos métodos responsáveis por criar e desenhar os elementos que compõem a tela, tais como plataformas, moedas, monstros e outros objetos.

Métodos:

__init__(self,fonte): inicializa a tela e cria os elementos que compõem a fase.
desenha_chao(self): cria as plataformas que compõem o chão da fase.
desenha_bolinha(self): cria as bolinhas que as plantas lançam em direção ao jogador.
cria_monstro(self): cria os monstros que aparecem aleatoriamente na fase.
cria_arvore(self): cria as árvores que compõem o cenário da fase.
cria_plat(self): cria as plataformas que o jogador pode pular.
cria_coin(self): cria as moedas que o jogador deve coletar.
cria_planta(self): cria as plantas que lançam as bolinhas.
desenha_tela(self): desenha a imagem de fundo da fase, as árvores e as moedas coletadas.
desenha_personagens(self): desenha os personagens na tela, como as plataformas, as plantas, os monstros, as moedas e o chão.
Atributos:

imagem: imagem de fundo da fase.
arvore: imagem da árvore que compõe o cenário.
next_level: imagem que indica o local da próxima fase.
moeda_contadora: imagem da moeda que indica a quantidade de moedas coletadas pelo jogador.
imprime_x: coordenada x da imagem de fundo da fase.
arvores: lista com as coordenadas das árvores do cenário.
posicao_plat: lista com as coordenadas das plataformas.
fonte: fonte utilizada para desenhar a quantidade de moedas coletadas.
contador_coin: quantidade de moedas coletadas pelo jogador.
frequenciadotiro: frequência com que as bolinhas são lançadas pelas plantas.
plataformaGroup: grupo de sprites das plataformas.
coinGroup: grupo de sprites das moedas.
grupo_monstro: grupo de sprites dos monstros.
plantaGroup: grupo de sprites das plantas.
bolinhaGroup: grupo de sprites das bolinhas.
chaoGroup: grupo de sprites do chão.
    '''
    def __init__(self,fonte):
        self.imagem=pygame.transform.scale(pygame.image.load('docs/imagens/floresta_outono.jpg'),(3000,410)).convert_alpha()
        self.arvore=pygame.transform.scale(pygame.image.load('docs/imagens/arvore-outono.png'),(80,100))
        self.next_level=pygame.transform.scale(pygame.image.load('docs/imagens/next_level.png'),(100,100)).convert_alpha()
        self.moeda_contadora=pygame.transform.scale(pygame.image.load('docs/imagens/coin_2.png'),(50,50)).convert_alpha()
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
        '''
        Método que desenha o chão do jogo.

    A função itera sobre um range de 0 a 60 e a cada iteração, multiplica o valor de i por 50
    para definir a posição x do objeto "chao". A posição y é definida como 360.
    Em seguida, um objeto "Chao" é criado com as coordenadas x e y definidas, e é adicionado 
    ao grupo de sprites "chaoGroup".

       '''
        for i in range(61):
            x= i*50
            y=360
            chao=Chao(x,y)
            self.chaoGroup.add(chao)

    def desenha_bolinha(self):
        '''
         Incrementa a variável 'frequenciadotiro' a cada chamada da função. 
        Quando essa variável atinge um múltiplo de 300, uma nova bolinha é criada a partir da posição de 
        uma planta e adicionada ao grupo de bolinhas. Todas as bolinhas existentes são então movidas 3 pixels
        para a esquerda. E desenha as bolinhas
        '''
        self.frequenciadotiro+=0.5
        if self.frequenciadotiro%80==0:
            for planta in self.plantaGroup:
                bolinha=Bolinha(planta.rect.x,planta.rect.y+10)
                self.bolinhaGroup.add(bolinha)
        for bolinha in self.bolinhaGroup:
            bolinha.rect.x-=5
        self.bolinhaGroup.draw(window)

    def cria_monstro(self):
        '''

 Cria um grupo de monstros aleatórios em posições específicas do jogo.

    Cada monstro é criado em uma posição aleatória no eixo X e fixa no eixo Y. 
    É verificado se há colisão com outro monstro já existente antes de adicioná-lo ao grupo.

        '''
        i=0
        while i<8:
            posicao_x = random.randint(600, 2450)
            posicao_y = 310
            monstro=Monstro(posicao_x,posicao_y)
            if not pygame.sprite.spritecollide(monstro, self.grupo_monstro, False, pygame.sprite.collide_mask) :
                i+=1
                self.grupo_monstro.add(monstro)

    def cria_arvore(self):
        '''
        Gera a posição x de 10 árvores aleatórias em um intervalo definido e fixa a posição y das árvores em 260.
    A posição x é armazenada em uma lista chamada 'arvores'.
        '''
        for i in range(10):
            posicao_x = random.randint(0, 2470)
            self.arvores.append([posicao_x,260])
    
    def cria_plat(self):
        '''
A função cria_plat gera plataformas aleatórias e as adiciona ao grupo de plataformas plataformaGroup. A função utiliza um laço while para criar até oito plataformas. Dentro do laço, são geradas coordenadas aleatórias posicao_x e posicao_y para a plataforma, e uma nova instância da classe Plataforma é criada com essas coordenadas.

Antes de adicionar a plataforma ao grupo de plataformas, é verificado se há colisão com outra plataforma no grupo utilizando a função spritecollide. Caso não haja colisão, a plataforma é adicionada ao grupo.
        '''
        i=0
        while i<8:
            posicao_x = random.randint(0, 2450)
            posicao_y = random.randint(150,250)
            plataforma=Plataforma(posicao_x,posicao_y)
            if not pygame.sprite.spritecollide(plataforma, self.plataformaGroup, False, pygame.sprite.collide_mask):
                i+=1
                self.plataformaGroup.add(plataforma)
    
    def cria_coin(self):
        '''
        A função cria_coin tem como objetivo criar moedas em locais aleatórios na tela. O parâmetro j é utilizado para controlar o número de moedas criadas, e o loop while garante que o número de moedas criadas seja exatamente 15.

Dentro do loop, a posição posicao_x é definida aleatoriamente entre 600 e 2450, e a posição posicao_y é definida aleatoriamente entre 100 e 330. Em seguida, um objeto Coin é criado nessas posições.

Antes de adicionar a moeda ao grupo coinGroup, é verificado se ela colide com algum objeto do grupo plataformaGroup ou coinGroup. Caso a moeda não colida com nenhum desses objetos, ela é adicionada ao grupo coinGroup e o contador j é incrementado.
        '''
        j=0
        while j<20:
            posicao_x = random.randint(600, 2450)
            posicao_y = random.randint(100,330)
            coin=Coin(posicao_x,posicao_y)
            if not pygame.sprite.spritecollide(coin, self.coinGroup, False, pygame.sprite.collide_mask) and not pygame.sprite.spritecollide(coin, self.plataformaGroup, False, pygame.sprite.collide_mask):
                j+=1
                self.coinGroup.add(coin)

    def cria_planta(self):
        '''
             Método para criar moedas no jogo.

    Cria 15 moedas em posições aleatórias na área do jogo. A posição Y é aleatória entre 100 e 330 pixels, enquanto a posição X é aleatória entre 600 e 2450 pixels. A função verifica se a nova moeda não colide com outras moedas ou plataformas existentes antes de adicioná-la ao grupo de moedas.
         '''
        j=0
        while j<5:
            posicao_x = random.randint(1500, 2450)
            posicao_y = 310
            planta=Planta(posicao_x,posicao_y)
            if not pygame.sprite.spritecollide(planta, self.plantaGroup, False, pygame.sprite.collide_mask):
                self.plantaGroup.add(planta)
                j+=1


    def desenha_tela(self):
        '''
        window.blit(self.imagem,(self.imprime_x,0)): desenha a imagem de fundo na posição (self.imprime_x,0) na tela;
for arvore in self.arvores: self.imagem.blit(self.arvore,(arvore[0],arvore[1])): desenha as árvores em posições aleatórias na tela;
window.blit(self.moeda_contadora,(900,20)): desenha a imagem de um ícone de moeda na posição (900,20) na tela;
self.contador_imagem=self.fonte.render(str(self.contador_coin),True,(0,0,0)): renderiza a imagem do texto que exibe a quantidade de moedas coletadas;
window.blit(self.contador_imagem,(960,35)): desenha o texto do contador de moedas na posição (960,35) na tela;
self.imagem.blit(self.next_level,(2800,280)): desenha o texto "Próximo nível" na posição (2800,280) na tela.
        '''
        window.blit(self.imagem,(self.imprime_x,0))
        for arvore in self.arvores:
            self.imagem.blit(self.arvore,(arvore[0],arvore[1]))
        window.blit(self.moeda_contadora,(900,20))
        self.contador_imagem=self.fonte.render(str(self.contador_coin),True,(0,0,0))
        window.blit(self.contador_imagem,(960,35))
        self.imagem.blit(self.next_level,(2800,280))
    
    def desenha_personagens(self):
        '''
        desenha todos os grupos de sprites na window
        '''
        self.plataformaGroup.draw(window)
        self.coinGroup.draw(window)
        self.plantaGroup.draw(window)
        self.grupo_monstro.draw(window)
        self.chaoGroup.draw(window)
        self.desenha_bolinha()
        