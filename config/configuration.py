import os
import configparser

env = os.environ.get("ENV")

cParser = configparser.ConfigParser()
cParser.read("config.toml", encoding="utf-8")

Config = cParser["default"]

if env in cParser:
    print("Config environment: {0}".format(env))
    Config.update(cParser[env])
else:
    print("{0} enviroment not found in config.toml".format(env))

Config["env"] = env