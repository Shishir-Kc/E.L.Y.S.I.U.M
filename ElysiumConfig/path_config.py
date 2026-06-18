import logging
from pathlib import Path
import os
import json
import requests

BASEDIR = Path(__file__).parent
GENERAL_CONFIG_PATH = f"{BASEDIR}/path_config.json"
logger = logging.getLogger("ElysiumConfig.path_config")
logging.basicConfig(
    level=logging.DEBUG,
    format="| %(levelname)s | %(asctime)s | %(name)s | %(message)s |" ,
    handlers=[
        logging.StreamHandler()
    ]

)

def get_elysium_path(of:str=""):
    with open(GENERAL_CONFIG_PATH,"r") as data:        
        config = json.load(data)
    elysium_path = config.get("elysium_paths",{})
    return elysium_path.get(of)


ELYSIUM_PATH= f"{Path.home()}/{get_elysium_path(of="Root_path")}"


def check_for_eLysium_path(path:str="")-> bool:
    elysium_path = path
    if not path:
        elysium_path = ELYSIUM_PATH    
   
    logger.info(elysium_path)
    try:
        if os.path.exists(elysium_path):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def show_elysium_paths(all:bool=False)->dict:
    paths = {}
    with open(GENERAL_CONFIG_PATH,"r") as file:
        data = json.load(file)
    elysium_paths = data
    if not all:
        for i ,path_name in enumerate(elysium_paths,start=1):
         paths[i] = path_name
        return paths
    return data

def download_config(dir:str,url:str,download:bool=True)-> bool:
    if dir=="" or url=="":
        raise Exception ("dir or url is not provided !")
    file_name = Path(url).name
    path = f"{dir}/{file_name}"
    try:
        response = requests.get(url)
        if not download:
            return response.json()
        with open(path,'w')as data:
            json.dump(response.json(),data,indent=2)
        return True
    except requests.ConnectTimeout:
        raise Exception ("timed out")
    except requests.HTTPError:
        raise Exception("http error")
    except requests.ReadTimeout:
        raise Exception("is server dead ")
    except Exception as e:
        print(f"Some thing went wrong ! {e}")
    return False 


