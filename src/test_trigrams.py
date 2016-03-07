# -*- coding: utf-8 -*-
"""Test functions in trigrams.py."""
import pytest

TEST_FILE = [
    ("text.txt", "This is my test file. It is for a test. There are many like it but this one is mine.")
]


TEST_DICTIONARY = [
    ("Something. Something else. Yep!", {("Something.", "Something"): ["else."], ("Something", "else."): ["Yep!"]})
]


@pytest.mark.parametrize('path, result', TEST_FILE)
def test_read_file(path, result):
    """Test to see that correct file path is openned."""
    from trigrams import read_file
    assert read_file(path) == result


@pytest.mark.parametrize('text, result', TEST_DICTIONARY)
def test_trigramize(text, result):
    """Test to see that files are put into dict correctly."""
    from trigrams import trigramize
    assert trigramize(text) == result
