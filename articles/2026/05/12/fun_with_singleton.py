from __future__ import annotations

import threading
import types
import typing

class SingletonMeta[T](type):
    _instances : typing.MutableMapping[SingletonMeta[T], T] = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs) -> T:
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    if not isinstance(cls._instances, dict):
                        cls._instances = {}
                    cls._instances[cls] = instance

        return cls._instances[cls]