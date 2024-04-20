from adventofcode2023 import aocinput
from adventofcode2023 import day1, day2, day3
import pytest

# TODO how can we use pytest-mypy to run mypy during tests?


@pytest.mark.parametrize(
    "input, solver_func, answer",
    [
        # Day 1
        ("day1", day1.solve_p1, None),
        ("day1.part2sample", day1.solve_p2, None),
        ("day1", day1.solve_p2, "day1.part2"),
        # Day 2
        ("day2.part1sample", day2.solve_p1, None),
        ("day2", day2.solve_p1, None),
        ("day2.part1sample", day2.solve_p2, "day2.part2sample"),
        ("day2", day2.solve_p2, "day2.part2"),
        # Day 3
        ("day3.part1sample", day3.solve_p1, None),
        ("day3", day3.solve_p1, None),
    ],
)
def test_solve(input, solver_func, answer):
    input_data = aocinput.read_filename_lines(input + ".input")
    assert solver_func(input_data) == int(
        aocinput.read_answer(answer if answer else input)
    )
