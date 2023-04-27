from classes import Jogo

roda = True
while roda:
    game = Jogo()
    game.loop()
    if game.fechou :
        roda = False


