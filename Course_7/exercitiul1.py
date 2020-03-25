from random import shuffle

class CardValueError(Exception):
    pass
    
class DuplicateCardError(Exception):
    pass

class Card:
    symbols = ["inima rosie", "inima neagra", "trefla", "romb"]
    values = ["A", "J", "Q", "K"]
    for val in range(2,11):
        values.append(str(val))
        
    def __init__(self, value, symbol):
        if self.sanity_checks(value, symbol):
            self.symbol = symbol
            self.value = value
        else:
            exception_text = "\nCartea introdusa este invalida: %s %s\n" % \
            (value, symbol)
            exception_text += "Valoarile valide sunt: %s\n" % Card.values
            exception_text += "Simbolurile valide sunt: %s\n" % Card.symbols
            raise CardValueError(exception_text)
            
    def sanity_checks(self, value, symbol):
        if symbol not in Card.symbols or value not in Card.values:
            return False
        return True
        
    def __repr__(self):
        return self.value + " " + self.symbol

class Deck:
    cards = []
    
    def __init__(self, name):
        self.name = name
        
    def is_duplicate_card(self, card):
        for c in Deck.cards:
            if card.symbol == c.symbol and card.value == c.value:
                return True
        return False
        
    def add_card(self, card):
        if not self.is_duplicate_card(card):
            Deck.cards.append(card)
        else:
            raise DuplicateCardError("Cartea exista deja in pachet")
        
    def remove_card(self, card):
        if self.is_duplicate_card(card):
            for c in Deck.cards:
                if card.symbol == c.symbol and card.value == c.value:
                    Deck.cards.remove(c)
                    break
        else:
            print("Cartea nu exista in pachet")
            
    def shuffle_deck(self):
        shuffle(Deck.cards)

def create_full_deck():
    deck = Deck("Full deck")
    for symbol in Card.symbols:
        for value in Card.values:
            deck.add_card(Card(value, symbol))
    return deck
            
if __name__ == "__main__":
    deck = create_full_deck()
    deck.shuffle_deck()
    print(deck.cards)
    deck.remove_card(Card("2", "trefla"))
    print(deck.cards)
    deck.remove_card(Card("2", "trefla"))
    print(deck.cards)
    deck2 = Deck("empty deck")
    print(deck2.cards)