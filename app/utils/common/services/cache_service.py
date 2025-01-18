from dataclasses import dataclass
from pyspark.sql import types as T, DataFrame
from ..repositories import S3Repository


@dataclass
class CacheTable(object):
    table: str
    schema: T.StructType


class CacheService:
    def __init__(self, s3: S3Repository):
        self._s3 = s3
        self._path_prefix = 'cache'

    def get(self, table: CacheTable) -> DataFrame:
        pass

    def save(self, data: DataFrame, table: CacheTable):
        pass
