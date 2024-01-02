#!/usr/bin/env python3

from anagram.anagram import is_anagram
from decorator.decorator import greet


def main():
    print(greet('alex'))

    # assert is_anagram('tinkofff', 'tinkoff')


if __name__ == "__main__":
    main()
