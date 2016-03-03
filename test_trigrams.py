"""Test functions in trigrams.py."""
import pytest


EXPECTED_CODE = ['One', 'nightit', 'was', 'on', 'the', 'twentieth', 'of',
                 'March', '1888I', 'was']


def test_tokenize():
    """Test main function."""
    from trigrams import tokenize
    given_value = "One night--it was on the twentieth of March, 1888--I was"
    assert tokenize(given_value) == EXPECTED_CODE
