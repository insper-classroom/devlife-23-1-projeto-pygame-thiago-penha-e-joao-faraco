from main import Jogo
'''
criou-se outro loop aqui para garantir que o jogo possa ser reiniciado após o jogador morrer
'''
roda = True
while roda:
    game = Jogo()
    game.loop()



