import sys
import os
from card import Card

'''
    Ingests and processes files
    Passing line that meets critera: https://stackoverflow.com/a/32953399
    Looping within line that meets criteria: https://stackoverflow.com/a/27805988
    Ignoring ValueError: https://stackoverflow.com/a/73108528 
'''
def process_file(filename): 
    dict = {}
    sb_dict = {}
    try: 
        if not os.path.isfile(filename):
            raise FileNotFoundError(filename + " file not found in current directory.")

        print("Importing " + filename + "...\n")
        with open(filename, 'r') as deck:
            for item in deck:
                # Split by first space to get number of copies of card
                try:  
                    if "SIDEBOARD:" in item.upper():
                        for sb_item in deck:
                            sb_qty, sb_cardname = sb_item.split(" ", 1)
                            sb_dict[sb_cardname.strip()] = sb_qty.strip()
                    else:
                        qty, cardname = item.split(" ", 1)
                        qty = qty.strip()
                        cardname = cardname.strip()
                        dict[cardname] = qty
                except ValueError:
                    pass
    except FileNotFoundError as not_found:
        sys.exit(not_found)
    
    return dict, sb_dict

''' 
    Deck Comparison Function
    Code/method copied from - https://stackoverflow.com/a/18860653 
'''
def deck_compare(a, b):
    a_keys = set(a.keys())
    b_keys = set(b.keys())
    shared_keys = a_keys.intersection(b_keys)
    added = b_keys - a_keys # Everything in B that is not in A
    removed = a_keys - b_keys # Everything in A that is not in B
    modified = {o : (a[o], b[o]) for o in shared_keys if a[o] != b[o]}
    same = set(o for o in shared_keys if a[o] == b[o])
    return added, removed, modified, same

'''
    Build output list
'''
def create_output_dict(added, removed, modified, a_dict, b_dict):
    add_list = []
    removal_list = []
    modified_list = []
    output_list = []
    # loop over each dictionary and build final output
    for item in added:
        # Cards that are in B, but not in A
        # Think of it as operation that needs to occur to turn A into B
        if item in a_dict:
            quantity = int(a_dict[item])
        if item in b_dict:
            quantity = int(b_dict[item])
        card = Card(item, quantity, "Addition")
        output_list.append(card)
        add_list.append(card)
    for item in removed:
        # Cards that were in A, but not in B
        # Think of it as a subtract op from A that needs to occur to create B
        if item in a_dict:
            negative_quantity = int(a_dict[item]) * -1
        if item in b_dict:
            negative_quantity = int(b_dict[item]) * -1
        card = Card(item, negative_quantity, "Removal")
        output_list.append(card)
        removal_list.append(card)
    for item in modified: 
        # get quantity from deck A get diff from deck B
        diff_value = int(b_dict[item]) - int(a_dict[item])
        card = Card(item, diff_value, "Modified")
        output_list.append(card)
        modified_list.append(card)

    return (
        sorted(add_list)
        , sorted(removal_list)
        , sorted(modified_list)
        , sorted(output_list)
    )

'''
    Takes an input list and change type to print list of cards for corresponding type
'''
def change_type_print_helper(input_list, change_type):
    if len(input_list) > 0:
        print(change_type)
        for card in input_list:
            print(card)