from adventofcode2023 import day1, aocinput


def check_answer(input_name: str, solver, answer_name: str = None):
    input = aocinput.read_filename_lines(input_name + ".input")
    if not answer_name:
        answer_name = input_name
    assert solver(input) == int(aocinput.read_answer(answer_name))


def test_day1():
    from dataclasses import dataclass
    from typing import Callable

    @dataclass
    class TestCase:
        input: str
        solver_func: Callable
        answer: str = None

    TESTS = [
        TestCase("day1", day1.solve_p1),
        TestCase("day1.part2sample", day1.solve_p2),
        TestCase("day1", day1.solve_p2, "day1.part2"),
    ]
    for tc in TESTS:
        check_answer(tc.input, tc.solver_func, tc.answer)
    # TODO this is not a pytest-onic way defining and running tests.
