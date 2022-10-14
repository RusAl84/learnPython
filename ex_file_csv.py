import csv
import random

users = []
for i in range(10):
    line = []
    line.append(f"Ёжик {i}")
    import random
    line.append(f"Возраст {random.randint(1, 5)}")
    users.append(line)

print(users)

with open("data.csv", "w", newline="", encoding="UTF8") as file:
    writer = csv.writer(file)
    writer.writerows(users)
