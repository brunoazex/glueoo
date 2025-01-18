from abc import ABC, abstractmethod
from utils.common.services import LogService


class Task(ABC):
    def __init__(self, log: LogService):
        self._log = log

    @abstractmethod
    def execute(self):
        raise NotImplementedError
