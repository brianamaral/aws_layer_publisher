import boto3
from base_handler import BaseHandler


class LambdaHandler(BaseHandler):
    def __init__(self, zipped_file: bytes, cli) -> None:
        super().__init__(cli=cli)
        self.aws_client = boto3.client("lambda", region_name=self.configs["region"])
        self.zipped_file = zipped_file

    def _return_layer_info(self, layer_info: dict) -> None:

        print(self._cut_layer_json(layer_info=layer_info))

    def _cut_layer_json(self, layer_info: dict) -> dict:
        return dict(
            (key, value)
            for key, value in layer_info.items()
            if key
            in [
                "LayerArn",
                "LayerVersionArn",
                "CreatedDate",
                "Version",
                "CompatibleRuntimes",
            ]
        )

    def publish_layer(self) -> dict:
        layer_info = self.aws_client.publish_layer_version(
            LayerName=self.configs["layer_name"],
            Description=self.configs["description"],
            Content={"ZipFile": self.zipped_file},
            CompatibleRuntimes=list(self.configs["runtimes"]),
        )

        self._return_layer_info(layer_info=layer_info)
