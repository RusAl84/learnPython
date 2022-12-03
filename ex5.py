def func1(name, value, drink):
    return (f"{name} выпил {value} мл. {drink} ", value*10)

if __name__=="__main__":
    (param1, param2) = func1("Русаков", 50, "HENESSY",)
    print(param1)
    print(param2)