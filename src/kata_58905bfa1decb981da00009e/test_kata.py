from kata_58905bfa1decb981da00009e.kata import Dinglemouse


def test_kata():
    tests = [

        [
            (
                (4, 1, 4, 11, 3),
                (7, ),
                (4, ),
                (10, 10, 7),
                (1, ),
                (10, 2, 10),
                (1, 1, 11, 11, 1),
                (8, 11, 5),
                (3, 5),
                (1, 9, 0),
            ),
            [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 10, 9, 8, 7, 5, 1, 0, 1, 2, 3, 7, 8, 9, 10, 11, 10, 9, 8, 7, 5, 1, 0, 2, 3, 4, 8, 9, 11, 10, 9, 8, 7, 5, 0, 2, 3, 8, 9, 11, 10, 9, 8, 7, 5, 3, 0, 2, 3, 8, 9, 10, 9, 8, 7, 5, 1, 2, 3, 4, 8, 9, 11, 9, 8, 7, 5, 3, 9, 10, 8, 7, 1, 3, 7, 9, 11, 8, 7, 1, 7, 2, 0],
            1
        ],
        [((3,), (2,), (0,), (2,), (), (), (5,)), [0, 1, 2, 3, 6, 5, 3, 2, 0], 5],
        [(
            (),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
        ), [0, 6, 5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 3, 2, 1, 0, 1, 0], 5],
        [((), (), (4, 4, 4, 4), (), (2, 2, 2, 2), (), ()), [0, 2, 4, 2, 4, 2, 0], 2],
        [((), (), (5, 5, 5), (), (), (), ()), [0, 2, 5, 0], 5],
        [((), (), (1, 1), (), (), (), ()), [0, 2, 1, 0], 5],
        [((), (3,), (4,), (), (5,), (), ()), [0, 1, 2, 3, 4, 5, 0], 5],
        [((), (0,), (), (), (2,), (3,), ()), [0, 5, 4, 3, 2, 1, 0], 5]
    ]

    for queues, answer, capacity in tests:
        lift = Dinglemouse(queues, capacity)
        l = lift.theLift()
        print(l, answer)
        assert l == answer