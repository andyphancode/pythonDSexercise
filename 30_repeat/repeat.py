def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """

    res = []
    i = 0
    if type(num) != str:
        if num >= 0:
            while i < float(num):
                res.append(phrase)
                i += 1
            return "".join(res)
    else:
        return None
