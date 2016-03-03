"""Generate random text based on model text."""
import io
import string


def read_file(path):
    """Produce random text."""
    fh = io.open(path)
    tokenize(fh.read())
    return fh.read()


def tokenize(data):
    """Split out sample text and removes punctuation."""
    for char in string.punctuation:
        data = data.replace(char, "")
    data_list = data.split()
    tuplize(data_list)
    return data_list


def tuplize(d_list):
    """Convert list to a list of tuples."""
    d = {}
    for i in range(len(d_list) - 2):
        tup = (d_list[i], d_list[i + 1])
        d.setdefault(tup, []).append(d_list[i + 2])
        # if d[tup]:
        #     d[tup].append(d_list[i + 2])
        # else:
        #     d[tup] = [d_list[i + 2]]
    print(d)
    return d

if __name__ == '__main__':
    pass


read_file("sample.txt")
