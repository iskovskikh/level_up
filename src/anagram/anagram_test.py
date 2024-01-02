from anagram.anagram import is_anagram
from decorator.decorator import time_it



def test_is_anagram():

    test_cases = [
        ("tinkoff", "ffoknit", True),
        ("tinkoff", "tinkoff", True),
        ("tinkofff", "tinkoff", False),
        ("tinkof", "tinkoff", False),
        ("tinkoff", "aaa", False),
    ]

    for word1, word2, expected in test_cases:
        assert is_anagram(word1, word2) == expected
