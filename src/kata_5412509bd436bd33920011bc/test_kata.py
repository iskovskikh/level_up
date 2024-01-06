
from kata_5412509bd436bd33920011bc.kata import maskify


def test_kata():
    test_cases = [
        ('', ''),
        ('123', '123'),
        ('SF$SDfgsd2eA', '########d2eA')
    ]

    for seconds, expected in test_cases:
        assert maskify(seconds) == expected
