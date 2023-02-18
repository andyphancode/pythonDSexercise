def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    string1 = str(num1)
    string2 = str(num2)
    string3 = f"{string1}{string2}"
    
    for number in string3:
        if string3.count(number) % 2 != 0:
            return False
    
    return True
    