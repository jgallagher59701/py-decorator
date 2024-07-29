"""
Examples of function decorators in Python from
https://realpython.com/primer-on-python-decorators/

Original version

def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

A useful template

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
"""

import functools
import time


def do_twice(func):
    """Call the function twice; the function can take arguments
    This version returns the value of the second call to the function."""

    @functools.wraps(func)  # used so that the wrapped function retains its __name__ attribute
    def wrapper_do_twice(*args, **kwargs):  # support passing arguments to the wrapped function
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value

    return wrapper_timer


"""
@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([number**2 for number in range(10_000)])
"""


def debug(func):
    """Print the function signature and return value"""

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__}() returned {repr(value)}")
        return value

    return wrapper_debug


"""
@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you're growing up!"
"""