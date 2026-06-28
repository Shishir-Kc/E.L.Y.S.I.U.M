"""
This file is responsible for updating and checking E.L.Y.S.I.U.M version . 
Agent can auto update at their will or when user prompts it
neither the less check updated methoid will run every instance 


"""
from pathlib import Path
import os
import json
from time import sleep
import requests
from .path_config import GENERAL_CONFIG_PATH
import logging

logger = logging.getLogger("ElysiumConfig.updater")

logging.basicConfig(
    level=logging.DEBUG,
    format="| %(levelname)s | %(asctime)s | %(name)s | %(message)s |",
    handlers=[
        logging.StreamHandler()
    ]
)

class Updater:
    def __init__(self) -> None:
            
        self.LOCALCONFIG = Path.home() / ".E.L.Y.S.I.U.M/ElysiumConfig/config.json"
        self.CLOUDCONFIG =  self._get_cloud_config()

    def _read_local_config(self):
        local_config_path= self.LOCALCONFIG
        with open(local_config_path,'r') as file:
            data = json.load(file)

        return data

    def _get_cloud_config(self)->dict:
      logger.info("Getting Cloud Config") 
      try:
           localconfig = self._read_local_config()
           logger.info(localconfig)
           metadata = localconfig.get("elysium",{})      
           config_url = metadata.get("url","")
           logger.info("Capturing Cloud Config")
           try:
                response = requests.get(url=config_url)
                return response.json()
           except Exception as e:
                logger.debug(e)
                return {}
      except Exception as e:
            logger.debug(e)
            return{}

    def check_update(self):
       updater = {} 
       Localconfig = self._read_local_config()
       CloudConfig = self._get_cloud_config()
       LocalMetadata = Localconfig.get("elysium",{})
       CloudMetadata = CloudConfig.get("elysium",{})
       if LocalMetadata['version'] < CloudMetadata['version']:
            logger.info("Update is Available")
            if LocalMetadata['version_name'] != CloudMetadata['version_name']:
                logger.info("Major Update is Available!")


updater = Updater()
updater.check_update()
