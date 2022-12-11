from termcolor import colored
from json import load, dump

class ConfigHandler:
    def __init__(self, path: str) -> None:
        self.path: str = path
        self.data: dict = self.load_data()

        print(colored("Successfully", "green"), f"loaded {self.path}")

    def load_data(self) -> dict:
        with open(self.path, "r") as json_file:
            return load(json_file)

    def get_data(self, data: str) -> dict:
        return self.data[data]