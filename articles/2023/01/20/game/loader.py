
import importlib

from typing import Callable

from game import factory


class PluginInterface:
    """Has  a single function"""
    @staticmethod
    def initialize(register_func: Callable) -> None:
        """Initialize the plugin"""

def import_module(name: str) -> PluginInterface:
    return importlib.import_module(name) # type: ignore

def load_plugins(plugins: list[str]) -> None:
    for plugin_name in plugins:
        plugin = import_module(plugin_name)
        plugin.initialize(factory.register)