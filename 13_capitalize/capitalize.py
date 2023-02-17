def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    phraselist = list(phrase)
    phraselist[0] = phraselist[0].upper()
    return "".join(phraselist)