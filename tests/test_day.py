from adventofcode2023 import aocinput
from adventofcode2023 import day1, day2
from dataclasses import dataclass
from typing import Callable
import pytest

#TODO how can we use pytest-mypy to run mypy during tests?

@dataclass
class TestCase:
    input: str
    solver_func: Callable
    answer: str = None


@pytest.mark.parametrize(
    "tc",
    [
        # Day 1
        TestCase("day1", day1.solve_p1),
        TestCase("day1.part2sample", day1.solve_p2),
        TestCase("day1", day1.solve_p2, "day1.part2"),
        # Day 2
        TestCase("day2.part1sample", day2.solve_p1),
        TestCase("day2", day2.solve_p1),
        TestCase("day2.part1sample", day2.solve_p2, "day2.part2sample"),
        TestCase("day2", day2.solve_p2, "day2.part2"),
    ],
)
def test_solve(tc):
    input_data = aocinput.read_filename_lines(tc.input + ".input")
    assert tc.solver_func(input_data) == int(
        aocinput.read_answer(tc.answer if tc.answer else tc.input)
    )
