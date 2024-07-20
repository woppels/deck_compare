'''
    Deck Transform

    Take two text deckfiles and show difference between first and second input. 
    Goal is to see what cards you have to change to switch to second deck. 

    a.txt:
        4 Ancient Tomb
        2 Cavern of Souls 

    b.txt:
        3 Ancient Tomb
        4 Cavern of Souls

    Output:
        -1 Ancient Tomb
        +2 Cavern of Souls

    Dev Notes:
        - Within a file, deck order doesn't matter. 
        - System will not separate sideboard out for now
        
    Add at some point
        - Sideboard comparison not yet supported within same file. 
        - Rename methods to be private
        - Refactor / fix exception classes
        - the sideboard must be sectioned below "SIDEBOARD:" and will be its own output
        - Save to file as an option:
            naming would be like a.txt + "_to_" b.txt
'''

# Define imports
import sys
import os
from constants import *
from funcs import *

# Print Introduction
print(intro_text)

# A-Deck Prompt
a_filename = input("Provide the name of the first deck including .txt extension: ")
try: 
    if not os.path.isfile(a_filename):
        raise FileNotFoundError(a_filename + " file not found in current directory.")

    print("Importing " + a_filename + "...\n")
    a_dict = {}
    a_sb_dict = {}
    with open(a_filename, 'r') as deck_a:
        for item in deck_a:
            # Split by first space to get number of copies of card
            try:  
                if "SIDEBOARD:" in item:
                    for sb_item in deck_a:
                        sb_qty, sb_cardname = sb_item.split(" ", 1)
                        a_sb_dict[sb_cardname.strip()] = sb_qty.strip()
                else:
                    qty, cardname = item.split(" ", 1)
                    qty = qty.strip()
                    cardname = cardname.strip()
                    a_dict[cardname] = qty
            except ValueError:
                pass
except FileNotFoundError as not_found:
    sys.exit(not_found)

# B-Deck Prompt
b_filename = input("Provide the name of the second deck including .txt extension: ")
try: 
    if not os.path.isfile(b_filename):
        raise FileNotFoundError(b_filename + " file not found in current directory.")

    print("Importing " + b_filename + "...\n")
    b_dict = {}
    with open(b_filename, 'r') as deck_b:
        for item in deck_b:
            # split by first space to get number of copies of card
            qty, cardname = item.split(" ", 1)
            qty = qty.strip()
            cardname = cardname.strip()
            b_dict[cardname] = qty
except FileNotFoundError as not_found:
    sys.exit(not_found)

print("Changes to go from " + a_filename + " to " + b_filename + ":")
# Build list of differences
added, removed, modified, same = deck_compare(a_dict, b_dict)

print("Added")
for key in added:
    print(key)
print("Removed")
for key in removed: 
    print(key)
for key in modified: 
    print(key, modified[key])
for key in a_sb_dict: 
    print(key)

# Build output list
output = create_output_dict(added, removed, modified, a_dict, b_dict)

# Print output list
for key in output:
    print(output[key])