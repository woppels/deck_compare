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
a_dict, a_sb_dict = process_file(a_filename)

# B-Deck Prompt
b_filename = input("Provide the name of the second deck including .txt extension: ")
b_dict, b_sb_dict = process_file(b_filename)

print("Changes to go from " + a_filename + " to " + b_filename + ":")
print("---Maindeck Changes---")
# Build list of differences for maindeck
added, removed, modified, same = deck_compare(a_dict, b_dict)
output = create_output_dict(added, removed, modified, a_dict, b_dict)

# Build list of differences for sideboard
sb_added, sb_removed, sb_modified, sb_same = deck_compare(a_sb_dict, b_sb_dict)
sb_output = create_output_dict(sb_added, sb_removed, sb_modified, a_sb_dict, b_sb_dict)

# Print output list
for key in output:
    print(output[key])

print("\n---Sideboard Changes---")
for key in sb_output:
    print(sb_output[key])