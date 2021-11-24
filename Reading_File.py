import json
import ast
class ReadingFile:
    def __init__(self, path_read) -> None:
        """Инициализация пути"""
        self.path = path_read
    def get_data_without_json(self)->list:
        with open(self.path) as myfile:
            text = myfile.read()
        norm_text = ast.literal_eval(text)
        return norm_text
    def get_data(self) -> list:
        data = json.load(open(self.path, encoding='windows-1251'))
        return data