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

class Hand:
    """рука : набор катра в руках """

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<пусто>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    """колода"""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
    
    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Не могу больше сдавать:",
                                 "карты закончились")        

def main():
    deck1 = Deck()
    print("Создана новая колода.")
    print("Вто эта колода.")
    print(deck1)

    deck1.populate()
    print("\nВ колоде появились карты.")
    print("Вот так теперь она выглядит:")
    print(deck1) 

    deck1.shuffle()
    print("\nКолода перемешана.")
    print("Вот так она выглядит теперь: ")
    print(deck1)


    my_hand = Hand()
    your_hand = Hand()
    hands =[my_hand , your_hand]
    deck1.deal(hands, per_hand = 5)
    print("\nМне и вам на руки роздано по 5 кард.")
    print("У меня на руках:")
    print(my_hand)
    print("У вас на руках:")
    print(your_hand)
    print("Осталось в колоде:")
    print(deck1)

    deck1.clear()
    print("\nКолода очищена.")
    print("Вот так она виглядит теперь:", deck1)

main()   
