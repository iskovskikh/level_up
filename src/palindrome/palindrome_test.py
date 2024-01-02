from palindrome.palindrome import is_palindrome


def test_is_palindrome():
    test_cases = [
        ("tinkoff", False),
        ('abcba', True),
        ('abccba', True),
        ('aa', True),
        ('a', True),
        ('', True),

    ]

    for word, expected in test_cases:
        assert is_palindrome(word) == expected
