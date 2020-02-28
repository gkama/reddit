import datetime
import json
import yaml

from logzero import logger


class Configuration(object):
    def __init__(self):
        self.config_json_file_path = ".\\config.json"
        self.config_yaml_file_path = ".\\config.yaml"

    
    def get_config(self, script_name):
        with open(self.config_yaml_file_path, "r") as f:
            try:
                config_yaml = yaml.safe_load(f)
                for script_config in config_yaml["scripts"]:
                    if script_config["name"] == script_name:
                        return script_config
            except yaml.YAMLError as e:
                logger.exception(e)

    
    def get_json_config(self):
        with open(self.config_json_file_path, "r") as f:
            try:
                return json.loads(f.read())
            except Exception as e:
                logger.exception(e)
