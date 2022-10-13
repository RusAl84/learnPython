
# with open("data.txt","w", encoding="UTF8") as file_with_numbers:
#     for num in range(1000):
#         file_with_numbers.write(f"ЁЖИК {num} \n")

content = ""
with open("data.txt","r", encoding="UTF8") as file_with_numbers:
    content = file_with_numbers.read()

print(content)