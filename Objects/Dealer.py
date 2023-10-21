import Deck
import Card
import numpy as np

'''
Dealer class
'''
class Dealer:
    '''
    Base dealer constructor
    '''
    def __init__(self):
        self._deck = self._generate_deck()

    '''
    Getter for the deck property of the dealer
    '''    
    def _get_deck(self):
        return self._deck

    '''
    Method to shuffle the deck
    '''
    def _shuffle_deck(self, card_deck):
        return np.random.shuffle(card_deck)

    '''
    Method to generate a deck for the dealer
    '''
    def _generate_deck(self):
        cardDeck = np.array()

        # Add all the number cards
        for i in range(0, 11, 1):
            cardDeck.append(Card(i))
            cardDeck.append(Card(i))
            cardDeck.append(Card(i))
            cardDeck.append(Card(i))
        
        # Face cards - all a value of ten
        for i in range(0, 12, 1):
            cardDeck.append(Card(10))

        return Deck(self._shuffle_deck(cardDeck))

    '''
    Card array property
    '''
    deck = property(fget = _get_deck,
        doc = "Card Array Property")