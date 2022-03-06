import json


def write_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, ensure_ascii=False)


def read_json(file_path):
    with open(file_path, 'w') as f:
        return json.load(f)
