# deck_transform
Lazy deck comparison
-----
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

    Dev Notes:
        - Within a file, deck order doesn't matter. 
        - Sideboard must be within file as SIDEBOARD:
        
    Add at some point 
        - Refactor / fix exception classes
        - Save to file as an option:
            naming would be like a.txt + "_to_" b.txt
        - File Validation:
            - Use longest card name x200 for battle of wits testing purposes (limit filesize to this)
            - Text files only
        - Host on site for drag and drop or paste input
        - Update code to take file input if through a lambda