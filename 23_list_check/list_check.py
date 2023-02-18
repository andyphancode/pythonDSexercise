def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    listcount = 0
    for item in lst:
        if type(item) == list:
            listcount += 1
    if listcount == len(lst):
        return True
    else:
        return False
