from domain.repositories import (
    CustomerSourceRepository,
    CustomerTargetRepository
)
from utils.common.services import CacheService, CacheTable
from pyspark.sql import DataFrame, types as T
from datetime import datetime


class CustomerService:
    def __init__(
        self,
        customers_source: CustomerSourceRepository,
        customers_target: CustomerTargetRepository,
        cache: CacheService
    ):
        self._customers_source = customers_source
        self._customers_target = customers_target
        self._cache = cache
        self._cache_table = CacheTable(
            "customers",
            T.StructType([
                T.StructField("id", T.StringType(), False),
                T.StructField("doc_id", T.StringType(), False)
            ])
        )

    def load(self) -> DataFrame:
        anomesdia = datetime.now().strftime("%Y%m%d")
        self._customers_source.get_by(f"anomesdia={anomesdia}")

    def transform(self, raw_data: DataFrame) -> DataFrame:
        cache = self._cache.get(self._cache_table)
        return (
            raw_data.alias('actual')
            .join(
                cache.alias('cached'),
                'doc_id',
                'inner'
            )
            .select('cache.id', 'actual.*')
        )

    def persist(self, data: DataFrame):
        self._customers_target.save(
            data=data,
            table='customers'
        )
