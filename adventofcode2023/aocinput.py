import glob
import pathlib

INPUTS_DIR = pathlib.Path("data")


def find(caller_path: str, ext: str):
    stem = pathlib.Path(caller_path).stem
    search_path = INPUTS_DIR / pathlib.Path(stem + ext)
    # TODO why does this need to be cast into a string?
    return glob.glob(str(search_path))


def readlines(path):
    with open(path, "r") as f:
        return f.readlines()


def read_days_input(caller_path: str):
    return readlines(find(caller_path, ".input")[0])

def read_answer(stem: str) -> str:
    search_path = INPUTS_DIR / pathlib.Path(stem + ".answer")
    filepath = glob.glob(str(search_path))[0]
    return readlines(filepath)[0].strip()