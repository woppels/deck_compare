'''
    Deck Transform

    Take two text deckfiles and show difference between first and second input. 
    Goal is to see what cards you have to change to switch to second deck. 

    a.txt:
        4 Ancient Tomb
        2 Cavern of Souls 

        SIDEBOARD:
        1 Elvish Spirit Guide

    b.txt:
        3 Ancient Tomb
        4 Cavern of Souls

        SIDEBOARD: 
        1 Simian Spirit Guide

    Output:
        Changes to go from a.txt to b.txt:
        ---Maindeck Changes---
        -1 Ancient Tomb
        +2 Cavern of Souls

        ---Sideboard Changes---
        -1 Elvish Spirit Guide
        +1 Simian Spirit Guide
'''

# Define imports
import sys
import os
from constants import *
from funcs import *

# Print Introduction
# print(intro_text)

# A-Deck Prompt
a_filename = input("Provide the name of the first deck including .txt extension: ")
a_dict, a_sb_dict = process_file(a_filename)

# B-Deck Prompt
b_filename = input("Provide the name of the second deck including .txt extension: ")
b_dict, b_sb_dict = process_file(b_filename)

# Display Prompt
display_input = input("Would you like to see changes split by change type (add, remove, modify) - Yes/No: ")
if "yes" in display_input.lower() or "y" in display_input.lower():
    display_by_category = True
else:
    display_by_category = False 

print("Changes to go from " + a_filename + " to " + b_filename + ":")
# Build list of differences for maindeck
added, removed, modified, same = deck_compare(a_dict, b_dict)
output, a_op, r_op, m_op = create_output_dict(added, removed, modified, a_dict, b_dict)

# Build list of differences for sideboard
sb_added, sb_removed, sb_modified, sb_same = deck_compare(a_sb_dict, b_sb_dict)
sb_output, sb_a_op, sb_r_op, sb_m_op = create_output_dict(sb_added, sb_removed, sb_modified, a_sb_dict, b_sb_dict)

# Print output list
if not display_by_category:
    print("---Maindeck Changes---")
    for key in output:
        print(output[key])

    print("\n---Sideboard Changes---")
    for key in sb_output:
        print(sb_output[key])

else: 
    print("---Split by Change Type---")
    print("Additions:")
    for key in r_op:
        print(r_op[key])
    print("Removals:")
    for key in a_op:
        print(a_op[key])
    print("Modified:")
    for key in m_op:
        print(m_op[key])
    print("\n---Sideboard Changes---")
    print("Additions:")
    for key in sb_r_op:
        print(sb_r_op[key])
    print("Removals:")
    for key in sb_a_op:
        print(sb_a_op[key])
    print("Modified:")
    for key in sb_m_op:
        print(sb_m_op[key])