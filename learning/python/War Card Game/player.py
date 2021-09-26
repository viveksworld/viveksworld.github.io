class Player:

    def __init__(self, name, is_human=True):
        self._name = name
        self._is_human = is_human
        self._cards = list()

    @property
    def name(self):
        return self._name

    @property
    def is_human(self):
        return self._is_human

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, cards):
        self._cards = cards

    def draw_card_from_deck(self):
        if self._cards:
            return self._cards.pop()
        else:
            return None

    def add_card_to_deck_bottom(self, card):
        self._cards.insert(0, card)

    def add_card_to_deck_top(self, card):
        self._cards.append(card)

    def count_cards_in_deck(self):
        card_count = len(self._cards)
        return card_count

    def show_cards(self):
        if self._cards:
            for card in self._cards:
                print(card.get_description())
        else:
            print("No cards in deck")
