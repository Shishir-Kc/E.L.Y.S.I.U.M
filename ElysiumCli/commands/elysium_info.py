# !/usr/bin/env python3

from pathlib import Path
from ElysiumConfig.path_config import show_elysium_paths
import json
from Server.main import logger,logging
from ElysiumConfig.updater import Updater



logger = logging.getLogger("Commands.elysium_info")

el_updater = Updater()

HOMEDIR = Path.home()
configdata = show_elysium_paths(all=True).get("elysium",{})
configpath = HOMEDIR/ ".E.L.Y.S.I.U.M"/ configdata.get("config",{})


def readconfig():
    with open(configpath,"r") as file:
        data = json.load(file)
    return data.get("elysium",{})



def version(args=None):
    version = readconfig().get("version",{})
    logger.info(f"Version : {version}")
    return version

def status(args=None):
    status = readconfig().get("status",{})
    logger.info(f"Status : {status}")
    return status

def last_development_changes(args=None):
    dev = readconfig().get("last_development_changes",{}) 
    logger.info(f" last_development_changes : {dev}")
    return dev

def version_name(args=None):
    name = readconfig().get("version_name",{}) 
    logger.info(f"version_name : {name}")
    return name 
def is_stable(args=None):
    stable = readconfig().get("status",{}) 
    logger.info(f"Is_stable : {stable}")
    return stable


def elysium_info(args=None):
    print(f""" 
    
    Version : {version()},
    Version Name  : {version_name()},
    Stable : {is_stable()}
    Last Development Changes : {last_development_changes()}

    """)

def check_verison(args=None):
    update = el_updater.check_update()
    logger.info(f"Update Status : {update}")
    return update

def update(args:None):
   el_updater.update_elysium()

