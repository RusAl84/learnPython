# print(*range(9))
# print(*range(1, 5))
# print(*range(1, 6, 2))
# for i in range(5):
#     print(i)
# list1 = ["воды", "кирпич", "песок"]
# for item in list1:
#     print(f"Юра принес {item}")

list1 = ["воды","end", "кирпич", "песок", "пиво", "чипсы", "воблу", "end"]
for item in list1:
    if item == "пиво":
        continue
    if item == "end":
        break
    print(f"Юра принес {item}")
