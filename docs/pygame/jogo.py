from classes import Jogo

roda = True
while roda:
    game = Jogo()
    game.loop()
    if game.tela_inicio.saiu_no_inicio or game.jogador.fechou_no_jogo  :
        roda = False


