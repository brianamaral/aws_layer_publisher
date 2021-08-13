import os
import zipfile
from base_handler import BaseHandler
import logging


PATH = "python/lib/python3.8/site-packages"
logging.basicConfig(level=logging.INFO)


class FileHandler(BaseHandler):
    def __init__(self, file: str, cli) -> None:
        super().__init__(cli=cli)
        self.file = file

    def zip_folders(self) -> None:
        with zipfile.ZipFile(self.file, "w") as zip:
            for root, dirs, files in os.walk("python"):
                for filename in files:
                    file_path = os.path.join(root, filename)
                    logging.info(f"zipping: {file_path}")
                    zip.write(file_path)

    def zip_to_binary(self):
        with open(self.file, "rb") as zip:
            file = zip.read()
            return file
