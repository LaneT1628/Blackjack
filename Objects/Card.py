'''
Card class
''' 
class Card:
    '''
    Generic constructor to give the card a value
    '''
    def __init__(self, card_value):
        self._card_value = card_value

    '''
    Getter for the card_value property
    '''
    def _get_card_value(self):
        return self._card_value

    '''
    Defining the property value
    '''
    card_value = property(fget=_get_card_value,
    doc="Card Value Property.")
