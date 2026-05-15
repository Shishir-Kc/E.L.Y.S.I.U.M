import json
import os
from internal.Errors.errors import ConfigNotFound
import argparse
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('config.log')
    ]
)

class Config:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-make',action='store_true')
        self.args = self.parser.parse_args()
        if self.args.make:
            print("yooo")

        def check_config():
            """
             this is function checks of the config is there is not if there is no config 
             it shows a custome Exception where it says ConfigNotFound try creating config 
            
            """

            if not os.path.exists('config.json'):
                raise ConfigNotFound ("""Config not found ! ........................................... :(   
                    \n Try creating the config ! with ( -make )  """)    
            return True

        self.is_config_available = check_config()



    def load(self)-> dict:
        with open('config.json','r') as data :
            config = json.load(data)

        return config
    def load_data(self):
        config = self.load()
        model = config.get("model",{})
        provider = model.get("provider")
        model_name = model.get("model_name")
        api_key = model.get("api_key")
        model_type = model.get("model_type")
        if model_type == "Cloud" and api_key =="":
            logger.warning(f" Api key not provided for the Model : {model_name} ")

if __name__ == "__main__":
    config = Config()
    print(config.load_data())
