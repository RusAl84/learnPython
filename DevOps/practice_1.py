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


def open_file(filename="D:/sources/learnPython1/learnPython/DevOps/f1.txt"):
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
    s1 = "I""m"
    s = """I'm a string with weird formating, "and no need to escape tickles" 'neither dobule nor single'"""
    print(s1)
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
        print(
            f"Питон падал с ошибкой {exc}\n При попытке вывести:\n 999 > None")
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
        if idx % 7 == 0:
            print(l[idx - 7: idx])


############################################# STRINGS###################################################################


def define_strs():
    s = "Hello"
    s = "Hello"

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
    tun_str = iface + " " + tun
    print(tunnel)
    print(tun_str)
    print(tun * 5)
    print("#" * 80)


def strings_as_l_of_chars():
    str1 = "abcdfeghij"
    str2 = "0123456789"
    print(f"{str1}\n{str2}")
    print(f"Третий символ строк: {str1[2]}, {str2[2]}")
    print(f"Предпоследний символ строк: {str1[-2]}, {str2[-2]}")
    print(
        f"Символы с [4 по 5) начала включаем, конец нет : {str1[3:5]}, {str2[3:5]}")
    print(f"Символы с [3:] {str1[3:]}, {str2[3:]} ")
    print(f"Символы до [3:] {str1[:3]}, {str2[:3]} ")
    print("Можно вычислять в процессе...")
    print(f"Начиная с первого встреченного e: {str1[str1.find('e'):]}")
    print(f"До первой встреченной 5: {str2[:str2.find('5')]}")

    print("\nУгар и содомия. Можно указвать шаг. Но лучше писать ф-ии...")
    print(f"Го нечетные {str2[1::2]}, го кратные 3 {str2[0::3]}")
    print(f"Можно инветрнуть строки срезами [::-1] {str1[::-1]}, {str2[::-1]}")


def join_example():
    vlans = ["100", "168", "255", "196"]
    print(",".join(vlans))
    s = " ".join(dir(str))
    print(s[s.find("join"):])
    l = [str(i) for i in range(11)]
    s1 = " ".join(l)
    l2 = s1.split()
    print(
        f"\nИзначальный лист: {l}\nСклееная строка: {s1}\nВостановлено из строки: {l2}"
    )


def weird_str_methods():
    str1 = "SomethingInCamelCase"
    print(
        f"upper: {str1.upper()},\tlower: {str1.lower()},\t\nswapcase:{str1.swapcase()}, \t capitalize:{str1.capitalize()}"
    )


def find_like_str_methods():
    str1 = """
    Python является мультипарадигмальным языком программирования, поддерживающим императивное,
    процедурное, структурное, объектно-ориентированное программирование, метапрограммирование и функциональное
    программирование.
    Задачи обобщённого программирования решаются за счёт динамической типизации.
    Аспектно-ориентированное программирование частично поддерживается через декораторы,
    более полноценная поддержка обеспечивается дополнительными фреймворками.
    Такие методики как контрактное и логическое программирование можно реализовать с помощью библиотек
    или расширений."""
    print(str1)
    print(
        f'\nСколько раз корень програм есть в тексте выше:\t{str1.lower().count("програм")}'
    )
    idx = str1.lower().find("програм")
    print(f'Индекс первого упоминания "програм":\t{idx}')
    print(f'Контекст первого упоминания "програм":\t{str1[idx:idx+30]}...')
    print(f"То же но с конца...")
    idx = str1.lower().rfind("програм")
    print(f'Индекс первого упоминания "програм":\t{idx}')
    print(f'Контекст первого упоминания "програм":\t{str1[idx:idx + 30]}...')
    # никогда не делайте так IRL - улетите за границы


def methods_for_ppl_who_cant_import_re():
    str1 = "Intel(R) 82579LM Gigabit Network Connection"
    print(f'Начинается с Intel? {str1.startswith("Intel")}')
    print(f'Кончается на Intel? {str1.endswith("Intel")}')
    str1.endswith("Connection")
    str1.endswith("Network")
    print(f'Можно tuple как аргумент: {"test".startswith(("a", "b", "c"))}')
    print(f'Можно tuple как аргумент: {"test".endswith(("a", "t", "c"))}')

    str1 = "Intel(R) 82579LM Gigabit Network Connection"
    print(f"\n{str1} {id(str1)}")
    str2 = str1.replace("Gigabit", "Megabit")
    print(f"{str2} {id(str2)}")
    str3 = "[(  ( Im string from with some noise..  ])]"
    print(f"\nLets strip [ only {str3.strip('[')}")
    print(f"Lets strip '[]()' {str3.strip('[]() ')}")


def format_with_format(amount=10):
    vlan, mac, intf = ["100", "aabb.cc80.7000", "Gi0/1"]
    print("{:>15} {:>15} {:>15}".format(vlan, mac, intf))
    ip_tmpl = """
    IP address:
    {}"""
    print(ip_tmpl.format("196.168.100.234"))
    for i in range(amount):
        print(ip_tmpl.format(
            ".".join([str(random.randint(0, 255)) for x in range(4)])))


def more_format():
    import math
    print("To binary: {:b} {:b} {:b} {:b}".format(192, 100, 1, 1))
    print("С заданой точностью: {:.3f}".format(math.pi))
    print("Именовано ip/mask: {ip}/{mask}".format(mask=24, ip='10.0.0.1'))
    print(
        f"Формат строками {math.pi:.3f} Единственный минус в том что вы совмещаете логику и шаблон {2 + 3} это не очень ООПшно")


if __name__ == "__main__":
    # не правильный комментарий (incorrect comment)
    # syntax_example()  # correct comment
    # print(open_file())
    # comments_exmaple()
    #dir_help_example()
    #vars_example()
    """Все учебники по питону, утверждают, что при достаточно больших примитивах ссылки будут разные.
    У меня ссылки одинаковые, хотя объекты не зависимые. Так что не знаю, стоит ли это вообще показывать."""
    # links_to_same_primiteve(43534323423342)
    # links_to_dif_primiteve()
    # int_function()
    # simple_math()
    # comparesments()
    # switch_base()
    # math_exists()
    # define_strs()
    # strings_as_l_of_chars()
    # join_example()
    # weird_str_methods()
    # find_like_str_methods()
    # methods_for_ppl_who_cant_import_re()
    # format_with_format()
    # more_format()
