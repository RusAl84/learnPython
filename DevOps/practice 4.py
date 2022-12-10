import os
from datetime import datetime
import hashlib


def print_details(a):
    print(
        f"{a=}\ta.id: {id(a)}\ntype of a:{type(a)}\nis a an object:{isinstance(a, object)}\n"
    )

def fn2():
    pass


class A:
    name = "cls_name"
    __cls_private = "cls_private"
    _cls_protected = "cls_protected"

    def __init__(self, val):
        self.val = val
        self._protected = "protected"
        self.__private = "private"

    def print(self):
        print(
            f"{self.val=}, {self._protected=}, {self.__private=}, "
            f"{self.name=}, {self.__cls_private=}"
        )

class B(A):
    def __init__(self, val):
        super().__init__(val)
    def __str__(self):
        return f"< Class instance of B. {self.val=} >"
    def multiply(self, *args):
        if len(args)>0:
            res = self.val
            for arg in args:
                try:
                    print(f"Evaluating {res}*{arg} ...")
                    res *= arg
                except Exception as ex:
                    print(f"Something gone wrong at multipliing {res } and {arg}\n{str(ex)}")
            return res
        else:
            try:
                return self.val * self.val
            except ValueError as ex:
                print(f"Can't multiple {self.val} course it's {type(self.val)}")
                return None


if __name__ == "__main__":
    # Everything is an Object, one more time with feeling
    # print_details(a=1)
    # print_details(a="Hello world!")
    # print_details(a=datetime.now())
    # print_details(a=os.path.realpath("./"))
    # print_details(fn2)
    # a = A(4834)
    # a.print()
    # a=A(322)
    # b=A("sdsafafsa")
    # print_details(a)
    # a.print()
    # print_details(b)
    # b.print()
    # print("Lets try an instance of our class c= B(322)")
    # c=B(88889999) #Можно брейкпоинт тут поставить, чтобы закончить все ращговоры за инкапсуляцию. Т.е. если вы в лагере ее нет, вот пруф.
    # print_details(c)
    # print(c.multiply())
    # print(c.multiply(1,2,3))

    print("\nAnd another one: d = B(3)")
    d=B(3)
    print(d.multiply(91))
    print(d.multiply("Privet, KAK DILA? "))
    print(d.multiply("Privet,", "KAK DILA? "))
