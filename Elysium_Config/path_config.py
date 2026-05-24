from pathlib import Path
import os
import json
import requests

BASEDIR = Path(__file__).parent
GENERAL_CONFIG_PATH = f"{BASEDIR}/path_config.json"
ELYSIUM_PATH= f"{Path.home()}/.config/E.L.Y.S.I.U.M"


def check_for_eLysium_path()-> bool:
    try:
        if os.path.exists(ELYSIUM_PATH):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def get_elysium_path(of:str=""):
    with open(GENERAL_CONFIG_PATH,"r") as data:        
        config = json.load(data)
    elysium_path = config.get("elysium_paths",{})
    return elysium_path.get(of)

def show_elysium_paths()->dict:
    paths = {}
    with open(GENERAL_CONFIG_PATH,"r") as file:
        data = json.load(file)
    elysium_paths = data.get("elysium_paths",{})
    for i ,path_name in enumerate(elysium_paths,start=1):
        paths[i] = path_name
    return paths

def download_config(dir:str,url:str)-> bool:
    if dir=="" or url=="":
        raise Exception ("dir or url is not provided !")
    
    dir = f"{ELYSIUM_PATH}/{dir}"
    try:
        response = requests.get(url)

        with open(dir,'w')as data:
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


# download_config(dir=str(input("dir:>")),url=str(input("URL : > ")))
# print(load_elysium_paths())
# print(show_elysium_paths())
