from dataclasses import dataclass


# @dataclass(init=False)
# class GameSetString:
#     red: int
#     green: int
#     blue: int

#     def __init__(self, string: str) -> None:
#         self.red = 0
#         self.green = 0
#         self.blue = 0


def object_counts(string: str) -> dict:
    """Returns the counts of the objects as a dict

    Args:
        string (str): string to be parsed

    Returns:
        dict: A dict where the keys are object names and values are the counts

    >>> object_counts("3 blue, 4 red")
    {'blue': 3, 'red': 4}
    """
    rd = {}
    string = string.strip()
    for obj_string in string.split(","):
        parts = obj_string.strip().split(" ")
        assert len(parts) == 2
        rd[parts[1]] = int(parts[0])
    return rd


@dataclass(init=False)
class Bag:
    cubes: int = 0
    __initial: int = 0

    def __init__(self, initial: int) -> None:
        self.__initial = initial
        self.cubes = initial

    def draw(self, n) -> int:
        """Draw some cubes from the bag and return the number remaining

        Args:
            n (_type_): number to withdraw

        Returns:
            int: remaining cubes in the bag
        """
        self.cubes -= n
        return self.cubes

    def reset(self) -> None:
        self.cubes = self.__initial


class Game:
    def __init__(self) -> None:
        self.reds = Bag(12)
        self.greens = Bag(13)
        self.blues = Bag(14)

    def reset_bags(self) -> None:
        self.reds.reset()
        self.greens.reset()
        self.blues.reset()

    def play_set(self, object_counts: dict) -> bool:
        self.reds.draw(object_counts.get("red", 0))
        self.greens.draw(object_counts.get("green", 0))
        self.blues.draw(object_counts.get("blue", 0))
        valid: bool = (
            self.reds.cubes >= 0 and self.greens.cubes >= 0 and self.blues.cubes >= 0
        )
        self.reset_bags()
        return valid


def solve_line(line: str) -> int:
    """Solves the line and returns the game id if the game was viable

    Args:
        line (str): input line text

    Returns:
        int: Returns the game ID if the game was viable otherwise 0

    >>> solve_line("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    1
    >>> solve_line("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
    0
    """
    colon_split_line = line.split(":")
    assert len(colon_split_line) == 2
    id = int(colon_split_line[0].split(" ")[-1])
    game = Game()

    sets = colon_split_line[1].split(";")
    valid = True
    for set in sets:
        valid = game.play_set(object_counts(set))
        if not valid:
            break
    return id if valid else 0


def solve_p1(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        sum += solve_line(line)
    return sum


def solve_p2(lines) -> int:
    return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    import aocinput

    # lines = aocinput.read_filename_lines("day2.part1sample.input")

    # lines = aocinput.read_days_input(__file__)
    # print(solve_p1(lines))
    # print(solve_p2(lines))
