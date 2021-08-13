from .cli import Cli
from .pip_handler import PipHandler
from .file_handler import FileHandler
from .lambda_handler import LambdaHandler


def handle():
    cli = Cli()

    pip_handler = PipHandler(cli=cli)

    pip_handler.install_dependencies()

    file_handler = FileHandler(file="python.zip", cli=cli)

    file_handler.zip_folders()

    binary_zip = file_handler.zip_to_binary()

    lambda_handler = LambdaHandler(zipped_file=binary_zip, cli=cli)

    lambda_handler.publish_layer()

if __name__ == '__main__':
    handle()

