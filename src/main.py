#!/usr/bin/env python3
import functools
from typing import ParamSpec, TypeVar, Callable, Any

P = ParamSpec('P')
T = TypeVar('T', bound=Callable[..., Any])


def uppercase(func: Callable[P, T]) -> Callable[P, T]:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


@uppercase
def greet(username: str):
    return f'greetings {username}!'


def main():
    print(greet('alex'))


if __name__ == "__main__":
    main()
