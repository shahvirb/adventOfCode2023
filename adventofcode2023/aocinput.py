import glob
import pathlib

INPUTS_DIR = pathlib.Path("inputs")


def fetch(caller_path: str):
    stem = pathlib.Path(caller_path).stem
    search_path = INPUTS_DIR / pathlib.Path(stem + ".txt")
    # TODO why does this need to be cast into a string?
    return glob.glob(str(search_path))


def readlines(path):
    with open(path, "r") as f:
        return f.readlines()
