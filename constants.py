# Intro text
intro_text = (
        'Welcome to Deck Transform\n\n'
        'Take two text deckfiles and show difference between first and second input.\n'
        'Use to see what cards you have to change to switch to second deck.\n'

    'A.txt:\n'
        '\t4 Ancient Tomb\n'
        '\t2 Cavern of Souls\n' 

    'B.txt:\n'
        '\t3 Ancient Tomb\n'
        '\t4 Cavern of Souls\n'

    'Output:\n'
        '\t-1 Ancient Tomb\n'
        '\t+2 Cavern of Souls\n'
)

split_char = " "
split_num = 1