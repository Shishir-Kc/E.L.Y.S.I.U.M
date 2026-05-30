import threading
from Elysium_Config.path_config import ELYSIUM_PATH
import os 


worker_path = f"{ELYSIUM_PATH}/Config/worker"
worker_log = f"{ELYSIUM_PATH}/Logs/worker"

paths = [worker_path,worker_log]
for path in paths:
    os.makedirs(path,exist_ok=True)

class worker:
    def __init__(self) -> None:
        pass
    def check_worker_config(self):
        pass
    def add_config(self):
        pass
    def load_worker_config(self):
        pass

