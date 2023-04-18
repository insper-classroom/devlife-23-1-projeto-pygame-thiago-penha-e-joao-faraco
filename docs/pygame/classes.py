import pygame

class Jogo:
    def __init__(self):
<<<<<<< HEAD
        pygame.init()
        self.imagem = pygame.image.load('docs\imagens\Inverno_att.png')
        self.imagem= pygame.transform.scale(self.imagem,(1313,409))
        self.window = pygame.display.set_mode((1313,409))
=======
        self.imagem = pygame.image.load('docs/imagens/Outono.png')
        self.imagem= pygame.transform.scale(self.imagem,(1000,500))
        self.window = pygame.display.set_mode((1000,500))
>>>>>>> 0002cfec01ab150eacc2ca0d12da006afd280ffb

    def desenha(self):
        # self.window.fill((0,0,0))
        self.window.blit(self.imagem,(0,0))
        pygame.display.flip()
    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True