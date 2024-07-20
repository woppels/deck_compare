import sys
import os

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
    added = a_keys - b_keys
    removed = b_keys - a_keys
    modified = {o : (a[o], b[o]) for o in shared_keys if a[o] != b[o]}
    same = set(o for o in shared_keys if a[o] == b[o])
    return added, removed, modified, same

'''
    Print with a "+" for additions
    Print with a "-" for subtractions
'''
def clean_print(quantity, cardname):
    if int(quantity) > 0: 
        return "+" + str(quantity) + " " + cardname
    else: 
        return str(quantity) + " " + cardname

'''
    Build output list
'''
def create_output_dict(added, removed, modified, a_dict, b_dict):
    temp_output = {}
    # loop over each dictionary and build final output
    for card in added:
        # Use the correct dictionary to get the card quantities
        positive_quantity = 0
        if card in a_dict:
            positive_quantity = int(a_dict[card])
        if card in b_dict:
            positive_quantity = int(b_dict[card])
        temp_output[card] = clean_print(positive_quantity,card)
    for card in removed:
        # Use the correct dictionary to get the card quantities
        negative_quantity = 0
        if card in a_dict:
            negative_quantity = int(a_dict[card]) * -1
        if card in b_dict:
            negative_quantity = int(b_dict[card]) * -1
        temp_output[card] = clean_print(negative_quantity, card)
    for card in modified: 
        # get quantity from deck A get diff from deck B
        diff_value = int(b_dict[card]) - int(a_dict[card])
        temp_output[card] = clean_print(diff_value,card)
    
    sorted_output = dict(sorted(temp_output.items()))
    return sorted_output