import typing


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
    # TODO why calculate all the digits in the line? We just need the first and the last.
    assert len(d) > 0
    return d[0] * 10 + d[-1]


def solve(lines, line_preprocessor=None):
    sum = 0
    for line in lines:
        sum += line_int(line_preprocessor(line) if line_preprocessor else line)
    return sum


def solve_p1(lines):
    return solve(lines)


def replace_at(line: str, a: str, idx: int, b: str) -> str:
    """
    >>> replace_at("one two three", "two", 4, "2")
    'one 2 three'
    """
    return line[:idx] + b + line[idx + len(a) :]
    # return line[0:idx-1] + b + line[idx+1:len(line)-len(a)+1]


def words_to_digits(line: str) -> str:
    """
    >>> words_to_digits("eightwothree")
    '8wo3'
    """
    from dataclasses import dataclass

    @dataclass
    class WordNumber:
        word: str
        value_str: str

    DIGITS = [
        WordNumber("one", "1"),
        WordNumber("two", "2"),
        WordNumber("three", "3"),
        WordNumber("four", "4"),
        WordNumber("five", "5"),
        WordNumber("six", "6"),
        WordNumber("seven", "7"),
        WordNumber("eight", "8"),
        WordNumber("nine", "9"),
    ]

    @dataclass
    class DigitOccurence:
        word_number: WordNumber
        found_idx: int

    while True:
        occurences: typing.List[DigitOccurence] = []
        for d in DIGITS:
            found = line.find(d.word)
            if found >= 0:
                occurences.append(DigitOccurence(d, found))
        if occurences:
            first = sorted(occurences, key=lambda x: x.found_idx)[0]
            line = replace_at(
                line,
                first.word_number.word,
                first.found_idx,
                first.word_number.value_str,
            )
        else:
            return line

    return None


def solve_p2(lines):
    return solve(lines, line_preprocessor=words_to_digits)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    import aocinput

    lines = aocinput.read_days_input(__file__)
    print(solve_p1(lines))
    print(solve_p2(lines))

    p2sample = aocinput.read_filename_lines("day1.part2sample.input")
    print(solve_p2(p2sample))
