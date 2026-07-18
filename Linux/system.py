""" This file will contain all the code to run / manuplate Linux to using it wisely is considered 
    note for file size operation everything is in GB
"""

import subprocess
from pathlib import Path
import shutil
import psutil



class Linux:
    def __init__(self) -> None:
        self.Home = Path.home()
        self.application_dir = "/usr/share/applications/"
        self.cache_dir =  self.Home /".cache"

    def _get_storage(self):
        """ Get`s Os Storage Info """
        total , used , free = shutil.disk_usage("/")
        return {
            "total": (total//2**30),
            "free": (free//2**30),
            "used":(used//2**30)
        }
    def _get_system_ram(self):
        """ Gets Os Ram info """
        system_ram = psutil.virtual_memory()
        return { 
            "total": system_ram.total/1024**3,
            "free": system_ram.free/1024**3,
            "used": system_ram.used/1024**3,
            "swap": system_ram.available/1024**3
        }

    def _get_cache_storage(self):
        """ Gets storage occupied by Cache """  
        used =  subprocess.run(['du','-sh',self.cache_dir],capture_output=True,text=True)
        return {
                "used":used.stdout.split("\t")[0],
        }
    def _get_cahe_storage_usage(self,rangeof:int = 25):
        """ Ueses bash comannd to get .config files/dir storage occupied by application 
        Note the returned value can either be in MB or GB you need to calculate it
        it takes argument reangeof:int by default it is 25 
        """
        storage = []
        application = []
        usage = {}
        used = subprocess.run(
        f"du -sh {self.cache_dir}/* | sort -rh | head -{rangeof}",
        shell=True,
        capture_output=True,
        text=True
        )
        data = used.stdout.split()
        length =  len(used.stdout.split())
        for i in range(0,length):
            if i % 2 ==0:
                storage.append(data[i])
            else:
                application.append(data[i])
    
        for i in range(0,len(application)):
          usage[application[i]] = storage[i]
        return usage

    def get_apps(self):
        """ Gets all the insatlled apps from the Os """
        for file in Path(self.application_dir).glob("*.desktop"):
            yield file
    
    def get_cache(self):
        """ Gets All the Cache that are  piled up and hugs storage """
        for file in Path(self.cache_dir).glob("*"):
            yield file

linux = Linux()
# for paths in linux.get_cache():
#     # t.sleep(0.1) 
#     print(paths)
# print(linux.get_apps())
print(linux._get_cahe_storage_usage())
