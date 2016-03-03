"""Generate random text based on model text."""
import io
import string


def read_file(path):
    """Produce random text."""
    fh = io.open(path)
    tokenize(fh.read())
    return fh.read()


def tokenize(data):
	"""Splits out sample text and removes punctuation."""
    for char in string.punctuation:
        data = data.replace(char, "")
    data_list = data.split()
    print(data_list)
    return data_list


def tuplize():
	"""Convert list to a list of tuples."""


def dictionize():
    """Put our text in a dict."""


if __name__ == '__main__':
    pass


read_file("sample.txt")
