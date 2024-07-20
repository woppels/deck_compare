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
'''
def clean_print(quantity, cardname):
    if quantity > 0: 
        return "+" + str(quantity) + " " + cardname
    else: 
        return str(quantity) + " " + cardname

'''
    Build output list
'''
def create_output_dict(added, removed, modified, a, b):
    temp_output = {}
    # loop over each dictionary and build final output
    for card,qty in added:
        temp_output[card] = clean_print(qty,card)
    for card,qty in removed:
        temp_output[card] = clean_print(qty,card)
    for card in modified: 
        # get quantity from deck A get diff from deck B
        diff_value = int(b[card]) - int(a[card])
        temp_output[card] = clean_print(diff_value,card)
    
    sorted_output = dict(sorted(temp_output.items()))
    return sorted_output