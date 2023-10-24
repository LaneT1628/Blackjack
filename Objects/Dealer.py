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
    def __init__(self, hand):
        self._deck = self._generate_deck()
        self._hand = hand

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
        card_deck = np.array()

        # Add all the number cards
        for i in range(0, 11, 1):
            for j in range(4):
                np.append(card_deck, Card(i))
        
        # Face cards - all a value of ten
        for i in range(0, 12, 1):
            np.append(card_deck, Card(10))

        return Deck(self._shuffle_deck(card_deck))
    
    '''
    Card array property
    '''
    deck = property(fget = _get_deck,
        doc = "Card Array Property")
    
    '''
    Getter for the hand property
    '''
    def _get_hand(self):
        return self._hand
    
    '''
    Setter for the hand property
    '''
    def _set_hand(self, hand):
        self._hand = hand

    '''
    Method to delete the hand property
    '''
    def _del_hand(self):
        del self._hand

    '''
    Hand property
    '''
    hand = property(fget = _get_hand,
        fset = _set_hand,
        fdel = _del_hand,
        doc = "Hand Property")
    
    '''
    Method to add a card to the player hand
    '''
    def _add_card_to_hand(self, card):
        self._hand._add_card(card)
    
    '''
    Method to return the player hand value
    '''
    def _calculate_player_value(self):
        return self._hand._calculate_hand_value()