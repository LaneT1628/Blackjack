'''
Class to hold properties and methods related to the dealer or player's hand
Needed?
'''
import numpy as np

class Hand:
    '''
    Base constructur, takes an array of cards
    '''
    def __init__(self, card_array):
        self._card_array = card_array

    '''
    Method to get the card array
    '''
    def _get_card_array(self):
        return self._card_array
    
    '''
    Method to add a card to the hand
    '''
    def _add_card(self, card):
        np.append(self._card_array, card)

    '''
    Method to delete the hand
    '''
    def _del_hand(self):
        del self._card_array

    '''
    Method to calculate the hand value
    '''
    def _calculate_hand_value(self):
        value = 0
        for i in self._card_array:
            value += i.card_value
        return value

    '''
    Card array property
    '''
    card_value = property(fget = _get_card_array,
        fdel = _del_hand,
        doc = "Card Array Property")