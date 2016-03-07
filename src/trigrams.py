# -*- coding; utf-8 -*-
"""Generate random text based on model text."""
import io
import random
import sys


def read_file(path):
    """Read a file and return the text."""
    file = io.open(path, encoding='utf-8')
    text = file.read()
    file.close()
    return text


def trigramize(text):
    """Convert text to a dictionary for later use."""
    dictionary = {}
    text = text.replace('\n', ' ')
    while len(text.split(" ")) > 2:
        split_text = text.split(" ", 3)
        keys = (split_text[0], split_text[1])
        value = split_text[2]
        if keys not in dictionary:
            dictionary[keys] = [value]
        else:
            new_value = dictionary.get(keys)
            new_value.append(value)
            dictionary[keys] = new_value
        length = len(split_text[0]) + 1
        text = text[length:]
    return dictionary


def rand_words(dictionary, new_text):
    """Begin new text with random key from dictionary."""
    random_key = random.choice(list(dictionary.keys()))
    first_word = str(random_key[0])
    second_word = str(random_key[1])
    third_word = random.choice(dictionary[random_key])
    new_text.extend([first_word, second_word, third_word])
    return new_text


def make_new_text(dictionary, n):
    """Make a new text using random entries from the dictionary."""
    new_text = []
    rand_words(dictionary, new_text)
    while len(new_text) < n:
        latest = (new_text[-2], new_text[-1])
        if latest in dictionary:
            fetch_latest = random.choice(dictionary[latest])
            new_text.append(fetch_latest)
        else:
            rand_words(dictionary, new_text)
    return " ".join(new_text)


def main(path, n):
    """Process trigramize and make_new_text to create new text from file."""
    text = read_file(path)
    trigrams = trigramize(text)
    product = make_new_text(trigrams, n)
    print(product)
    sys.exit(0)


if __name__ == "__main__":
    path = sys.argv[1]
    n = sys.argv[2]
    main(path, int(n))
