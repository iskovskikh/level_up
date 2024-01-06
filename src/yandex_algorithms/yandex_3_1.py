# Дана последовательность положительных чисел длинной N и число X.
# Найти 2 различных числа A и B из последовательности,
# таких что A + B = X или вернуть пару 0, 0 если такой пары нет

def find_summ(n: list[int], x: int) -> tuple[int, int]:
    # решение за O(N^2):
    # for index, a in enumerate(n):
    #     for b in n[index+1:]:
    #         if a + b == x:
    #             return a, b
    # return 0, 0

    # решение за O(N)
    checked_set = set()
    for current in n:
        if x - current in checked_set:
            return x - current, current
        checked_set.add(current)
    return 0, 0
