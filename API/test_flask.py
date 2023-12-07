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

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run()