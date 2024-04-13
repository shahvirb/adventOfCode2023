def digits(string: str) -> list[int]:
    """A list of digits in the string

    Args:
        string (str): input string

    Returns:
        list[int]: a list of only the digits in the string
        
    >>> digits("he3llo4 wo8rld!")
    [3, 4, 8]
    """
    digits = []
    for c in string:
        if c.isnumeric():
            digits.append(int(c))
    return digits


def line_int(line: str) -> int:
    """
    >>> line_int("he3llo4 wo8rld!")
    38
    >>> line_int("threehqv2")
    22
    """
    d = digits(line)
    assert len(d) > 0
    return d[0]*10 + d[-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    import aocinput
    inputs = aocinput.fetch(__file__)
    lines = aocinput.readlines(inputs[0])
    sum = 0
    for line in lines:
        sum += line_int(line)
    print(sum)
    #TODO implement a test day day1 part 1. The answer should be 54388