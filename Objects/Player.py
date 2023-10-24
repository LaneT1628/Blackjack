'''
Player class
'''

class Player:
    '''
    Base constructor method
    '''
    def __init__(self, hand):
        self._hand = hand

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