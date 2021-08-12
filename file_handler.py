import os
import zipfile
from base_handler import BaseHandler

PATH = "python/lib/python3.8/site-packages"


class FileHandler(BaseHandler):
    def __init__(self, file: str) -> None:
        super().__init__()
        self.file = file

    def zip_folders(self) -> None:
        with zipfile.ZipFile(self.file, "w") as zip:
            for root, dirs, files in os.walk("python"):
                for filename in files:
                    file_path = os.path.join(root, filename)
                    zip.write(file_path)

    def zip_to_binary(self):
        with open(self.file, "rb") as zip:
            file = zip.read()
            return file
