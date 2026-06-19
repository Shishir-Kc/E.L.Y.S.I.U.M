"""
This file contains code for doewnloading config / checking config  version / updating config 
Mainly the config is for E.L.Y.S.I.U.M Additionals (  ' plug and play ' ) architecture .
Furter more EL can automatically / independently call these methods / function as tools ,
so it can decide when to update .
The additionals code is in sepereate repo of the developer called Elysium_additionals 
Link : https://github.com/Shishir-Kc/Elysium_additionals , developer might move the code to
personal hosted server for the additionals.

What is additionals ?

well in simple terms Additionals is a way for EL to learn and controll new skills or tools to improve its performance, 
Additionals can we configured according to user liking , base version of E.Y.S.I.U.M will not contain all the functionality of Additionals
but it can be downloaded manually by cli or just ask el to download it  

"""

import  logging
import os
from pathlib import Path 
import json
from Errors.errors import AdditionalsNotFound, ConfigFileMissing
from .path_config import (download_config,show_elysium_paths,
check_for_eLysium_path,BASEDIR)

logger = logging.getLogger('ElysiumConfig.download_additionals')

CONFIGPATH = f"{BASEDIR}/config.json" # Path for config.json of ElysiumConfig
HOMEDIR = Path.home()

logging.basicConfig(
    level=logging.DEBUG,
    format="| %(levelname)s | %(asctime)s | %(name)s | %(message)s |" ,
    handlers=[
        logging.StreamHandler()
    ]
)
logger.info(f"Config path {CONFIGPATH}")



def load_additiosnals_config():
    logger.info("Loading additionals config")
    try:
     with open(CONFIGPATH,'r') as f:
        data = json.load(f)
     return data
    except FileNotFoundError:
        logger.error("Config file doesnot exists! ")
        raise FileNotFoundError


logger.info("Getting ADDITIONALSROOTPATH")
load_config = load_additiosnals_config()
config = load_config.get('elysium_additionals_config',{})
if not config:
    raise ConfigFileMissing
all_paths = show_elysium_paths(all=True)
additionals_paths = all_paths.get('elysium_additionals_paths',{})
additionals_root = additionals_paths.get('Root_path',{})

ADDITIONALSROOTPATH = f"{HOMEDIR}/{additionals_root}"
logger.info("Got ADDITIONALSROOTPATH")



def download_additionals_config(download:bool=True):
    os.makedirs(ADDITIONALSROOTPATH,exist_ok=True)
    download_url = config.get("download_url",{})
    logger.info("Downloading Additionals config")
    try:
     configs = download_config(url=download_url,dir=ADDITIONALSROOTPATH,download=download)    
     if not download:
            logger.info("Got Additionals CLOUDCONFIG ") 
            return configs
     logger.info("Additionals downloaded sucessfully") 
     return True
    except Exception as e:
        logger.error(e)
        return False

logger.info("Getting Additionals Config ")
ADDITIONALSCONFIG = f"{HOMEDIR}/{all_paths.get("additionals_config",{}).get("Config_path",{})}"
logger.info("Checking Additionals Config File")
if not Path(ADDITIONALSCONFIG).exists():
    logger.warning("Additionals Config File Missing ")
    logger.info("Auto Downloading Config File")
    download_additionals_config()
logger.info(f"Additionals Config: : : {ADDITIONALSCONFIG}")



logger.info("Checking additionals path")
if not check_for_eLysium_path(path=""):
    os.makedirs("asd",exist_ok=True)

class Additionals:
    def __init__(self) -> None:
        pass

    def additionals(self):
        with open(ADDITIONALSCONFIG,'r')as f:
            data = json.load(f)
        return data
   
    def check_update(self):
        updates={}
        LocalConfig = self.additionals()
        localconfig = list(LocalConfig)
        CloudConfig = download_additionals_config(download=False)
        logger.info("Checking for updates ")
        for _ , additional in enumerate(LocalConfig,start=0):
            if LocalConfig[additional]['version'] < CloudConfig[additional]['version']: #type:ignore
                updates[localconfig[_]] = CloudConfig[additional] #type:ignore
                logger.info(f"update available for {localconfig[_]}") 
        if not updates:
            updates = {
                "status":"Up_to_date"
            }
            logger.info("Additionals are up to date")
        return updates

    
    def download(self,update:bool=False,additional:str=""):
        if update:
            update_info= self.check_update()
            if update_info.get("status",{}) == "Up_to_date":
             return {
                "status":"Up_to_date"
            }
        if not additional:
            return {
                "status":"No_additionals_provided"
            }
        additionals = self.additionals() 
        additionalinfo = additionals.get(additional,{})
        if not additionalinfo:
            raise AdditionalsNotFound 
        additional_dir = HOMEDIR/additionalinfo.get("path","")
        os.makedirs(additional_dir,exist_ok=True)
        additional_download_url = additionalinfo.get("download_url","")
        response = download_config(url=additional_download_url,dir=additional_dir)
        dependencys =  additionalinfo.get("dependency",{})
        dependencylist = list(dependencys)
        if dependencys:
            logger.info(f"Found dependencys for {additional}")
            for _ , dependency in enumerate(dependencys):
                download_config(dir=additional_dir,url=dependencys.get(dependency)['download_url'])
                logger.info(f"Downloading Dependency: {dependencylist[_]}") 
        return response
 

additionals = Additionals()
print(additionals.download(additional="SASDASD"))
