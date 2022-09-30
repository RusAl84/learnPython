def say_hello():
    print("Привет родной;)")


def say_hello(name="Василий", age=18):
    if age >= 18:
        print(f"Рад Вас приветствовать {name}")
    else:
        print(f"Привет {name}")


def say_bye():
    print("До свидания")


if __name__ == "__main__":
    say_hello(name="Алексей Михайлович", age=37)
    say_hello(name="Алиса", age=16)
