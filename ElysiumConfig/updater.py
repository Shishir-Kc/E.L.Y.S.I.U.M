"""
This file is responsible for updating and checking E.L.Y.S.I.U.M version . 
Agent can auto update at their will or when user prompts it
neither the less check updated methoid will run every instance 


"""

from pathlib import Path
import os
import json
import requests
import logging
import shutil
import subprocess

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
        self.ELYSIUM_ROOT = Path.home() / ".E.L.Y.S.I.U.M"
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
       updates = {} 
       Localconfig = self._read_local_config()
       CloudConfig = self._get_cloud_config()
       LocalMetadata = Localconfig.get("elysium",{})
       CloudMetadata = CloudConfig.get("elysium",{})
       if LocalMetadata['version'] < CloudMetadata['version']:
            logger.info("Update is Available")
            updates["version"] = CloudMetadata['version']
            if LocalMetadata['version_name'] != CloudMetadata['version_name']:
                logger.info("Major Update is Available!")
                updates['version_name'] = CloudMetadata['version_name']
            updates['stable'] = False 
            if CloudMetadata['stable'] == True:
             updates['stable'] = True
            updates['url'] = CloudMetadata['url']
            updates['repo'] = CloudMetadata['repo']
            updates['latest_changes'] = CloudMetadata['last_development_changes']
            return updates
       else:
            logger.info("No update available ")
            return updates

    def update_elysium(self):
        """ 
        This method will download and update E.L.Y.S.I.U.M automatically
        if it detects new version ! 
        1) It will delete the old version
        2) clones the new version from master branch
        3) update done
        """


        logger.info("Looking For Updates ")
        update_metadata = self.check_update()
        if not update_metadata:
            logger.info("No Updates Found")
            return update_metadata
        if not os.path.exists(self.ELYSIUM_ROOT):
            logger.info("E.L.Y.S.I.U.M Is Not Installed ")
            raise Exception ("E.L.Y.S.I.U.M Does Not Exists ")
        logger.warning("Deleting Old version")
        homedir = os.path.expanduser("~")
        os.chdir(homedir)
        try:
            for entry in os.scandir(self.ELYSIUM_ROOT):
             if entry.is_dir(follow_symlinks=False):
                shutil.rmtree(entry.path)
             else:
                os.remove(entry.path)
            logger.info("Old Version Deleted ")
        except Exception as e:
            logger.error(f"Some Error Occured While Deleting Old Versio {e}")
        try:
            logger.info("Downloading Update")
            subprocess.run(['git','clone',update_metadata['repo'],self.ELYSIUM_ROOT],check=True) 
        except Exception as e:
            logger.error(f"Something Went Wrong while updating{e}")
        logger.info("Update Downloaded")
        logger.info("Syncing UP ")
        os.chdir(self.ELYSIUM_ROOT)
        subprocess.run(['uv','sync'],check=True)
        logger.info("Sync Process Completed ")

