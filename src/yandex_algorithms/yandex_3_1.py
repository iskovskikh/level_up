# Дана последовательность положительных чисел длинной N и число X.
# Найти 2 различных числа A и B из последовательности,
# таких что A + B = X или вернуть пару 0, 0 если такой пары нет

def find_summ(n: list[int], x: int) -> tuple[int, int]:
    for index, a in enumerate(n):
        for b in n[index+1:]:
            print(a, b, "==", x)
            if a + b == x:
                return a, b

    return 0, 0
