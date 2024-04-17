from adventofcode2023 import day1, aocinput
from dataclasses import dataclass
from typing import Callable

@dataclass
class TestCase:
    input: str
    solver_func: Callable
    answer: str = None

    def exec(self):
        input = aocinput.read_filename_lines(self.input + ".input")
        answer_name = self.answer if self.answer else self.input
        assert self.solver_func(input) == int(aocinput.read_answer(answer_name))


def test_day1():
    TESTS = [
        TestCase("day1", day1.solve_p1),
        TestCase("day1.part2sample", day1.solve_p2),
        TestCase("day1", day1.solve_p2, "day1.part2"),
    ]
    for tc in TESTS:
        tc.exec()
    # TODO this is not a pytest-onic way defining and running tests.
