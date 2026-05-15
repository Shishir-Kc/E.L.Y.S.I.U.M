import json
import os
from internal.Errors.errors import ConfigNotFound


class Config:
    def __init__(self) -> None:
        def check_config():
            if not os.path.exists('config.json'):
                raise ConfigNotFound ("""Config not found ! ........................................... :(   
                    \n Try creating the config ! """)            
            return True

        self.is_config_available = check_config()

    def load(self)-> dict:
        with open('config.json','r') as data :
            config = json.load(data)

        return config


if __name__ == "__main__":
    config = Config()
    print(config.load())
