import time
from config import Config
from typing import Callable
from functools import wraps


def square(x):
    return (x, x**2)


def sum_of_3(a, b, c=0):
    print(f"{a=}, {b=}, {c=}")
    print(f"Returning {a + b + c}")
    return a + b + c


def sum_of_any(a, b, *args):
    print(f"{a=}, {b=}, {args=}")
    res = a + b
    for i in args:
        res += i
    print(f"Returning {res}")
    return res


def sum_of_args(*args):
    if len(args) == 0:
        return None
    res = args[0]
    # for idx in range(1, len(args)):
    #     res += args[idx]
    for i in args:
        res += i
    return res


def kwargs101(**kwargs):
    print(kwargs, type(kwargs))


def print_args(*args, **kwargs):
    arg_str = ", ".join([str(i) for i in args])

    d2l = [f"{k}:{v}" for k, v in kwargs.items()]
    kwarg_str = ", ".join(d2l)

    print(f"{args=},{kwargs=}")
    print(f"upacked args: {arg_str}.\t unpacked kwargs: {kwarg_str}")


globVar = "Global var"


def scopes_outer1():
    p1 = 1
    lst = []

    def scopes_inner2():
        p2 = 2
        nonlocal p1
        p1 = 10
        lst.append(10)
        global globVar
        globVar = "f2 global var"
        print(f"{p2=}, {p1=}, {globVar=}", locals())

    scopes_inner2()
    print(f"{p1=}, {lst=}, {globVar=}", locals())


def divi(a, b):
    return a / b


def mult(a, b):
    return a * b


def plus(a, b):
    return a + b


def power(a, b):
    return a**b


def minus(a, b):
    return a - b


def fn_as_1st_cl_member(a: int, b: int, operation: Callable) -> int:
    return operation(a, b)


def sumator_closure():
    state_storage = []

    def sum_with_state(val: int) -> int:
        print(f"Adding {val} to storage")
        state_storage.append(val)
        res = sum(state_storage)
        print(f"Returning {res} as sum of {state_storage}")
        return res

    return sum_with_state


##################Decorator########################
#  определение функции декоратора
def select(input_func):
    def output_func():  # определяем функцию, которая будет выполняться вместо оригинальной
        starString = "*" * 120
        print(starString)  # перед выводом оригинальной функции выводим всякую звездочки
        input_func()  # вызов оригинальной функции
        print(starString)  # после вывода оригинальной функции выводим всякую звездочки

    return output_func  # возвращаем новую функцию


# определение оригинальной функции
@select  # применение декоратора select
def hello():
    print("Hello DevOps")


def timer(func):
    # print("timer")
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_ts = time.time()
        res = func(*args, **kwargs)
        end_ts = time.time()
        print(f"Time of {func.__name__} is {end_ts - start_ts} seconds")
        return res
    return wrapper


def sleeper(delay_sec=0.5, fake=True):
    def _sleeper(func):
        # print("sleeper")
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            print(f"sleeper make us sleep {delay_sec}")
            time.sleep(delay_sec)
            return res
        return wrapper
    return _sleeper


@timer
@sleeper()
def get_default_content(url):
    return url


@sleeper(0.1, False)
def get_delayed_content(url):
    return url


@timer
def get_docs_from_http(urls, https=True):
    """urls -> list of universal resource locators  [ссылки]"""
    res = []
    for url in urls:

        if url.endswith("vk.com"):
            content = get_delayed_content(url)
        else:
            content = get_default_content(url)
        res.append(content)
    return res


def parse_vals(command):
    eq_idx = command.find("=")
    next_space_idx = command.find(" ", eq_idx)
    a = int(command[eq_idx + 1 : next_space_idx])
    eq_idx = command.find("=", next_space_idx)
    next_space_idx = command.find(" ", eq_idx)
    if next_space_idx == -1:
        b = int(command[eq_idx + 1 :])
    else:
        b = int(command[eq_idx + 1 : next_space_idx])
    return a, b


def do_what_i_say(command: str) -> int:
    fn_map = {
        "сложи": plus,
        "плюс": plus,
        "вычти": minus,
        "минус": minus,
        "множ": mult,  # йета корень ни фсе праграммисты ни умеют вруский
        "раз": mult,
        "дели": divi,  # корень
    }
    oper = None

    for k, v in fn_map.items():
        if k in command.lower():
            oper = v
            break
    if not oper:
        print("Не удалось распознать команду")
        return None
    try:
        a, b = parse_vals(command)
    except ValueError as er:
        print("Не удалось распознать аргументы")
        return None
    print(f"passing {a}, {b}, {k}  to fn_as_1st_cl_member")
    res = fn_as_1st_cl_member(a, b, oper)
    return res


def make_function(name, *args, kw=42, **kwargs):
    """makes inner function"""

    def inner(sadness=999):
        print(f"{name=}, {sadness=}, {kw=}, {args=}, {kwargs=}")

    return inner


if __name__ == "__main__":
    # cfg = Config("00:00")
    # cfg.print_status_time()
    # print(square(12))
    # print(sum_of_3(2,2))
    # print(sum_of_3(2, 2, 77))
    # sum_of_any(1,2,3,4,5,6,7,8,9)
    # print(sum_of_args(1))
    # print(sum_of_args(1, 2))
    # print(sum_of_args(1, 2, 3))
    # print(sum_of_args(1, 2, 3, 4))
    # print(sum_of_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 470))
    # kwargs101(m=3, n=4, arg1='somestr',long_arg='asmoranomardicadaistinaculdacar')
    # print_args(1,2,3,4,key='val', num=3)
    # scopes_outer1()

    # Closure example
    # sum_c = sumator_closure()
    # s = sum_c(1)
    # s = sum_c(1)
    # s = sum_c(23333)

    # Functions as first class members
    # print(f"passing 2, 3, plus to fn_as_1st_cl_member: {fn_as_1st_cl_member(2,3,plus)}")
    # print(
    #     f"passing 2, 3, mult to fn_as_1st_cl_member: {fn_as_1st_cl_member(2, 3, mult)}"
    # )
    # print(
    #     f"passing 2, 3, power to fn_as_1st_cl_member: {fn_as_1st_cl_member(2, 3, power)}"
    # )

    ##################Decorator########################
    # hello()

    # start_ts = time.time()
    # urls = ["https://google.com", "http://ya.ru", "https://rkn.gov.ru/"]
    # print(get_docs_from_http(urls))
    # end_ts = time.time()
    # print(f"Total: {end_ts - start_ts} seconds")

    # Fn mapping if time allows
    print(do_what_i_say("Умножь a=20 на b=5"))
    print(do_what_i_say("Дели a=7 на b=2"))
    print(do_what_i_say("Порядок a=2 b=10 не имеет значения плюс"))    
    print(do_what_i_say("Порядок a=2 b=10 с=598 не имеет значения плюс1"))

    # How this magic works
    fn = make_function("", 54, aim="term")
    # fn()
    # fn()
    print(f"Name: {fn.__name__}\nDocstring: {fn.__doc__}\nDefaults:{fn.__defaults__}")
    print(f"Closure: {fn.__closure__}")
    print(f"Lets peek inside of this links: {fn.__closure__[0].cell_contents}")
    print(f"Lets peek inside of this links: {fn.__closure__[1].cell_contents}")
