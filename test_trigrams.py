# -*- coding: utf-8 -*-
"""Test functions in trigrams.py."""
import pytest

TEST_FILE = [
    ('test.txt', 'This is my test file. It is for a test.'
     'There are many like it but this one is mine.')
]


TEST_DICTIONARY = [
    ('Something. Something else. Yep!', {'Something. Something': ['else'], 'Something else': ['Yep!']})
]


# EXPECTED_CODE = ['One', 'nightit', 'was', 'on', 'the', 'twentieth', 'of',
#                  'March', '1888I', 'was']


@pytest.mark.parametrize('path, result', TEST_FILE)
def test_read_file(path, result):
    from trigrams import read_file
    assert read_file(path) == result


@pytest.mark.parametrize('text, result', TEST_FILE)
def test_trigramize(text, result):
    from trigrams import trigramize
    assert trigramize() == result


# @pytest.mark.parametrize()
# def test_rand_words():
#     from trigrams import rand_words
#     assert rand_words() == result


# @pytest.mark.parametrize('path, result', TEXT_TABLE)
# def make_new_text():
#     from trigrams import make_new_text
#     assert make_new_text() == result

