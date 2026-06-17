import  logging
import os
from pathlib import Path 
import json
from Errors.errors import ConfigFileMissing
from .path_config import (download_config,show_elysium_paths,
check_for_eLysium_path,BASEDIR)

logger = logging.getLogger('ElysiumConfig.download_additionals')

CONFIGPATH = f"{BASEDIR}/config.json"
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



def download_additionals_config():
    os.makedirs(ADDITIONALSROOTPATH,exist_ok=True)
    download_url = config.get("download_url",{})
    logger.info("Downloading Additionals config")
    try:
     download_config(url=download_url,dir=ADDITIONALSROOTPATH)    
     logger.info("Additionals downloaded sucessfully")
    except Exception as e:
        logger.error(e)

download_additionals_config()

logger.info("Checking additionals path")
if not check_for_eLysium_path(path=""):
    os.makedirs("asd",exist_ok=True)

class AdditionalsDownloader:
    def __init__(self) -> None:
        pass

    def available_additionals(self):
        pass

    def download_additionals(self):
        pass
   

additionals = AdditionalsDownloader()
additionals.download_additionals()
