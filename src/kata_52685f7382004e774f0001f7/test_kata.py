from kata_52685f7382004e774f0001f7.kata import make_readable


def test_kata():
    test_cases = [
        (0, "00:00:00"),
        (59, "00:00:59"),
        (60, "00:01:00"),
        (3599, "00:59:59"),
        (3600, "01:00:00"),
        (86399, "23:59:59"),
        (86400, "24:00:00"),
        (359999, "99:59:59"),
    ]

    for seconds, expected in test_cases:
        assert make_readable(seconds) == expected
