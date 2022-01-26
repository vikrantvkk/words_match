import pytest
import sys, os

sys.path.append(os.path.abspath("."))

from utils import sort_letters_in_word
from words import Words

test_functionality_data = [
    (["helloworld", "foo", "bar", "stylight_team", "seo"], "eos", ['seo']),
    (["helloworld", "foo", "bar", "stylight_team", "seo"], "stylightteam_", ['stylight_team']),
    (["helloworld", "foo", "bar", "stylight_team", "seo"], "styligh", [])
]

test_sort_letters_in_word_data = [
    ("stylight_team", "_aeghilmsttty"),
    ("stylightteam_", "_aeghilmsttty"),
    ("1wb", "1bw"), ("!", "!"), ("@", "@"), ("#", "#"), ("$", "$"), ("%", "%"), ("^", "^"), ("&", "&"), ("*", "*"),
    ("(", "("), (")", ")"), ("-", "-"), ("+", "+"), ("=", "="), ("{", "{"), ("}", "}"), ("[", "["), ("]", "]"),
    ("\\", "\\"), ("|", "|"), (":", ":"), (";", ";"), ('"', '"'), ("'", "'"), ("<", "<"), (">", ">"), (".", "."),
    (",", ","), ("?", "?"), ("/", "/")
]

test_append_word_to_hash_data = [
    ("test_word", "test_word", 1)
]


@pytest.mark.parametrize("words, search_string, result", test_functionality_data)
def test_functionality(words, search_string, result):
    words = Words(words)
    assert words.find_word(search_string) == result


@pytest.mark.parametrize("word, expected_value", test_sort_letters_in_word_data)
def test_sort_letters_in_word(word, expected_value):
    res = sort_letters_in_word(word)
    assert res == expected_value


@pytest.mark.parametrize("word, expected_value", test_sort_letters_in_word_data)
def test_append_word_to_hash_set(word, expected_value):
    res = sort_letters_in_word(word)
    assert res == expected_value


@pytest.mark.parametrize("word, expected_value, words_len_after_addition", test_append_word_to_hash_data)
def test_append_word_to_hash_set(word, expected_value, words_len_after_addition):
    words = Words([])
    len_before = len(words.find_word(word))
    words.append_word_to_hash_set(word)
    word_key = sort_letters_in_word(word)
    assert expected_value in words.words_hash[word_key]
    assert len(words.words_hash[word_key]) - len_before == 1
