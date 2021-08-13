import json
from cli import Cli


class BaseHandler:
    def __init__(self, cli: Cli) -> None:
        self.configs = cli.configs
