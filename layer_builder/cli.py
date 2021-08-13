from boto3.session import Session


class Cli:
    def __init__(self) -> None:
        self.session = Session()
        self.regions = self._get_regions()
        self.configs = self.build_configs()

    def _get_regions(self):
        return self.session.get_available_regions("lambda")

    def _print_logo(self) -> None:
        pass

    def build_configs(self) -> dict:
        return {
            "layer_name": self.set_layer_name(),
            "description": self.set_description(),
            "libraries": self.set_lib_list(),
            "runtimes": self.set_runtimes(),
            "region": self.set_region(),
        }

    def set_description(self) -> str:
        description = input("set the description of your layer [default: none]: ")
        return description

    def set_runtimes(self) -> list:
        return ["python3.8"]

    def set_layer_name(self) -> str:
        layer_name = input("set your layer name: ")
        return layer_name

    def set_region(self) -> None:
        while True:
            region = input("set your region [default: sa-east-1]: ")

            if region not in self.regions:
                print(f"there is no region named {region}, try another one")
                continue

            return region

    def set_lib_list(self) -> None:
        while True:
            libs = input("list which libs you want to include in your layer: ")
            if libs == "":
                print("you should put at least one lib")
                continue
            break
        return self._input_into_list(usr_input=libs)

    def _input_into_list(self, usr_input: str) -> list:
        return usr_input.split(" ")
