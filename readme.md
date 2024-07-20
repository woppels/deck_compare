# deck_transform
Lazy deck comparison
-----
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
