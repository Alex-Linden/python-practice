def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flipped = ''

    for letter in phrase:
        if letter == to_swap.lower():
            flipped += letter.upper()
        elif letter == to_swap.upper():
            flipped += letter.lower()
        else:
            flipped += letter
    
    return flipped
            

