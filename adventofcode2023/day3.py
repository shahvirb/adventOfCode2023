import typing


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


# When accessing do something like Grid.array[r][c]
# where r is the row index and c is the col index
class Schematic:
    def __init__(self, lines: list[str]) -> None:
        self.array = [[c for c in line.strip()] for line in lines]
        self.rows = len(self.array)
        self.cols = len(self.array[0])
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
                if is_symbol(self.array[r][c]):
                    yield r, c

    def adjacent_numbers(self, row, col) -> typing.Iterator[tuple[int, int]]:
        r1, r2 = plus_minus(row, 0, self.rows)
        c1, c2 = plus_minus(col, 0, self.cols)
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if self.array[i][j].isnumeric():
                    yield i, j

    def calc_sum(self) -> int:
        for r, c in self.find_symbols():
            print("Searching for symbols around: ", r, c)
            for ar, ac in self.adjacent_numbers(r, c):
                print("Found: ", self.array[ar][ac], ar, ac)
                    
        return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    import aocinput

    lines = aocinput.read_filename_lines("day3.part1sample.input")
    sch = Schematic(lines)
    sch.calc_sum()
