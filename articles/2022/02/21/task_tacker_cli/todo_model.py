import datetime

from enum import Enum, IntEnum

class Status(IntEnum):
    OPEN = 0
    COMPLTED = 1


class Todo:
    def __init__(self,
                 task,
                 category,
                 date_added=None,
                 date_completed=None,
                 status=Status.OPEN,
                 position=None):
        self.task = task
        self.category = category
        self.date_added = date_added if date_added is not None else datetime.datetime.now().isoformat()
        self.date_completed = date_completed
        self.status = status
        self.position = position


    def __repr__(self) -> str:
        return f"Todo({self.task}, {self.category}, {self.date_added}, {self.date_completed}, {self.status}, {self.position}"

