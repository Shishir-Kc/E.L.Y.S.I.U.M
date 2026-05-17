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
from Errors.errors import ProviderNotGiven,ModelNameNotGiven,ApiKeyNotGiven

BASEDIR = Path(__file__).resolve().parent

logger=logging.getLogger(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s |  %(message)s",
    handlers=[
        # logging.StreamHandler(),
        logging.FileHandler(f"{BASEDIR}/model_config.log")
    ]
)

class Elysium_Model_Config:
    def __init__(self) -> None:
        self.config_name = "model_config.json" 
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-download_config',action='store_true',help="downlads pre-defined model config ")
        self.parser.add_argument('-make',action='store_true',help="make pre-defined model config")
        self.parser.add_argument('-insert_api',action="store_true",help="update api key ")
        self.args = self.parser.parse_args()
        self.default_config_url="https://raw.githubusercontent.com/Shishir-Kc/Assets/main/Elysium_config/model_config.json"  
        if self.args.download_config:
            logger.info("user started config installation")
            try:
             self.download_config(url=input("Enter Custom Config URL or Leave It Empty => "))
            except KeyboardInterrupt:
                logger.error("User cancled the installation ")
            except Exception as e:
                logger.error(f"something is not right ! {e}")
        if self.args.make:
            if not self.check_model_config_path():
                self.download_config()
             
        self.pre_load_config =self.load_config()

    def check_model_config_path(self)->bool:
        if not os.path.exists(f"{BASEDIR}/{self.config_name}"):
            logger.warning(f"{self.config_name} does not exists !")
            return False
        logger.info(f"{self.config_name} exists :) ")
        return True

    def load_config(self)->dict:
     logger.info("trying to load model_config")
     try:
        with open(f'{BASEDIR}/{self.config_name}','r') as file:
            data = json.load(file)           
            logger.info(f"{self.config_name} Loaded ! ")
        return data
     except FileNotFoundError:
        logger.error(f"{self.config_name} not found in {BASEDIR}")
        logger.info(f" it seems like {self.config_name} has not  been created try ( -make )")
        return {}
     except Exception as e:
        logger.error(f"Looks like something went wrong {e}")
        return {}

    def available_providers(self):
        info= " |  {num} | provider => {name} "
        for  i , provider  in enumerate(self.pre_load_config,start=1):
            print(info.replace("{name}",provider).replace("{num}",str(i)))
    
    def insert_api_key(self,provider_name:str,model_name:str,api_key:str):
         model_config = self.load_config()
         logger.info("Appying Custom API key ")
         if not provider_name:
            logger.error("Provider not Givem")
            raise ProviderNotGiven("Excepted provider name")
         if not api_key:
            logger.error("API key not given")
            raise ApiKeyNotGiven("Excepted API Key")
         if not model_name:
            logger.error("Model_name not given")
            raise ModelNameNotGiven("Excepted Model name ")
         get_providers_models = model_config.get(provider_name,{})
         [get_providers_models.pop(otherstuff,None) for otherstuff in ["auth","requires","installation","priority"]]
         return get_providers_models

    def download_config(self, url:str | None = None):
        if not url:
            url = self.default_config_url
            logger.info("Using default config url ")
        logger.info(f"Using custom url '{url}'")
        try:
           response = requests.get(url)
           response.raise_for_status()
           with open(f"{BASEDIR}/{self.config_name}","w") as data:
            json.dump(response.json(),data,indent=2)
            logger.info(f"downloading config from {url}")
           if not self.check_model_config_path():
            logger.error("Unsucessful to install !")
        except requests.RequestException as e:
            logger.error(f"Request failed {e}")
        except(ConnectionError, ConnectionAbortedError, ConnectionRefusedError)as e:
         logger.error(f"Connection Error checks the logs ! {e}")
        except Exception as e:
                logger.error(f"Something went south ! {e}")
 
if __name__ == "__main__":    
    el = Elysium_Model_Config()
    print("Use -h for more info ")

