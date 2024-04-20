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


# When accessing do something like Grid.array[r][c]
# where r is the row index and c is the col index
class Grid:
    def __init__(self, lines: list[str]) -> None:
        self.array = [[c for c in line.strip()] for line in lines]

    @property
    def rows(self) -> int:
        return len(self.array)

    @property
    def cols(self) -> int:
        return len(self.array[0])

    def find_symbols(self) -> typing.Iterator[tuple[int, int]]:
        for r in range(self.rows):
            for c in range(self.cols):
                if is_symbol(self.array[r][c]):
                    yield (r, c)

    def calc_sum(self) -> int:
        return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    import aocinput

    lines = aocinput.read_filename_lines("day3.part1sample.input")
    grid = Grid(lines)
    grid.find_symbols()
