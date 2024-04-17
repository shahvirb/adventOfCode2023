from adventofcode2023 import day1, aocinput
from dataclasses import dataclass
from typing import Callable
import pytest


@dataclass
class TestCase:
    input: str
    solver_func: Callable
    answer: str = None


@pytest.mark.parametrize(
    "tc",
    [
        TestCase("day1", day1.solve_p1),
        TestCase("day1.part2sample", day1.solve_p2),
        TestCase("day1", day1.solve_p2, "day1.part2"),
    ],
)
def test_solve(tc):
    input_data = aocinput.read_filename_lines(tc.input + ".input")
    assert tc.solver_func(input_data) == int(
        aocinput.read_answer(tc.answer if tc.answer else tc.input)
    )
