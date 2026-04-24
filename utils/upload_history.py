import json
import os

FILE = "upload_history.json"

def load_history():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save_history(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

def save_upload_history(username, filename):
    data = load_history()

    if username not in data:
        data[username] = []

    data[username].append(filename)
    save_history(data)

def get_upload_history(username):
    data = load_history()
    return data.get(username, [])