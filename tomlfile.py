import tomli
import os

class TomlFile:
    settings = None
    filename = None
    configFilePath = None

    def __init__(self, filename:str):
        if filename == None:
            return
    
        self.configFilePath = os.path.join(os.path.expanduser("~"), ".config", filename)
        with open(self.configFilePath, 'rb') as toml_file:
            self.settings = tomli.load(toml_file)

    def getValue(self, key:str):
       try:
           return self.settings[key]
       except KeyError:
           return None

    def addValue(self, key:str, value):
        settings[key] = value 

        with open(self.configFilePath, 'rb') as toml_file:
            tomli.dump(self.settings, toml_file)
