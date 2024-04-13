
import glob
import pathlib
INPUTS_DIR = pathlib.Path("inputs")

def fetch(caller_path: str):
    stem = pathlib.Path(caller_path).stem
    search_path = INPUTS_DIR / pathlib.Path(stem + ".txt")
    # TODO why does this need to be cast into a string?
    glob.glob(str(search_path))


# def get_callers_name():
#     import inspect
#     filename = inspect.stack()[1].filename
#     print(filename)