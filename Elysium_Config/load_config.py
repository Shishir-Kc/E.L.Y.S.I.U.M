"""
    yo yo yo ! sup , so this model_config file is needed and it only contains " free models " 
    if you want to add a paid model make sure that it is compatable with langchain primarly 
    the provider should be compatable ! . 


"""
import json
import os
from pathlib import Path
import logging
import argparse
import requests

BASEDIR = Path(__file__).resolve().parent

logger=logging.getLogger(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s |  %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(f"{BASEDIR}/model_config.log")
    ]
)

class Elysium_Model_Config:
    def __init__(self) -> None:
        self.pre_load_config =self.load_config()
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-download_config',action='store_true')
        self.args = self.parser.parse_args()
        self.default_config_url="https://raw.githubusercontent.com/Shishir-Kc/Assets/main/Elysium_config/model_config.json"
        self.config_name = "model_config.json"
        logger.info("loading model_config . . . . ")
        if self.args.download_config:
            self.download_config()
    def load_config(self)->dict:
     try:
        with open(f'{BASEDIR}/{self.config_name}','r') as file:
            data = json.load(file)            
        return data
     except:
        print("something went wrong !")
        return {}
    def available_providers(self):
        info=" |  {num} | provider => {name} "
        for  i , provider  in enumerate(self.pre_load_config,start=1):
            print(info.replace("{name}",provider).replace("{num}",str(i)))
    def download_config(self, url:str | None=None):
        if url is None:
            url = self.default_config_url
            response = requests.get(url)
            with open(f"{BASEDIR}/{self.config_name}","w") as data:
                json.dump(response.json(),data,indent=2)

el = Elysium_Model_Config()
el.available_providers()

