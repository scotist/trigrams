"""Generate random text based on model text."""
import io
import string
import random


def read_file(path):
    """Get sample text."""
    fh = io.open(path)
    prep_list = tokenize(fh.read())
    # print(prep_list)
    return prep_list


def tokenize(data):
    """Split out sample text and removes punctuation."""
    for char in string.punctuation:
        data = data.replace(char, "")
    data_list = data.split()
    tuplize(data_list)
    return data_list


def tuplize(d_list):
    """Convert list to a list of tuples."""
    dictionary = {}
    for i in range(len(d_list) - 2):
        dict_keys = (d_list[i], d_list[i + 1])
        dictionary.setdefault(dict_keys, []).append(d_list[i + 2])
    first_two_words(dictionary)
    return dictionary


def first_two_words(dict):
    """Create a random paragraph using the dictionary."""
    random_key = random.choice(list(dict.keys()))
    start_paragraph = [' '.join((random_key[0], random_key[1]))]
    create_paragraph(random_key, start_paragraph, dict)
    return start_paragraph


def create_paragraph(keys, para, dict):
    """Create the whole paragraph."""
    # print(para)
    random_word = (keys[0], keys[1])
    while dict.get(random_word, None):
        if para[-1] is None:
            break
        para.append(random.choice(dict[random_word]))
        random_word = (para[-2], para[-1])
        # continue
    print(para)


if __name__ == '__main__':
    pass


read_file("sample.txt")
