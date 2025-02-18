import os


def has_even_bytesize(path: str):
    filesize = os.path.getsize(path)
    return filesize % 2 == 0


def has_every_vowel(path: str):
    name = os.path.basename(path).lower()
    return ('a' in name) and ('e' in name) and ('i' in name) and ('o' in name) and ('u' in name)


def is_size_more_than(path: str, maxsize: int = 1000):
    filesize = os.path.getsize(path)
    return filesize > maxsize
