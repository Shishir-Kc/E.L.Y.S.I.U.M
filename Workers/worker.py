import threading
from Elysium_Config.path_config import ELYSIUM_PATH
import os 
import uuid

"""

i need to implement a woker json from where the code can actually get info on what to do and load it 
i need to make it so that new work can be implemented dynamicay or by an agent with out any hard coding it . 
also make the code clean ! : ) 




"""



worker_path = f"{ELYSIUM_PATH}/Config/worker"
worker_log = f"{ELYSIUM_PATH}/Logs/worker"

paths = [worker_path,worker_log]
for path in paths:
    os.makedirs(path,exist_ok=True)

class worker:
    def __init__(self) -> None:
        pass
    def check_config(self):
        pass
    def add_config(self):
        pass
    def stats(self):
        pass
    def load_config(self):
        pass

