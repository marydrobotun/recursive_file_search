import os
from typing import Any, Callable


def walk(folder: str, filter_func: Callable[[Any], bool]) -> list[str]:
    """
    Recursively walk through a directory and collect file paths that satisfy a given filter function.

    :param folder: The path to the directory to traverse.
    :type folder: str
    :param filter_func: A function that takes a file path and returns a boolean indicating whether
                       the file should be included in the result.
    :type filter_func: Callable[[Any], bool]
    :return: A list of file paths that satisfy the filter function.
    :rtype: list[str]
    """
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
