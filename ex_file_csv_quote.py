import csv


def quote_generator(str1="Артём привет! Ты уже едешь ко мне на дачу?"):
    quote = ""
    for word in str1.split():
        with open("data_quote.csv", "r", newline="", encoding="UTF8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == word or row[1] == word or row[2] == word:
                    quote = row[3]
    return quote


if __name__ == "__main__":
    str1 = "Артём привет! Ты уже едешь ко мне на дачу?"
    quote = quote_generator()
    print(f"Текст сообщения: {str1}")
    print(f"Пословица к сообщению: \"{quote}\"")
    str1 = "Мама я поеду завтра вместо школы в лес"
    quote = quote_generator(str1)
    print(f"Текст сообщения: {str1}")
    print(f"Пословица к сообщению: \"{quote}\"")
