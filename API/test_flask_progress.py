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
    
@app.route("/send", methods=['POST'])
def send():
    msg = request.json
    print(msg)
    ListOfMessages.append(msg)
    return f"Сообщение отослано успешно. Всего сообщений: {len(ListOfMessages)} ", 200

@app.route("/get/<int:id>")
def get(id):
    return ListOfMessages[id], 200

@app.route("/vanya/<int:id>")
def getd(id):
    return f"Иван не съел {id} ёжиков", 200

@app.route("/vanya", methods=['POST'])
def vanya():
    msg = request.json
    text = msg['text']
    return f"{text[::-1]}", 200

@app.route("/get_value")
def get_value():
    return f"{progress}", 200

@app.route("/up_value")
def up_value():
    global progress
    progress+=0.01
    return f"{progress}", 200

@app.route("/down_value")
def down_value():
    global progress
    progress-=0.01
    return f"{progress}", 200

if __name__ == '__main__':
    global progress
    progress = 0
    app.run(host='0.0.0.0')
    # app.run()