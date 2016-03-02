"""Generate random text based on model text."""
import io
import string


def read_file(path):
    """Produce random text."""
    fh = io.open(path)
    return fh.read()


def tokenize(data):
    for char in string.punctuation:
        data = data.replace(char, "")
    return data.split()


if __name__ == '__main__':
    pass
