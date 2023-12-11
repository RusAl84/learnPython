# import datetime
import requests
# import json


ServerAdress = "http://localhost:5000"
msg={"FILATOV PLACHET": "NE BERET"}

url = ServerAdress + "/send"
# data = json.loads(msg)  
r = requests.post(url, json=msg)