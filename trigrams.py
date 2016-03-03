"""Generate random text based on model text."""
import io
import string


def read_file(path):
    """Get sample text."""
    fh = io.open(path)
    prep_list = tokenize(fh.read())
    # print(prep_list)
    return prep_list


def tokenize(data):
    """Split out sample text and remove punctuation."""
    for char in string.punctuation:
        data = data.replace(char, "")
    data_list = data.split()
    return data_list


def dictionize(list):
    """Put our text in a dict."""
    trigrams = {}
    while len(list) >= 3:
        first_key = list.pop(0)
        second_key = list[0]
        value = list[1]
        if (first_key, second_key) in trigrams.keys():
            trigrams[(first_key, second_key)].append(value)
        else:
            trigrams[(first_key, second_key)] = [value]
    print(trigrams)
    return trigrams


def main():
    """Put it all together."""
    pass


if __name__ == '__main__':
    pass


dictionize(read_file("sample.txt"))
