import datetime
import yaml

class Configuration(object):
    def __init__(self):
        self.config_file_path = ".\\config.yaml"

    
    def get_config(self, script_name):
        with open(self.config_file_path, "r") as f:
            try:
                config_yaml = yaml.safe_load(f)
                for script_config in config_yaml["scripts"]:
                    if script_config["name"] == script_name:
                        return script_config
            except yaml.YAMLError as e:
                print("{0}|error|{1}".format(datetime.datetime.now(), e))