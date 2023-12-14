import requests

while(True):
    r = requests.get("http://localhost:5000/down_value", timeout=0.005)
    print(r.text)