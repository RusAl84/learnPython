# print(2 + 5)
# print("Вася и", "Вера ", "купили виллу на Азове")
# age = 18
# if age >= 18:  # проверка совершеннолетия
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ на сайт запрещен")
# print("Программа окончила работу")

name = "Антон"
capacity = 0.5
drink = "Балтика 0"
print(name + str(capacity) + drink)
str1 = f"Наш дорогой(ая) {name} любит пить {drink} в объеме {capacity} литра"
print(str1)
str1 = "{0} выпил {1} {2}".format(name, capacity, drink)
print(str1)
str1 = name + " выпил " + str(capacity) + " " + drink
print(str1)
