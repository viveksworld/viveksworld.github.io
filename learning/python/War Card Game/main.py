from player import Player
from war_card_game import Game

player1_name = input("Enter the name of player #1 : ")
player2_name = input("Enter the name of player #2 : ")

player1 = Player(player1_name)
player2 = Player(player2_name)
game = Game(player1, player2)