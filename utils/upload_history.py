import os

HISTORY_FILE = "upload_history.txt"

def save_upload_history(filename):
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(filename + "\n")

def get_upload_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        history = file.readlines()

    return [item.strip() for item in history]