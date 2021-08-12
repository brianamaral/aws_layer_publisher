import json


class BaseHandler:
    def __init__(self) -> None:
        self.configs = self._read_configs()

    def _read_configs(self) -> dict:
        with open("configs.json", "r") as config_file:
            config = json.load(config_file)
            return config

