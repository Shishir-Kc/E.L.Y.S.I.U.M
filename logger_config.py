import logging
from Errors.errors import MalformedLog

def set_up_logging(level:str="DEBUG",logpath:str=""):
    """ 
    This function will setup a basic logging config , 
    if you want to change the logging level pass the desired level in the args eg level="INFO"
    or if u want to save logs in a specific dir u can pass the dir in the args eg logpath="user/sys/loGs.log"
    it must end with .log 
    """
    try:
     handlers=[logging.StreamHandler()]
     if logpath:
        if not logpath.endswith(".log"):
            raise MalformedLog ("It does not end with .log")

        handlers.append(logging.FileHandler(logpath)) #type:ignore
     logging.basicConfig(
      level = level.upper(),
      handlers=handlers, 
      format="| %(asctime)s | %(levelname)s | %(name)s | %(message)s |"
      )
    except Exception as e:
        print(e)


