import boto3
from base_handler import BaseHandler


class LambdaHandler(BaseHandler):
    def __init__(self, zipped_file: bytes) -> None:
        super().__init__()
        self.aws_client = boto3.client("lambda", region_name=self.configs["region"])

    def publish_layer(self):
        self.client_aws.publish_layer_version(
            LayerName=self.configs["layer_name"],
            Description=self.configs["description"],
            Content={"ZipFile": self.zipped_file},
            CompatibleRuntimes=list(self.configs["runtimes"]),
        )
