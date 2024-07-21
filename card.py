'''
class Card:
    properties: 
        - card_name
        - quantity (can be negative)
        - change_type as add, remove, or modify
            - negative quantity must be a remove or modify
            - positive quantity must be an add or modify
'''
import functools
from functools import total_ordering

'''
    Print with a "+" for additions
    Print with a "-" for subtractions
'''
def print_quantity(quantity):
    if int(quantity) > 0: 
        return "+" + str(quantity)
    else: 
        return str(quantity)

'''
    Print quantity and card name
    Example: +4 Ancient Tomb
'''
def print_quantity_and_card(quantity, card_name):
    return print_quantity(quantity) + " " + card_name

@total_ordering
class Card: 
    def __init__(self, card_name, quantity, change_type):
        self.card_name = card_name
        self.quantity = quantity
        self.change_type = change_type
    
    def __str__(self): 
        if int(self.quantity) > 0: 
            return f"+{self.quantity} {self.card_name}"
        else: 
            return f"{self.quantity} {self.card_name}"
        
    def __add__(self, val2):
        return f"{self.quantity} {self.card_name}{val2}" 
    
    def __lt__(self, obj):
        return ((self.card_name) < (obj.card_name))

    def __gt__(self, obj):
        return ((self.card_name) > (obj.card_name))

    def __le__(self, obj):
        return ((self.card_name) <= (obj.card_name))

    def __ge__(self, obj):
        return ((self.card_name) >= (obj.card_name))

    def __eq__(self, obj):
        return (self.card_name == obj.card_name)

    def __repr__(self):
        return str((self.card_name, self.card_name))