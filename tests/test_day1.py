from adventofcode2023 import day1, aocinput


def check_answer(stem: str, solver):
    input = aocinput.read_filename_lines(stem + ".input")
    assert solver(input) == int(aocinput.read_answer(stem))


def test_day1():
    TESTS = [("day1", day1.solve_p1), ("day1.part2sample", day1.solve_p2)]
    for filestem, solver_func in TESTS:
        check_answer(filestem, solver_func)
    # TODO this is not a pytest-onic way defining and running tests.
