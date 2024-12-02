import os
import json
import requests
from PyQt6.QtWidgets import QMessageBox


def popup_window(title : str, text : str):
    window = QMessageBox()
    window.setWindowTitle(title)
    window.setText(text)
    window.exec()

def get_request(api : str, path : str):
    try:
        response = requests.get(api)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http:
        popup_window("Ошибка", f"Ошибка: {http}")
    except requests.exceptions.ConnectionError as cn:
        popup_window("Ошибка", f"Ошибка: {cn}")
    except requests.exceptions.Timeout as tm:
        popup_window("Ошибка", f"Ошибка: {tm}")
    except requests.exceptions.RequestException as re:
        popup_window("Ошибка", f"Ошибка: {re}")
    else:
        with open(os.path.join(path, "result.json"), 'w') as fl:
            json.dump(response.json(), fl, ensure_ascii=False, indent=4)
        
        return True

    return False

def post_request(api : str, path : str):
    try:
        response = requests.post(api)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http:
        popup_window("Ошибка", f"Ошибка: {http}")
    except requests.exceptions.ConnectionError as cn:
        popup_window("Ошибка", f"Ошибка: {cn}")
    except requests.exceptions.Timeout as tm:
        popup_window("Ошибка", f"Ошибка: {tm}")
    except requests.exceptions.RequestException as re:
        popup_window("Ошибка", f"Ошибка: {re}")
    else:
        with open(os.path.join(path, "result.json"), 'w') as fl:
            json.dump(response.json(), fl, ensure_ascii=False, indent=4)
        
        return True

    return False