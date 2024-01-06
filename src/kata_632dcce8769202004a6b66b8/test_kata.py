from kata_58905bfa1decb981da00009e.kata import Dinglemouse
from kata_632dcce8769202004a6b66b8.kata import calculate


def test_kata():
    test_cases = [
        (['0000', '0000'], 2, 0),
        (['z0z0', 'zzzz'], 2, 70),
        (['00', 'zz'], 3, 0),
        (['00', '11'], 2, 2),
        (['000', 'zzz'], 2, 210),
        (['zz00', '00zz'], 2, 140),
        (['0000', 'zzzz'], 2, 420),
        (['00000', 'zzzzz'], 2, 700),
        (['000000', 'zzzzzz'], 2, 1050),
        (['0000000', 'zzzzzzz'], 2, 1470),
        (['0000000', 'zzzzzzz'], 3, 3675),
        (['0000000', 'zzzzzzz'], 4, 4900),
        (['00aa', 'ggzz'], 2, 82),
        (['3i3i', '9f9f'], 2, 18),
        (['00112222', 'xxii0000'], 2, 124),
        (['00', 'zz',], 2, 70),
        (['00', 'zz', '00'], 2, 140),
        (['00', 'zz', '00', 'zz'], 2, 210),
        (['pqpq', 'dbdb', 'pqpq', 'dbdb'], 2, 162),
        (['pqpqooii', 'dbdbxxgg', 'pqpqhnhm', 'dbdbwwuu'], 2, 184),
        (['x9f81mjll', 'vujd8vqh1', '6e3u9dw7a',
          '333333333', '7bbjxh9ed', 'lllllllll',
          'ooooooooo', '111111111', 'fffffffff',
          'ttttttttt', 'ttttttttt', 'p6dzi6mrj',
          'nnnnnnnnn', 'lllllllll', '777777777',
          'sssssssss', 'qqqqqqqqq', '555555555',
          '8we6trpvj', 'eeeeeeeee', '222222222',
          'f54xqfykj', 'sssssssss', '999999999',
          'ddddddddd', 'sssssssss'], 4, 82656),
        ([
             'hraee7jbnhfqb1c7v5nu2wr',
             'na1fwft37ms41odfgje3l8r',
             'wwxbjbcebbno17uub738ld3',
             'sdctngiv1ra6aaa5eil9118',
             'el7ltogqui7a3fdc9jokpyx',
             'rcioo3xg0w16kd4hjxhkg24',
             'qdpo5fzvugps975tl1dnzxw',
             '15jqh3rewu8r4g7i6li4c8f',
             'kxicmfi66to86nlc8cctd3j',
             'xhu8wviskrijf5z7o8svoob',
             'j9h6h9767xbwr2dltmuerne',
             '3h4bynunxx8bfkpvki6sx9j',
             'qk3gh91fbjba4l2ghayhfgx',
             'w3612e3gr8j4hbv4allg1h8',
             '13s5rrwj9gvl7sk7yq6vq14',
             '0wd5ofggb75aeh7g1oaswmz',
             'j1utx8i4ahcpssekzcbiehk',
             'whvh1u52lexzw37zs7sx61r',
             'o1elyih59nhpbpkojk72sc6',
             'k4wb4v3fe9tr7lp5w6bqhoo',
             'n7btgthdj45bbq07f8l9u2o',
             'vknnrbu1pe1ev4uvy4c4acb',
             'oz3oiuljho6nhjstdq7jxpe',
             'bwk1sovf75287hh0reskd47',
             'vzw3phi5ow2hb728zo4q4ge',
             'jydegf2txrkgxbuqr34l8yi',
             'qpa8kmn8w4ewyjerx32osuk',
             'mejvefhlm5ign945osle58n'
         ], 2, 120),
    ]

    for data, n, expected in test_cases:
        result = calculate(data, n)
        assert result == expected