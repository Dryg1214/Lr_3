import json
def write_file_json(lst: list, filename) -> None:
    """Запись в файл списка словарей"""
    with open(filename + ".json", "w") as write_file:
        json.dump(lst, write_file)

def write_file_after_deserialization(lst: list, filename):
