from json import load, dump

class ConfigHandler:
    def __init__(self, path: str) -> None:
        self.path: str = path

    def get_data(self, data: str):
        with open(self.path, "r") as json_file:
            return load(json_file)[data]