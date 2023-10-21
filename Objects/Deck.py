'''
Deck class - holds cards
'''
class Deck:
    '''
    Base constructor for a card deck
    '''
    def __init__(self, card_array):
        self._card_array = card_array

    '''
    Card array getter
    '''
    def _get_card_array(self):
        return self._card_array
    
    '''
    Card array setter
    '''
    def _set_card_array(self, card_array):
        self.card_array = card_array

    def _delete_card_array(self):
        del self.card_array

    '''
    Card array property
    '''
    card_array = property(fget = _get_card_array,
        fset = _set_card_array,
        fdel = _delete_card_array,
        doc = "Card Array Property")
