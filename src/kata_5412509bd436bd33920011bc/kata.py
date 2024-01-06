# return masked string
import string


def maskify(cc):
    a = string.digits
    if len(cc) <= 4:
        return cc
    else:
        return '#' * (len(cc) - 4) + cc[-4:]

    return []