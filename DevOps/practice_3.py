import time
from config import Config
from typing import Callable
from functools import wraps

def square(x):
    return x, x**2

def sum_of_3(a, b, c=0):
    print(f"{a=}, {b=}, {c=}")
    print(f"Returning {a + b + c}")
    return a + b + c


if __name__ == "__main__":
    cfg = Config("00:00")
    # print(square(10))
    # print(sum_of_3(2,2))
    print(sum_of_3(2,2))