''' 
Strats 
    Comparison methods: 
    a. ingest into two dictionaries (k,v) as ("card", quantity)
        Iterate through keys of first dictionary and compare to keys of second dictionary
            for card, qty in a
                diff_value = str(B['card'] - A['card']) 
                If diff_value > 0:
                    output += "+" + B['card'] + " " + card # +2 Cavern of Souls
                Else:
                    output += B['card']
    b. use sets and set difference
        code/method copied from - https://stackoverflow.com/a/18860653 
        def deck_compare(a, b):
            a_keys = set(a.keys())
            b_keys = set(b.keys())
            shared_keys = a_keys.intersection(b_keys)
            added = a_keys - b_keys
            removed = b_keys - a_keys
            modified = {o : (a[o], b[o]) for o in shared_keys if a[o] != b[o]}
            same = set(o for o in shared_keys if a[o] == b[o])
            return added, removed, modified, same

        # clean print
        def clean_print(quantity, cardname):
            if quantity > 0: 
                return "+" + str(quantity) + " " + cardname
            else: 
                return str(quantity) + " " + cardname

        # define the added, removed, modified before function call and def
        output = {}
        def create_output_dict():
            # loop over each dictionary and build final output
            for card,qty in added:
                output[c] = clean_print(qty,card)
            for card,qty in removed:
                output[c] = clean_print(qty,card)
            for card in modified: 
                # get quantity from deck A get diff from deck B
                diff_value = b[card] - a[card]
                output[c] = clean_print(diff_value,card)
            
            sorted_output = dict(sorted(output.items()))
            return sorted_output


    Input: 
    - Prompt user for Deck filenames
        - If filename not found, exit
        
    - Validate file contents / format
        Nah, maybe later

    - Ingest into data structures
        4 Ancient Tomb --> x['Ancient Tomb'] = 4

    - Compare
        deck_compare(a,b)
        
    - Create output
        create_output_dict()

    - Display output


    class Card:
        properties: 
            - card_name
            - quantity (can be negative)
            - change_type as add, remove, or modify
                - negative quantity must be a remove or modify
                - positive quantity must be an add or modify

'''