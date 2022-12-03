# •	для файла передачи данных в систему интеллектуального анализа данных
# (текстовые данные) в виде массива данных с датой отправки данных,
# id кем отправленные, приоритет обработки данных —
# список из 3х элементов
data = []
record = {}
record["send_date"] = "19:30 07.10.2022"
record["sender_id"] = 437
record["data"] = "Мама мыла раму, и потом наступил новый год"
record["priority"] = "low"
data.append(record)
record = {}
record["send_date"] = "19:33 07.10.2022"
record["sender_id"] = 467
record["data"] = "Даша дай пожалуйста списать контрольную работу, очень прошу"
record["priority"] = "higth"
data.append(record)
record = {}
record["send_date"] = "19:35 07.10.2022"
record["sender_id"] = 884
record["data"] = "Мама я не хочу больше учить питон, мне надоело. Мама я хочу в Сирию"
record["priority"] = "low"
data.append(record)
print(data)
import json

json_string = json.dumps(data)
print(json_string)
with open("data3.json", 'w') as file1:
    file1.write(json_string)

with open("data3.json", 'r') as file2:
    content = file2.read()
import json
object = json.loads(content)

for item in object:
    print(f"{item['send_date']} <{item['sender_id']}>: {item['data']} ({item['priority']})")