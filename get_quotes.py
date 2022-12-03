import pymorphy2
import json


def get_quotes():
    # https://1gai.ru/publ/525009-116-vdohnovljajuschih-citat-samyh-izvestnyh-ljudej-mira.html
    quotes = []
    quotes.append(
        "«Если человека всё устраивает, то он полный идиот. Здорового человека, в нормальной памяти не может всегда и всё устраивать». — Владимир Путин (О своем отношении к правительству в интервью 24 декабря 2000 г.)")
    quotes.append(
        "«Два самых важных дня в твоей жизни: день, когда ты появился на свет, и день, когда ты понял зачем!». — Марк Твен")
    quotes.append("«В трех словах я могу изложить все то, что узнал о жизни. То, что она продолжается». — Роберт Фрост")
    quotes.append(
        "«Я считаю, что у каждого человека есть ограниченное количество сердечных сокращений. Я не собираюсь тратить впустую мое». — Нил Армстронг")
    quotes.append("«Вы живете только один раз, но если вы все сделаете правильно, одного раза достаточно». — Мэй Уэст")
    quotes.append("«Ваше время ограничено, не тратьте его, живя другой жизнью». — Стив Джобс")
    return quotes


def get_normal_form(morph, word):
    p = morph.parse(word)[0]
    return p.normal_form


def getn_quotes_keywors():
    morph = pymorphy2.MorphAnalyzer()
    quotes = get_quotes()
    quotes_keywords = []
    for quote in quotes:
        line = {}
        line["quote"] = quote
        keywords = []
        for word in quote.split():
            keywords.append(get_normal_form(morph, word))
        line["keywords"] = keywords
        quotes_keywords.append(line)
    jsonstring = json.dumps(quotes_keywords)
    print(jsonstring)
    with open("quotes_keywords.json", "w", encoding="UTF8") as file:
        file.write(jsonstring)


if __name__ == "__main__":
    with open("quotes_keywords.json", "r", encoding="UTF8") as file:
        content = file.read()
    quotes_keywords = json.loads(content)
    str1 = "Мама я всё понял, я больше не буду учить питон. Буду тратить своё время на доту"
    quotes_keywords2 = []
    num = 0
    for quote in quotes_keywords:
        for word in str1.split():
            if word in quote["keywords"]:
                num += 1
            quote["num"] = num
        quotes_keywords2.append(quote)
    num = 0
    maxkw_quote = ""
    for quote in quotes_keywords2:
        if quote["num"] > num:
            num = quote["num"]
            maxkw_quote = quote["quote"]
    print(maxkw_quote)
    print(num)
