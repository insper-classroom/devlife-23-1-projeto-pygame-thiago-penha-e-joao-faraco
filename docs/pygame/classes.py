import pygame

pygame.init()
class Jogo:
    def __init__(self):
        self.imagem = pygame.image.load('docs\imagens\Inverno_att.png')
        self.imagem= pygame.transform.scale(self.imagem,(1313,409))
        self.window = pygame.display.set_mode((1313,409))

    def desenha(self):
        self.window.fill((0,0,0))
        self.window.blit(self.imagem,(0,0))
        pygame.display.update()
    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True