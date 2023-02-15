def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    swapped = [letter for letter in phrase]
    caseswap = []

    if to_swap.isupper():
        for letter in swapped:
            if letter == to_swap:
                caseswap.append(letter.lower())
            elif letter == to_swap.lower():
                caseswap.append(letter.upper())
            else:
                caseswap.append(letter)
        return ''.join(caseswap)
    else:
        for letter in swapped:
            if letter == to_swap:
                caseswap.append(letter.upper())
            elif letter == to_swap.upper():
                caseswap.append(letter.lower())
            else:
                caseswap.append(letter)
        return ''.join(caseswap)