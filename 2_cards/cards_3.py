class Card:
    "Игральная карта"

    RANKS = ["Т", "2", "3", "4", "5", "6", "7", 
            "8", "9", "10", "В", "Д", "К"]

    #масти
    SUITS = [u'\u2660', u'\u2663', u'\u2665', u'\u2666']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Unprintable_Card(Card):
    """Карта номинал и масть которой не могут выводиться на экран """

    def __str__(self):
        return "<Нельзя напечатать>"

class Positionable_Card(Card):
    """Можно менять положение таких карт """
    
    def __init__(self, rank, suit, face_up = True):
        super() .__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super() .__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up                

def main():
    card1 = Card("Т", Card.SUITS[0])
    card2 = Unprintable_Card("Т", Card.SUITS[1])
    card3 = Positionable_Card("Т", Card.SUITS[2])
    print("Печатаю открытую карту:")
    print(card1)
    print("\nПечатаю закрытую карту:")
    print(card2)
    print("\nПечатаю  свободную карту: ")
    print(card3)
    print("Переворачиваю свободную карту")
    card3.flip()
    print("Печатаю свободную карту после того как перевернул:")
    print(card3)







main()