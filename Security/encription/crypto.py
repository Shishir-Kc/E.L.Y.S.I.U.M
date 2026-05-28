"""
    generate_key() -> will generate_key and returns it in bytes ! 
    encrypt() -> will encrypt key , arguments [item,key] 
    dencrypt() -> will dencrypt key , arguments [item,key] 
     
"""

from cryptography.fernet import Fernet
from Elysium_Config.path_config import ELYSIUM_PATH
import os 
import logging
import json

ENCRYPTION_KEYS_PATH = f"{ELYSIUM_PATH}/Config/Security/encryption"
ENCRYPTION_KEYS_LOG_PATH = f"{ELYSIUM_PATH}/Logs/Security/encryption"
paths = [ENCRYPTION_KEYS_PATH,ENCRYPTION_KEYS_LOG_PATH]
for path in paths:
    if  not os.path.exists(path):
     os.makedirs(path,exist_ok=True)
logger = logging.getLogger('cryptography')
logging.basicConfig(
    level = logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(f"{ENCRYPTION_KEYS_LOG_PATH}/cryptography.log")
    ]
)
def generate_key(process:str):
    logging.info(f"creating key for process {process}")
    key = Fernet.generate_key()

    new_entry = {
        "process": str(process),
        "key": key.decode("utf-8")  
    }

    keys_file = f"{ENCRYPTION_KEYS_PATH}/keys.json"
    if os.path.exists(keys_file):
        with open(keys_file, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(new_entry)

    with open(keys_file, "w") as f:
        json.dump(data, f, indent=2)

def encrypt(item,key):
    logging.info("encrypting key")
    key = Fernet(key)
    return key.encrypt(item)
def decrypt(item,key):
    logger.info("dencrypting key")
    key=Fernet(key)
    return key.decrypt(item).decode()

generate_key(process="idk")
