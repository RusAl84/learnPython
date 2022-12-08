import datetime
import random

"""
Datatype examples;
Working with strings without control flow;
"""


def syntax_example():
    a = 10
    b = 5
    if a > b:
        print("A больше B")
        print(a - b)
    else:
        print("B больше или равно A")
        print(b - a)
    print("Конец")


def open_file(filename="./f1.txt"):
    print("Чтение файла", filename)
    with open(filename, "rt", encoding="utf-8") as f:
        return f.read()


def comments_exmaple():
    # Очень важный комментарий
    a = 10
    b = 5  # Очень нужный комментарий
    """
    Очень важный
    и длинный комментарий
    """
    a = 10
    b = 5
    # Строки и регэкспы с эсплайн также используют тройные кавычки.
    s = """I'm a string with weird formating, "and no need to escape tickles" 'neither dobule nor single'"""
    print(s)
    s1 = "I " "help" " hedgehog"
    print(s1)


def dir_help_example():
    s1 = "hello"
    int1 = 123
    print(f"dir от str:\n{dir(s1)}")
    input("Awaiting input...")
    print(f"help от str:\n{help(str)}")


def vars_example():
    a = 3
    b = "Hello"
    c, d = 9, "Hedgehog"
    print(a, b, c, d)
    # 3 Hello 9 Test


def links_to_same_primiteve(equals_to=None):
    if equals_to is None:
        a = b = c = 33478563487543904374508347
        equals_to = 33478563487543904374508347
    else:
        a = b = c = equals_to
    print(f"a=b=c={equals_to}\na:{a}\tb:{b}\tc:{c}")
    print(f"a: {id(a)}\nb: {id(b)}\nc: {id(c)}")


def links_to_dif_primiteve():
    a = "собака"
    b = "собака"
    c = "собака"
    b = "hadgehog"
    print(f"a=b=c=собака\na:{a}\tb:{b}\tc:{c}")
    print(f"a: {id(a)}\nb: {id(b)}\nc: {id(c)}")


def int_function():
    a = int(322)
    b = int(1024 - a)
    c = int(b / a)
    print(f"\na:{a}\tb:{b}\tc:{c}")
    print(f"a: {id(a)}\nb: {id(b)}\nc: {id(c)}")


def simple_math():
    print("Арифметика")
    print(f"1 + 2 = {1 + 2}")
    print(f"1 + 3.0 = {1 + 3.0}")
    print(f"2^3 = {2 ** 3}")
    print("\nПреведение типов, округления")
    print(f"10/3 = {10 / 3}")
    print(f"10/2.5 = {10 / 2.5}")
    print(f"10/3 = {round(10 / 3, 2)}")
    print(f"10 остаток от деления на 3 = {10 % 3}")


def comparesments():
    print(f"Равенство 10 == 10\t{10 == 10}")
    print(f"Меньше равно 10 <= 10\t{10 <= 10}")
    print(f"Больше 10 > 10\t{10 > 10}")
    print(f"Больше  или равно 10 >= 12\t{10 >= 12}")
    print(
        f"Особое знанчение inf 99999999999 >= float('inf')\t{999999999999 >= float('inf')}"
    )
    try:
        print(
            f"Особое знанение None не стоит с ним сравнивать\n\t 999 == None\t{999 == None}"
        )
        print(f"\n\t{999 > None}")
    except TypeError as exc:
        print(f"Питон падал с ошибкой {exc}\n При попытке вывести:\n 999 > None")
    a = 32
    print(f"Сравнивать лучше так a is None\t{ a is None }")


def switch_base():
    print(f"Двоичное представление bin(8):\t {bin(8)}")
    print(f"Двоичное представление bin(255):\t {bin(255)}")
    print(f"По основанию 16 hex(255):\t {hex(255)}")
    print(f"По основанию 16 hex(8):\t {hex(8)}")
    print(f"Цепочки преобразований, возможны")
    print(f"int('ff', 16) {int('ff', 16)}")
    print(f"bin(int('ff', 16)) {bin(int('ff', 16))}")


def math_exists():
    import math
    print(f"Квадратный корень из 9 {math.sqrt(9)}")
    print(f"Квадратный корень из 10 {math.sqrt(10)}")
    print(f"Факториал 4 {math.factorial(4)}")
    print(f"Константы {math.pi}")
    print("Не забываем про dir и ctrl+space...")
    l = dir(math)
    for idx in range(len(l)):
        if (idx % 7 == 0):
            print(l[idx-7:idx])

#############################################STRINGS###################################################################

def define_strs():
    s = "Hello"
    s = 'Hello'

    tunnel = """
    interface Tunnel0
    ip address 10.10.10.1 255.255.255.0
    ip mtu 1416
    ip ospf hello-interval 5
    tunnel source FastEthernet1/0
    tunnel protection ipsec profile DMVPN
    """
    iface = "interface"
    tun = "Tunnel0"
    tun_str = iface + ' ' + tun
    print(tunnel)
    print(tun_str)
    print(tun * 5)
    print("#" * 80)


if __name__ == "__main__":
    # не правильный комментарий (incorrect comment)
    # syntax_example() # correct comment
    # print(open_file())
    # comments_exmaple()
    # dir_help_example()
    # vars_example()
    """Все учебники по питону, утверждают, что при достаточно больших примитивах ссылки будут разные.
    У меня ссылки одинаковые, хотя объекты не зависимые. Так что не знаю, стоит ли это вообще показывать."""
    # links_to_same_primiteve(43534323423342)
    # links_to_dif_primiteve()
    # int_function()
    # simple_math()
    # comparesments()
    # switch_base()
    # math_exists()
    define_strs()