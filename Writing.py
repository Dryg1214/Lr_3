import json


def write_file_json(lst: list, filename) -> None:
    """Сериализация списка и запись его в словарь"""
    with open(filename + ".json", "w") as write_file:
        json.dump(lst, write_file)


def write_file_after_deserialization(lst: list, filename: str):
    """Запись списка в текстовый файл"""
    with open(filename + '.txt', 'w') as txt_file:
        for item in lst:
            txt_file.write("%s\n" % item)
