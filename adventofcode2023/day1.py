from dataclasses import dataclass


@dataclass
class WordNumber:
    word: str
    value_str: str


DIGITS_P1 = [WordNumber(str(x), str(x)) for x in range(10)]
DIGITS_P2 = DIGITS_P1 + [
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


def line_int(line: str, digits: list[WordNumber]) -> int:
    """
    >>> line_int("he3llo4 wo8rld!", DIGITS_P1)
    38
    >>> line_int("threehqv2", DIGITS_P1)
    22
    >>> line_int("threehqv2", DIGITS_P2)
    32
    >>> line_int("eightwo", DIGITS_P2)
    82
    """
    first_found: str = ""
    last_found: str = ""
    string: str = line
    while len(string) > 0:
        for d in digits:
            if string.startswith(d.word):
                last_found = d.value_str
                if not first_found:
                    first_found = d.value_str
        string = string[1:]
    return int(first_found + last_found)


def solve(lines: list[str], digits: list[WordNumber]) -> int:
    sum = 0
    for line in lines:
        sum += line_int(line, digits)
    return sum


def solve_p1(lines: list[str]) -> int:
    return solve(lines, DIGITS_P1)


def solve_p2(lines) -> int:
    return solve(lines, DIGITS_P2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    import aocinput

    lines = aocinput.read_days_input(__file__)
    print(solve_p1(lines))
    print(solve_p2(lines))

    # p2sample = aocinput.read_filename_lines("day1.part2sample.input")
    # print(solve_p2(p2sample))
