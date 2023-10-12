import tomli
import tomli_w
import os

class TomlFile:
    settings = None
    filename = None
    configFilePath = None

    def __init__(self, filename:str):
        if filename == None:
            return

        self.configFilePath = os.path.join("/home/vdizon", ".config", filename)
        try:
            with open(self.configFilePath, 'rb') as toml_file:
                self.settings = tomli.load(toml_file)
        except FileNotFoundError:
            file = open(self.configFilePath, 'x')
            with open(self.configFilePath, 'rb') as toml_file:
                self.settings = tomli.load(toml_file)




    def getValue(self, key:str):
       try:
           return self.settings[key]
       except KeyError:
            return None

    def addValue(self, key:str, value):
        self.settings[key] = value 

        with open(self.configFilePath, 'wb') as toml_file:
            tomli_w.dump(self.settings, toml_file)
