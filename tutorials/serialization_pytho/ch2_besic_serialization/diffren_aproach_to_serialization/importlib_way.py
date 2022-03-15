"""load configuration with importlib"""
from importlib.machinery import SourceFileLoader


def load_config_importlib(path):
    """load configuration from path"""
    return SourceFileLoader('config', path).load_module()