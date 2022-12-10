import math
import os
import random
from datetime import datetime, timedelta
from time import sleep

from config import Config

"""
Control flow
Collections
"""


def simple_if(i=322):
    if i == 7:
        print(f"{i} равно 7")
    elif i < 7:
        print(f"{i} меньше 7")
    else:
        print(f"{i} больше 7")
    print(f"Есть хак с формат строками {i=}")


def casts_to_boolean():
    flag1 = 0
    flag2 = ""
    if flag1 or flag2:
        print("Never happens")
    else:
        print(f"{flag1} и '{flag2}' кастуется в False")
        print("None и пустой объект тоже")

    flag1 = 322
    flag2 = "ШБВВНХ"
    flag3 = datetime.now()
    if flag1 and flag2 and flag3:
        print(f"{flag1} и '{flag2}' и '{flag3}' кастуется в True")
        print(
            "Любые отличные от нуля числа и не пустые строки, и не пустые объекты тоже"
        )
    else:
        print("Never happens")

    print(
        """None or 0 or [] or {} or 0.0 or False
        or set() or () or "" or b"" or 322"""
    )
    print(None or 0 or [] or {} or 0.0 or False or set() or () or "" or b"" or 322)


def if_in_ex():
    route1 = {
        "IOS": "15.4",
        "IP": "10.255.0.1",
        "hostname": "london_r1",
        "location": "21 New Globe Walk",
        "model": "4451",
        "vendor": "Cisco",
    }
    print(f"{'IOS' in route1} IOS in route1")
    print(f"{'mAdell' in route1} IOS not in route1")

    l = [x for x in range(20)]
    print(l)
    print(f"{9 in l} 9 в диапазоне [0,19]")
    print(f"{20 in l} 20 в диапазоне [0,19]")
    print(f"{22 in l} 22 в диапазоне [0,19]")


def pseudo_pass_check(sitename="Denis.ru"):
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    if len(password) < 8:
        print("Пароль слишком короткий")
    elif (username in password) or (username in sitename):
        print("Пароль содержит имя пользователя")
    else:
        print("Пароль для пользователя {} установлен".format(username))


def for_examples():
    for i in range(100):
        print(f"{100-i} ### сидели на стене...")

    for fname in os.listdir():
        print(fname)


def for_layers():
    commands = [
        "switchport mode access",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
    ]
    fast_int = ["0/1", "0/3", "0/4", "0/7", "0/9", "0/10", "0/11"]
    for intf in fast_int:
        print(f"interface FastEthernet {intf}")
        for com in commands:
            print(f"\t{com}")


def while_example():
    l = [x for x in range(10)]
    while len(l) > 0:
        cur = l.pop()
        print(f"Выдернули {cur} осталось {l}")

    now = datetime.now()
    td = timedelta(seconds=5)
    stop = now + td
    while now < stop:
        now = datetime.now()
        secs_left = (stop - now).seconds
        print(f"Осталось {secs_left} секунд")
        sleep(0.5)


def another_pseudo_pass():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    pass_valid = False

    while not pass_valid:
        if len(password) < 8:
            print("Пароль слишком короткий\n")
        elif username in password:
            print("Пароль содержит имя пользователя\n")
        else:
            print(f"Пароль для пользователя {username} установлен")
            pass_valid = True
            continue
        password = input("Введите пароль еще раз: ")


def simple_try_except():
    try:
        a = input("Введите первое число: ")
        b = input("Введите второе число: ")
        print("Результат: ", int(a) / int(b))
    except ValueError:
        print("Пожалуйста, вводите только числа")
    except ZeroDivisionError:
        print("На ноль делить нельзя")


def trashy_try_except(i=None, range_start=0, range_end=9):
    print(i)
    try:
        i += 1
    except TypeError:
        i = range_start + 1
    print(i)


#####################################Collections#######################################


def list_plus_append():
    print(
        """
    tp1 = (1, 2, [3, 4])
    tp2 = (5, 6, [7, 8])
    
    tp = tp1 + tp2
    tp[2].append(99)
    """
    )
    tp1 = (1, 2, [3, 4])
    tp2 = (5, 6, [7, 8])

    tp = tp1 + tp2
    print(f"tp = {tp}")

    tp[2].append(99)
    print(f"tp = {tp}")
    print(f"tp1 = {tp1}")


def list_app_and_ext():
    tp2 = (5, 6, [7, 8])
    lst = []
    lst.append("99")
    print(lst)
    lst.extend(tp2)
    print(lst)
    lst.append(tp2)
    print(lst)
    myList = ["Lion", "Tiger", "Bear", "Cheetah", "Puma"]
    listToAdd = ["Leopard", "Lynx"]
    myList.extend(listToAdd)
    print(myList)


def list_pop_ins_del():
    lst = [1, 2, 3, 4, 5]
    print(lst)
    lst.insert(0, 0)
    lst.pop()
    print(lst)

    lst.pop(0)
    print(lst)

    lst.pop(0)
    print(lst)

    lst.pop(1)
    print(lst)

    lst.remove(2)
    print(lst)


def list_slices():
    lst = list(range(10))
    print(lst)

    print(lst[0 : len(lst) : 1])
    print(lst[:])

    print(lst[1:6:2])


def list_for_enumerate():
    lst = list(range(5))
    print(lst)
    for i, n in enumerate(lst, 10):
        print(i, n)


def dict_def():
    dct1 = {}
    dct2 = {1: 11, 2: 22}
    dct3 = dict(q=33, w=44)

    print(dct1, dct2, dct3)

    dct4 = {**dct1, **dct2, **dct3}
    print(dct4)

    dct4[42] = 4422
    print(dct4)
    print(dct4[42])

    print("pop", dct4.pop(42))
    print(dct4)

    print("pop", dct4.pop(42, "default"))
    print(dct4)

    print(42 in dct4, 1 in dct4)


def dict_traversal():
    dct = {1: 11, 2: 22, 0: 0}
    for i in dct:
        print(i)

    print("keys()")
    for i in dct.keys():
        print(i)

    print("values()")
    for i in dct.values():
        print(i)

    print("items()")
    for key, val in dct.items():
        print(key, val)

    print("\nenumerate()")
    for i, val in enumerate(dct.items()):
        print(i, val)

    print("\nenumerate()")
    for i, (key, val) in enumerate(dct.items()):
        print(i, key, val)

def list_sorted():
    lst = [4, 7, 23, 45, 7, 8, 6, 3, 1, 4, 6]
    print(lst)
    print(sorted(lst))
    print(sorted(lst, reverse=True))
    print(sorted(lst, key=str))


def list_compreh():
    lst = [n ** 2 for n in range(10)]
    print(f"lst = [n ** 2 for n in range(10)] \n{lst}")
    lst = [n ** 2 for n in range(10) if n % 2]
    print(f"lst = [n ** 2 for n in range(10) if n % 2] \n{lst}")
    lst = [str(random.randint(0,255)) for _ in range(4)]
    print(f"[random.random_int(0,255) for _ in range(4)] \n{lst} \n ipv4 {'.'.join(lst)}")
    lst = [round(math.sqrt(i),2) for i in range(64) if i % 2 == 0 ]
    print(f"[round(math.sqrt(i),2) for i in range(64) if i % 2 == 0 ]\n {lst}")
    #TODO Пример явного злоуботребления?

def dict_fetch():
    dct = {1: 11, 2: 22, 0: 0}

    print(dct[1])
    print(dct.get(2))
    print(99 in dct and dct[99])
    print(dct.get(99))
    print(dct.get(99, -1))


if __name__ == "__main__":
    # cfg = Config("10:43")
    # cfg.print_status_time()
    # simple_if(9)
    # casts_to_boolean()
    # if_in_ex()
    # pseudo_pass_check()
    # for_examples()
    # for_layers()
    # while_example()
    # another_pseudo_pass()
    # simple_try_except()
    # trashy_try_except()
    # list_plus_append()
    # list_app_and_ext()
    # list_pop_ins_del()
    # list_slices()
    # list_for_enumerate()
    # dict_def()
    # dict_traversal()
    # list_sorted()
    # list_compreh()
    dict_fetch()
    
