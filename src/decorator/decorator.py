import functools
import time
from typing import Generic, Callable, ParamSpec, TypeVar

P = ParamSpec('P')
T = TypeVar('T')


def time_it(func: Callable[P, T]) -> Callable[P, T]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__} took {end - start} seconds')
        return result

    return wrapper

class MyClassDecorator(Generic[P, T]):
    wrapped_call: Callable[P, T]

    def __init__(self, call: Callable[P, T]):
        if not isinstance(call, MyClassDecorator):
            self.wrapped_call = call
        else:
            ...

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
        return self.wrapped_call(*args, **kwargs)


def my_func_decorator(
        func: Callable[P, T]
) -> Callable[P, T]:
    @functools.wraps(func)
    def wrapper(
            *args: P.args,
            **kwargs: P.kwargs
    ) -> T:
        # Do something before calling the function
        result = func(*args, **kwargs)
        # Do something after calling the function
        return result

    return wrapper


@my_func_decorator
def greet(username: str):
    return f'greetings {username}!'
