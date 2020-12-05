import os

from configparser import ConfigParser

config_file_path = os.path.normpath(os.path.join(os.path.abspath(__name__), "..", "config.ini"))
# get config file
config = ConfigParser()
config.read(config_file_path)
