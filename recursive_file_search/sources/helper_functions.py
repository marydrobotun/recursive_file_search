import os


def has_even_bytesize(path: str):
    """
    Check if the file at the given path has an even byte size.

    :param path: The path to the file.
    :type path: str
    :return: True if the file size is even, False otherwise.
    :rtype: bool
    """
    filesize = os.path.getsize(path)
    return filesize % 2 == 0


def has_every_vowel(path: str):
    """
    Check if the filename (without extension) contains every vowel (a, e, i, o, u).

    :param path: The path to the file.
    :type path: str
    :return: True if the filename contains all vowels, False otherwise.
    :rtype: bool
    """
    name = os.path.basename(path).lower()
    return ('a' in name) and ('e' in name) and ('i' in name) and ('o' in name) and ('u' in name)


def is_size_more_than(path: str, minsize: int = 1000):
    """
    Check if the file size is greater than the specified minimum size.

    :param path: The path to the file.
    :type path: str
    :param minsize: The minimum size threshold (default is 1000 bytes).
    :type minsize: int
    :return: True if the file size is greater than minsize, False otherwise.
    :rtype: bool
    """
    filesize = os.path.getsize(path)
    return filesize > minsize

def is_size_less_than(path: str, maxsize: int = 1000):
    """
    Check if the file size is less than the specified maximum size.

    :param path: The path to the file.
    :type path: str
    :param maxsize: The maximum size threshold (default is 1000 bytes).
    :type maxsize: int
    :return: True if the file size is less than maxsize, False otherwise.
    :rtype: bool
    """
    filesize = os.path.getsize(path)
    print(filesize)
    return filesize < maxsize
