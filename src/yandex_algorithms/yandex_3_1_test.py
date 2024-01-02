from yandex_algorithms.yandex_3_1 import find_summ


def test_find_summ():
    test_cases = [
        ([1, 2, 3], 5, (2, 3)),
        ([1, 2, 3], 8, (0, 0)),
        ([1, 2, 6, 4, 3], 9, (6, 3)),
    ]

    for n, x, expected in test_cases:
        assert find_summ(n, x) == expected
