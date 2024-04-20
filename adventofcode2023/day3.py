import typing
import re

MAX_LENGTH_PARTNUMBER = 3
NUMBERS_REGEX = re.compile(r"\d+")


def is_symbol(char: str):
    """
    >>> is_symbol(".")
    False
    >>> is_symbol("1")
    False
    >>> is_symbol("*")
    True
    """
    assert len(char) == 1
    return char != "." and not char.isnumeric()


def plus_minus(x: int, limit_min: int, limit_max: int) -> tuple[int, int]:
    """
    >>> plus_minus(5, 0, 10)
    (4, 6)
    >>> plus_minus(5, 0, 5)
    (4, 5)
    >>> plus_minus(0, 0, 5)
    (0, 1)
    """
    low = max(x - 1, limit_min)
    high = min(x + 1, limit_max)
    return low, high


def within_match(match: re.Match, i: int) -> bool:
    """Checks whether i's value is within/inside the span of the match

    Args:
        match (re.Match): The regex match to test
        i (int): some integer value

    Returns:
        bool: True if i is within the span of the match
    """
    return match.start() <= i < match.end()


# When accessing do something like Grid.array[r][c]
# where r is the row index and c is the col index
class Schematic:
    def __init__(self, lines: list[str]) -> None:
        self.__array = [[c for c in line.strip()] for line in lines]
        self.__lines = lines
        # TODO do we really need both? array and lines?
        self.rows = len(self.__array)
        self.cols = len(self.__array[0])
        # Warning: don't change the array because rows and cols must then be recomputed

    # @property
    # def rows(self) -> int:
    #     return len(self.array)

    # @property
    # def cols(self) -> int:
    #     return len(self.array[0])

    def find_symbols(self) -> typing.Iterator[tuple[int, int]]:
        for r in range(self.rows):
            for c in range(self.cols):
                if is_symbol(self.__array[r][c]):
                    yield r, c

    def adjacent_digits(self, row, col) -> typing.Iterator[tuple[int, int]]:
        r1, r2 = plus_minus(row, 0, self.rows)
        c1, c2 = plus_minus(col, 0, self.cols)
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if self.__array[i][j].isnumeric():
                    yield i, j

    def find_digits(self) -> list[tuple[int, int]]:
        digits_found = []
        for r, c in self.find_symbols():
            # print("Searching for symbols around: ", r, c)
            for ar, ac in self.adjacent_digits(r, c):
                # print("Found: ", self.__array[ar][ac], ar, ac)
                digits_found.append((ar, ac))
        return digits_found

    def calc_sum(self) -> int:
        adjacent_pns = set()
        partnumbers_by_row = (
            {}
        )  # this will have keys as row numbers and values which are the regex matches of part numbers in that row
        for r, c in self.find_digits():
            if r not in partnumbers_by_row:
                partnumbers_by_row[r] = [
                    m for m in NUMBERS_REGEX.finditer(self.__lines[r])
                ]
            for match in partnumbers_by_row[r]:
                if within_match(match, c):
                    adjacent_pns.add(match)

        sum = 0
        for pn in adjacent_pns:
            sum += int(pn[0])
        return sum


def solve_p1(lines: list[str]) -> int:
    return Schematic(lines).calc_sum()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    import aocinput

    lines = aocinput.read_filename_lines("day3.part1sample.input")
    sch = Schematic(lines)
    print(sch.calc_sum())

    # for match in regex.finditer(lines[0]):
    #     print(match.span())
    # pass
