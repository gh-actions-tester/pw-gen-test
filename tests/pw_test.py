import pytest
import re

from passwords import generate_password


def has_special_characters_regex(string):
    pattern = r'[^a-zA-Z0-9\s]'
    if re.search(pattern, string):
        return True
    return False

@pytest.mark.parametrize(
    "length",
    [
        (5),
        (4),
        (26)
    ],
)
def test_rows_even_numbers(length):
    iterator = generate_password(length)
    assert len(iterator) == length


def test_lowercase_ascii():
    password = generate_password(50)
    assert any(char.islower() for char in password)


def test_uppercase_ascii():
    password = generate_password(50)
    assert any(char.isupper() for char in password)


def test_special_characters():
    password = generate_password(50)
    assert has_special_characters_regex(password)


def test_docstring():
    assert generate_password.__doc__