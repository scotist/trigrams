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
    # first_two_words(dictionary)
    make_new_text(dictionary)
    return dictionary


def make_new_text(num, dict):
    """Make a random new text using the dictionary."""
    keys = list(dict.keys())
    first_two_words = keys[random.randint(0, len(keys) - 1)]
    new_text = first_two_words.split(" ")
    while len(new_text) < num:
        new_key = "{0} {1}".format(new_text[-2], new_text[-1])
        if new_key in dict:
            value = random.choice(dict[new_key])
            new_text.append(value)
        else:
            value = keys[random.randint(0, len(keys) - 1)]
            value = value.split(" ")
            new_text = new_text + value
    return new_text


def main(num, path):
    """Print new text."""
    read = read_file(path)
    tokenize = tokenize(data)
    tuplize = tuplize(d_list)
    make = make_new_text(num, dict)
    return


main(500, "sample.txt")


# def first_two_words(dict):
#     """Create a random new text using the dictionary."""
#     random_key = random.choice(list(dict.keys()))
#     new_text = [' '.join((random_key[0], random_key[1]))]
#     create_paragraph(random_key, new_text, dict)
#     return new_text


# def create_paragraph(keys, new_text, dict):
#     """Create the whole paragraph."""
#     random_word = (keys[0], keys[1])
#     while dict.get(random_word, None):
#         if new_text[-1] is None:
#             break
#         new_text.append(random.choice(dict[random_word]))
#         random_word = (new_text[-2], new_text[-1])
#         # continue
#     print(new_text)
#     # print(dict)


if __name__ == '__main__':
    pass


read_file("sample.txt")
