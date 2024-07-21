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
from card import Card

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
add_list, removal_list, modified_list, cardlist = create_output_dict(added, removed, modified, a_dict, b_dict)

# Build list of differences for sideboard
sb_added, sb_removed, sb_modified, sb_same = deck_compare(a_sb_dict, b_sb_dict)
sb_add_list, sb_removal_list, sb_modified_list, sb_cardlist = create_output_dict(sb_added, sb_removed, sb_modified, a_sb_dict, b_sb_dict)

# Print output list
if not display_by_category:
    print("---Maindeck Changes---")
    # for key in output:
    #     print(output[key])
    for card in cardlist: 
        print(card + " " + card.change_type)

    print("\n---Sideboard Changes---")
    # for key in sb_output:
    #     print(sb_output[key])
    for sb_card in sb_cardlist: 
        print(sb_card + " " + sb_card.change_type)

# else: 
#     print("---Split by Change Type---")
#     if len(add_list) > 0:
#         print("Additions:")
#         for card in add_list:
#             print(card)
#     if len(removal_list) > 0:
#         print("Removals:")
#         for card in add_list:
#             print(card)
#     if len(modified_list) > 0:
#         print("Modified:")
#         for card in add_list:
#             print(card)
#     print("Removals:")
#     for key in a_op:
#         print(a_op[key])
#     print("Modified:")
#     for key in m_op:
#         print(m_op[key])
#     print("\n---Sideboard Changes---")
#     print("Additions:")
#     for key in sb_r_op:
#         print(sb_r_op[key])
#     print("Removals:")
#     for key in sb_a_op:
#         print(sb_a_op[key])
#     print("Modified:")
#     for key in sb_m_op:
#         print(sb_m_op[key])