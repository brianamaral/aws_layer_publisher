import os
import subprocess
import sys
from .base_handler import BaseHandler
import logging


logging.basicConfig(level=logging.ERROR)
PATH = "python/lib/python3.8/site-packages"


class PipHandler(BaseHandler):
    def __init__(self, cli) -> None:
        super().__init__(cli=cli)
        self._build_dirs()

    def _build_dirs(self) -> None:
        os.makedirs(PATH, exist_ok=True)

    def install_dependencies(self) -> None:
        for dependencie in self.configs["libraries"]:
            try:
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", dependencie, "-t", PATH]
                )
            except subprocess.CalledProcessError:
                continue
