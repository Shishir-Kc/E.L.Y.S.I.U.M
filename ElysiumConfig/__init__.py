from ElysiumConfig.path_config import check_for_eLysium_path
from Errors.errors import ConfigFileMissing

if not check_for_eLysium_path():
    raise ConfigFileMissing ("there aint config file ")
