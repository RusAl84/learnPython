import csv

# with open("data.csv", "r", newline="", encoding="UTF8") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(f"{row[0]} {row[1]} {row[2]} - {row[3]}")

str1 = "Артём привет! Ты уже едешь ко мне на дачу?"
quote=""
for word in str1.split():
    with open("data_quote.csv", "r", newline="", encoding="UTF8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == word or row[1] == word or row[2] == word:
                quote = row[3]
print(quote)

