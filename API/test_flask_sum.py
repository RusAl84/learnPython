from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

ListOfMessages = []

@app.route('/')
def dafault_route():
    return f"Test message"

@app.route('/status')
def status():
    return {
        len(ListOfMessages)
    }

# отправка сообщений
@app.route("/send", methods=['POST'])
def send():
    msg = request.json
    print(msg)
    ListOfMessages.append(msg)
    return f"Сообщение отослано успешно. Всего сообщений: {len(ListOfMessages)} ", 200

# получение сообщений
@app.route("/get/<int:id>")
def get(id):
    return ListOfMessages[id], 200

# получение сообщений
@app.route("/vanya/<int:id>")
def getd(id):
    return f"Иван не съел {id} ёжиков", 200

def BERT_Summarizer(text):
    # https://github.com/dmmiller612/bert-extractive-summarizer
    # pip install bert-extractive-summarizer
    # pip install ...etc
    from summarizer import Summarizer
    model = Summarizer()
    result = model(text, num_sentences=3)
    return result

# отправка сообщений
@app.route("/sum", methods=['POST'])
def summi():
    msg = request.json
    text = msg['text']
    return f"{BERT_Summarizer(text)}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run()