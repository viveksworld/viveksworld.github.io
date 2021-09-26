class Card:

    CARD_SUITE = {
        "hearts": "♥",
        "diamonds": "♦",
        "clubs": "♣",
        "spades": "♠"
    }

    CARD_TEXT_VALUE = {
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "Jack",
        12: "Queen",
        13: "King",
        14: "Ace"
    }

    def __init__(self, value, suite, ):
        self._suite = suite
        self._value = value

    @property
    def suite(self):
        return self._suite

    @property
    def value(self):
        return self._value

    def is_special(self):
        return self._value > 10

    def get_description(self):
        desc = "{}{}".format(Card.CARD_TEXT_VALUE[self._value], Card.CARD_SUITE[self._suite])
        return desc

    def __str__(self):
        return self.get_description()