import os
from typing import Any, Callable


def walk(folder: str, filter_func: Callable[[Any], bool]) -> list[str]:

    result = []
    folder = os.path.abspath(folder)
    for name in os.listdir(folder):
        filepath = os.path.join(folder, name)
        if os.path.isfile(filepath):
            if filter_func(filepath):
                result.append(filepath)
        elif os.path.isdir(filepath):
            result.extend(walk(filepath, filter_func))
    return result