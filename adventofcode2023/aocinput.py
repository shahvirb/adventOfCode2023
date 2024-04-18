import glob
import pathlib

INPUTS_DIR = pathlib.Path("data")


def find(caller_path: str, ext: str):
    stem = pathlib.Path(caller_path).stem
    search_path = INPUTS_DIR / pathlib.Path(stem + ext)
    # TODO why does this need to be cast into a string?
    return glob.glob(str(search_path))


def readlines(path) -> list[str]:
    with open(path, "r") as f:
        return f.readlines()


def read_filename_lines(filename: str) -> list[str]:
    """Reads a file in the data dir with the given filename

    Args:
        filename (str): Filename of file in data dir
    """
    filepath = INPUTS_DIR / pathlib.Path(filename)
    print(filepath)
    return readlines(filepath)


def read_days_input(caller_path: str) -> list[str]:
    return readlines(find(caller_path, ".input")[0])


def read_answer(stem: str) -> str:
    filename = stem + ".answer"
    return read_filename_lines(filename)[0].strip()
