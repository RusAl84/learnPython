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
    with open(filename, 'rt', encoding='utf-8') as f:
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
    s1 = "I ""help"" hedgehog"
    print(s1)
    
def dir_help_example():
    s1='hello'
    int1=123
    print(f'dir от str:\n{dir(s1)}')
    input("Awaiting input...")
    print(f'help от str:\n{help(str)}')

def vars_example():
    a = 3
    b = 'Hello'
    c, d = 9, 'Hedgehog'
    print(a, b, c, d)
    # 3 Hello 9 Test

def links_to_same_primiteve(equals_to=None):
    if equals_to is None:
        a=b=c=33478563487543904374508347
        equals_to=33478563487543904374508347
    else:
        a=b=c=equals_to
    print(f"a=b=c={equals_to}\na:{a}\tb:{b}\tc:{c}")
    print(f"a: {id(a)}\nb: {id(b)}\nc: {id(c)}")


if __name__ == "__main__":
    # не правильный комментарий (incorrect comment)
    # syntax_example() # correct comment
    # print(open_file())
    # comments_exmaple()
    # dir_help_example()
    # vars_example()
    """ Все учебники по питону, утверждаюь что при достаточно больших примитивах ссылки будут разные.
    У меня ссылки одинаковые, хотя объекты не зависимые. Так что хз, стоит ли это вообще показывать."""
    #links_to_same_primiteve(43534323423342)
    #links_to_dif_primiteve()

