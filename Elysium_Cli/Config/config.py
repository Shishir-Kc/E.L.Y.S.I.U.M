import json
import os
from internal import ConfigNotFound,InvalidArgsFound
import argparse
import logging
from pydantic import BaseModel
from pathlib import Path

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('Config/config.log')
    ]
)

BASEDIR= Path(__file__).parent


class Model_Schema(BaseModel):
    provider:str|None
    model_name:str|None
    api_key:str|None
    model_type:str|None



class Config:
    def __init__(self) -> None:
        self.base_config_path = f'{BASEDIR}/config.json'
        self.sad_face = ". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . :("
        self.happy_face = ". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . :)"
        self.default_config = {
                     "model":{
                    "provider": "provider_name(Google , OpenAI , Anthropic )",
                    "model_name": "model_name (gemini-3.1-flash-lite , gtp-5.4 , claude-sonnet-4-6",
                    "api_key": "XAPIX",
                    "model_type": "Local/Cloud"
                    }
                } 
        def make_config(over_ride:bool=False)->None:
            if not os.path.exists(self.base_config_path):
                with open(self.base_config_path,'w') as data:
                    json.dump(self.default_config,data,indent=2)
                print(" Default config.json has been created ")
            if over_ride:
                with open(self.base_config_path,'w') as data:
                    json.dump(self.default_config,data,indent=2)


        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-make',action='store_true')
        self.parser.add_argument('-over_ride',action='store_true')
        self.parser.add_argument('-add_config',action='store_true')
        self.args = self.parser.parse_args()
        
        if self.args.make:
            # here if there is not premade config then it will make a default config . 
            # all the values will be null !  
            logger.info("Creating Default config"+self.happy_face)
            
            make_config() 

        if self.args.over_ride:
            """
                 so basically it over writes the config.json file with the predefine 
                 self.default_config . in short u run this your config goo boom ! 
            """

            logger.warning("Warning Your Config.json file will be over_rided with default config.json")
            try:
             user_permission = input(" Are You Sure ? Anything/n => ")
             if not user_permission == "n":
                logger.info("Creating default config.json ")
                make_config(over_ride=True)
             else:
              logger.info(" Operation (over_ride) Canceled")

            except KeyboardInterrupt as e :
                logger.info("Stopped (over_ride) Process" , e)

        if self.args.add_config:
            logger.info("Adding Values "+self.happy_face)
            self.input_config()

        def check_config()->None:
            """
             this is function checks of the config is there is not if there is no config 
             it shows a custome Exception where it says ConfigNotFound try creating config 
            
            """

            if not os.path.exists(self.base_config_path):
                raise ConfigNotFound ("Config not found !  \n Try creating the config ! with ( -make )  ")    
             

        check_config()
    

    def input_config(self):
        config:dict[str,str]={} 
        try:
          for i in self.default_config['model'].keys():
            user_input = str(input(f"Enter {i} => "))
            config[i]=user_input 
          self.update_config(**config)
        except KeyboardInterrupt as e:
         logger.info(f"Adding (config key) Interrupted ! {e}" + self.sad_face)
         print(f"Stopped {self.sad_face}")
    def update_config(self,**kwargs):
        try:
            validate = Model_Schema(**kwargs)
        except ValueError as e:
            logger.warning(f"Invalid Args or missing \n Check this {e}")
            raise InvalidArgsFound(f"Invalid args ! {self.sad_face} ")
        config = self.load()
        with open(self.base_config_path,'w') as data: 
            config['model']=validate.model_dump(exclude_none=True)
            try: 
             json.dump(config,data,indent=2)
            except Exception as e:
                logger.warning(f"Something Terriable has gone wrong ! check this out ! {e}" + self.sad_face)

    def load(self)-> dict:
        try: 
            with open(self.base_config_path,'r') as data :
             config = json.load(data)
            return config
        except json.JSONDecodeError as e:
            logger.warning(e)
            print(f"Failed to Load content from config.json \n Try overriding the config.json to default {self.sad_face}")
            print(" Command ? \n \n here =>  uv run config.py -make -over_ride \n")
            return {
                "Error":e
            }
    def load_data(self)->dict:
        config = self.load()
        model = config.get("model",{})
        model_name = model.get("model_name")
        provider = model.get("provider")
        api_key = model.get("api_key")
        model_type = model.get("model_type")
        if model_type == "Cloud" and api_key =="":
            logger.warning(f" Api key not provided for the Model : {model_name}  {self.sad_face} ")
            try:
                api_key = str(input("API_KEY: "))
                self.update_config(
                                  provider=provider,
                                   api_key=api_key,
                                   model_name=model_name,
                                   model_type=model_type)
            except KeyboardInterrupt:
                logger.warning(f"API_KEY not saved!  {self.sad_face} ")
        return (model)

if __name__ == "__main__":
    config = Config()
    

