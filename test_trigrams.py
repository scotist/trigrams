"""Test functions in trigrams.py."""
import pytest


EXPECTED_CODE = ['One', 'nightit', 'was', 'on', 'the', 'twentieth', 'of',
                 'March', '1888I', 'was']


def test_tokenize():
    """Test main function."""
    from trigrams import tokenize
    GIVEN_VALUE = "One night--it was on the twentieth of March, 1888--I was"
    assert tokenize(GIVEN_VALUE) == EXPECTED_CODE
