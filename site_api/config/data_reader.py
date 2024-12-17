import json


with open('data.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)


def get(key: str = '') -> str:
    return data.get(key)
