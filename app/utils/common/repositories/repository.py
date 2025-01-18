from abc import ABC, abstractmethod
from pyspark.sql import DataFrame
from ..services import LogService
from utils.common.glue import Glue


class Repository(ABC):
    def __init__(self, glue: Glue, log: LogService):
        self._glue = Glue
        self._log = log

    @abstractmethod
    def get_all(self) -> DataFrame:
        raise NotImplementedError

    @abstractmethod
    def get_by(self, criteria: str) -> DataFrame:
        raise NotImplementedError

    @abstractmethod
    def save(self, data: DataFrame, **kwargs):
        raise NotImplementedError
