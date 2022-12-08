import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
global df
df = ""


@app.route('/')
def dafault_route():
    return 'Test server'


@app.route('/elena')
def nastya_route():

    return 'Elena TOP'


@app.route("/api/schedule", methods=['POST'])
def schedule():
    data = request.json
    teacher = str(data['teacher'])
    week = str(data['week'])
    return_data = []
    line = {}
    item = df.loc[11, :].values.tolist()
    line["inst"] = str(item[0])
    line["groups"] = str(item[1])
    line["num_day"] = str(item[2])
    line["num_subj"] = str(item[3])
    line["week"] = str(item[4])
    line["subj_name"] = str(item[5])
    line["subj_type"] = str(item[6])
    line["teach_name"] = str(item[7])
    line["aud_name"] = str(item[8])
    return_data.append(line)
    return_data.append(line)
    print(return_data)
    str_return_data = json.dumps(return_data)
    return str_return_data
    # return f"{teacher} {str(week)}"


@app.route("/dron/<int:id>", methods=['get'])
def dron(id):
    return f"Артём не съел {id} ёжиков"


@app.route("/api/teachers", methods=['get'])
def teachers():
    teachers = ["teach1", "teach2"]
    str_return_data = json.dumps(teachers)
    return str_return_data


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
