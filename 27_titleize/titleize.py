def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    phrase = phrase.lower()
    wordlist = [letter for letter in phrase]
    wordlist[0] = wordlist[0].upper()
    i = 0
    while i < len(wordlist):
        if wordlist[i] == ' ':
            wordlist[i+1] = wordlist[i+1].upper()
        i += 1
    return "".join(wordlist)