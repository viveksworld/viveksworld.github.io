from card import Card
from random import shuffle
import sys


class Game:

    round_number = 0

    def __init__(self, player1, player2):
        self._player1 = player1
        self._player2 = player2
        print("Building Cards...")
        self._cards = self.build_cards()

        print("Shuffling Cards...")
        self.shuffle_card()

        print("Distributing cards to players...")
        self.distribute_cards_to_players()

        self.show_player_stats()

        self.play_battle(None)

    @property
    def player1(self):
        return self._player1

    @property
    def player2(self):
        return self._player2

    @staticmethod
    def build_cards():
        cards = []
        for suite in Card.CARD_SUITE:
            for value in Card.CARD_TEXT_VALUE.keys():
                cards.append(Card(value, suite))
        return cards

    def show_cards(self):
        if self._cards:
            for card in self._cards:
                print(card.get_description())
        else:
            print("Cards not found. You need to have a card deck to play this game.")

    def shuffle_card(self):
        shuffle(self._cards)

    def distribute_cards_to_players(self):
        idx = 0
        while True:
            idx += 1
            if self._cards:
                card = self._cards.pop()
                if idx % 2 == 1:
                    self._player1.add_card_to_deck_top(card)
                    self._player1.count_cards_in_deck()
                    # self._player1.show_cards()
                else:
                    self._player2.add_card_to_deck_top(card)
                    self._player2.count_cards_in_deck()
                    # self._player2.show_cards()
            else:
                break

    def play_battle(self, cards_on_ground):

        if cards_on_ground is None:
            cards_on_ground = []



        while 1:
        # Un-comment the below block to play the game interactively
        #     user_input = input("Press Y to continue with the next round: ")
        #     if user_input.lower() != 'y':
        #         print("Thanks for playing War Game...Hope you enjoyed this game")
        #         return 0
        #     else:

            Game.round_number += 1

            print("Round # {}".format(Game.round_number))

            player1_card = self._player1.draw_card_from_deck()
            player2_card = self._player2.draw_card_from_deck()

            self.check_game_over(player1_card, player2_card)

            print("{} got {}".format(self._player1.name, player1_card.get_description()))

            print("{} got {}".format(self._player2.name, player2_card.get_description()))

            round_winner = self.find_round_winner(player1_card, player2_card)

            cards_on_ground = cards_on_ground + [player1_card, player2_card]

            if round_winner == 1:
                # Add cards to player1 deck
                print("{} Wins this round".format(self._player1.name))
                self.add_cards_to_player(self._player1, cards_on_ground)
                self.show_player_stats()
                cards_on_ground.clear()
            elif round_winner == 2:
                # Add cards to player2 deck
                print("{} Wins this round".format(self._player2.name))
                self.add_cards_to_player(self._player2, cards_on_ground)
                self.show_player_stats()
                cards_on_ground.clear()
            else:
                # Start War
                print("This is a tie. Entering War ...".format(self._player2.name))
                self.show_player_stats()
                self.check_game_over_before_war()
                self.play_war(cards_on_ground)

    def show_player_stats(self):
        print("{} got {} card(s) in deck".format(self._player1.name, self._player1.count_cards_in_deck()))
        print("{} got {} card(s) in deck".format(self._player2.name, self._player2.count_cards_in_deck()))

    def play_war(self, cards_on_ground):
        player1_secret_card = self._player1.draw_card_from_deck()
        player2_secret_card = self._player2.draw_card_from_deck()

        cards_on_ground = cards_on_ground + [player1_secret_card, player2_secret_card]

        self.play_battle(cards_on_ground)

    def check_game_over_before_war(self):
        loser = 0
        if self._player1.count_cards_in_deck() < 2:
            loser += 1
        if self._player2.count_cards_in_deck() < 2:
            loser += 2

        if loser == 1:
            print("{} is not having sufficient cards to continue playing the game.".format(self._player1.name))
            print("{} Wins !".format(self.player2.name))
            sys.exit(0)
        elif loser == 2:
            print("{} is not having sufficient cards to continue playing the game.".format(self._player2.name))
            print("{} Wins !".format(self.player1.name))
            sys.exit(0)
        elif loser == 3:
            print("Both {} and {} are not having sufficient cards to continue playing the game.".format(self._player1.name, self._player2.name))
            print("This game is a tie !")

    def check_game_over(self, player1_card, player2_card):
        loser = 0
        if not player1_card:
            loser += 1
        if not player2_card:
            loser += 2

        if loser == 1:
            print("{} has no more card in the deck.".format(self._player1.name))
            print("{} Wins !".format(self.player2.name))
            sys.exit(0)
        elif loser == 2:
            print("{} has no more card in the deck.".format(self._player2.name))
            print("{} Wins !".format(self.player1.name))
            sys.exit(0)
        elif loser == 3:
            print("Both {} and {} have no more card in the deck.".format(self._player1.name, self._player2.name))
            print("This game is a tie !")

    @staticmethod
    def add_cards_to_player(player, cards):
        for card in cards:
            player.add_card_to_deck_bottom(card)

    @staticmethod
    def find_round_winner(player1_card, player2_card):
        if player1_card.value > player2_card.value:
            return 1
        elif player1_card.value < player2_card.value:
            return 2
        else:
            return 0
