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
        if len(args) > 0:
            res = self.val
            for arg in args:
                try:
                    print(f"Evaluating {res}*{arg} ...")
                    res *= arg
                except Exception as ex:
                    print(
                        f"Something gone wrong at multipliing {res } and {arg}\n{str(ex)}"
                    )
            return res
        else:
            try:
                return self.val * self.val
            except ValueError as ex:
                print(f"Can't multiple {self.val} course it's {type(self.val)}")
                return None


###########################################Class methods################################################################
class MethodDifference:
    class_attr = "Only class methods can change me."

    @staticmethod
    def print_static():
        print("static")

    @classmethod
    def print_cls(cls):
        print(f"class_method for {cls.__name__}")

    @classmethod
    def change_attr(cls, new_val):
        cls.class_attr = new_val
        print(f"Changed! {cls.class_attr=}")

    def __init__(self, val):
        self.val = val

    def print_offset(self, offset=10):
        print(self.val + offset)

    def __str__(self):
        return f"{self.__class__.__name__}:val={self.val}"


class VanillaPyUser:
    def __init__(self, name, password):
        self.__name = name
        self.password_hash = None
        self.password = password

    @staticmethod
    def make_hash(data: str) -> str:
        """method that emulates hashing. IRL u need real hasher(seed, val2hash)"""
        hashStr = hashlib.md5(data.encode()).hexdigest()
        print(f"Hash is {hashStr}")
        return hashStr

    @property
    def name(self):
        """name is read-only"""
        return self.__name

    @property
    def password(self):
        raise AttributeError("Password is write-only")

    @password.setter
    def password(self, plaintext):
        self.password_hash = VanillaPyUser.make_hash(plaintext)


##################################################Class#Inheritance#####################################################
class Ancestor:
    pass


class FirstGen(Ancestor):
    pass


class AnotherFirstGen:
    pass


class Child(FirstGen, AnotherFirstGen):
    pass


##################################################Class#IRL#############################################################
class Alive:
    def die(self):
        print(f"{self} says 'Im dead!'")

    def fly(self):
        print(f"{self} says 'Lets try flying. It's safe and fun'")
        self.die()


class Duck(Alive):
    def answer(self):
        print(f"{self} says 'Quack!'")

    def fly(self):
        print(f"{self} says 'Easy! I`m flying'")


class Developer(Alive):
    def develop(self):
        print(f"{self} says 'WIP. Reading Manual!'")

    def die(self):
        print(f"{self} says: `X.X & v prodakshen. Oops...`")

    def answer(self):
        print(f"{self} says 'Not now i`m busy, reading manual!'")


# class DuckDeveloper(Developer, Duck):
class DuckDeveloper(Duck, Developer):
    pass


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

    # print("\nAnd another one: d = B(3)")
    # d = B(3)
    # print(d.multiply(91))
    # print(d.multiply("Privet, KAK DILA? "))
    # print(d.multiply("Privet,", "KAK DILA? "))

    # Not all Methods are the same
    # print(f"No instance yet. But i can call static and class methods:")
    # MethodDifference.print_cls()
    # MethodDifference.print_static()
    # md_inst = MethodDifference(3)
    # print(md_inst)
    # md_inst.print_offset()
    # md_inst.print_offset(10)

    # Getters setters in vanilla python style
    # usr1 = VanillaPyUser("user1", "funnypass")
    # print(usr1.name)
    # try:
    #     print(usr1.password)
    # except AttributeError as ex:
    #     print(str(ex))
    # usr1.password = "LessFunnyPass"

    # Inheritance101: MRO and bases
    # print(FirstGen.__bases__)
    # print(FirstGen.mro())
    # print(Child.__bases__)
    # print(Child.mro())
    # print(2+2)
    # MRO and Ducks in oneshot. Need to change DuckDeveloper definiton...
    ducky = Duck()
    ducky_dev = DuckDeveloper()
    dev = Developer()

    ducky.answer()
    ducky.die()
    dev.answer()
    dev.die()
    ducky_dev.answer()
    ducky_dev.die()
    print(DuckDeveloper.mro())
    # Идем в объявление DuckDeveloper. Меняем порядок. Наша утка-разраб становится сначала (более) деволер, чем утка.
    # class DuckDeveloper(Duck, Developer): --> class DuckDeveloper(Developer, Duck):
