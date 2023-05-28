from game import Game

game = Game()

while game.running:
    game.curr_menu.display_menu()
    game.game_loop()

#TODO:
#fix the mouse going into the fucking floor
#fix the cat going into the fucking walls
#fix the cat going into fucking orbit
#fix the funny-ahh physics