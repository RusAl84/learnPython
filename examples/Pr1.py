def task1write():
    # для сообщения мессенджера
    # (поля никнейм, id пользователя,
    # сообщение и время отсылки сообщения);
    messages = []
    message = {}
    message["nickname"] = "RusAl"
    message["id_user"] = 17
    message["text"] = "Привет"
    message["timeStamp"] = "19:32:16 06.10.2022"
    messages.append(message)
    message = {}
    message["nickname"] = "Sveta"
    message["id_user"] = 15
    message["text"] = "Привет!"
    message["timeStamp"] = "19:32:45 06.10.2022"
    messages.append(message)
    message = {}
    message["nickname"] = "RusAl"
    message["id_user"] = 17
    message["text"] = "Как дела?"
    message["timeStamp"] = "19:34:16 06.10.2022"
    messages.append(message)
    message = {}
    message["nickname"] = "Sveta"
    message["id_user"] = 15
    message["text"] = "Да вот препод душный попался и дал контрольную работу. Воще капец."
    message["timeStamp"] = "19:36:45 06.10.2022"
    messages.append(message)
    import json
    json_string = json.dumps(messages)
    print(json_string)
    with open("data1.json", 'w') as file1:
        file1.write(json_string)


def task1read():
    content = ""
    with open("data1.json", 'r') as file2:
        content = file2.read()
    import json
    object = json.loads(content)
    for item in object:
        # print(item)
        print(f"{item['nickname']} <{item['timeStamp']}> : {item['text']}")

if __name__ == "__main__":
    task1write()
    # task1read()
